#! /udr/bin/python3

import random
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    
    # Define Position of Robot to spawn in the simulation world
    position = [0.0, 0.0, 0.2]

    # Define Orientation of Robot to spwan in the simulation world
    orientation = [0.0, 0.0, 0.0]

    # Robot Base name
    robot_base_name = "box_bot"
    entity_name = robot_base_name+"-"+str(int(random.random()*100000))

    # Spawn the Robot
    spawn_robot_node = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        name="spwan_entity",
        output="screen",
        arguments=['-entity',
                   entity_name,
                   '-x', str(position[0]), 
                   '-y', str(position[1]),
                   '-z', str(position[2]),
                   '-R', str(orientation[0]), 
                   '-P', str(orientation[1]),
                   '-Y', str(orientation[2]),
                   '-topic', '/robot_description'
                   ]
    )

    # Create and return the Launch Description Object
    return LaunchDescription(
        [
            spawn_robot_node
        ]
    )
