import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node

def generate_launch_description():
    
    # Input Data Files
    urdf_file = "box_bot_physical_properties.urdf"
    package_description = "my_box_bot_description"

    print("Fetching URDF ====>")
    robot_description_path = os.path.join(get_package_share_directory(package_name=package_description), "urdf", urdf_file)

    # Robot State Publisher
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        name="robot_state_publisher_node",
        output="screen",
        emulate_tty=True,
        parameters=[{'use_sim_time': True, 'robot_description': Command(['xacro ', robot_description_path])}],   
    )

    # RVIZ Configuration
    rviz_file = "urdf_vis.rviz"
    rviz_config_dir = os.path.join(get_package_share_directory(package_name=package_description), "rviz", rviz_file)
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        output="screen",
        name="rviz_node",
        parameters=[{'use_sim_time': True}],
        arguments=['-d', rviz_config_dir])
    

    # Create and return launch description object
    return LaunchDescription(
        [
            robot_state_publisher_node,
            rviz_node
        ]
    )