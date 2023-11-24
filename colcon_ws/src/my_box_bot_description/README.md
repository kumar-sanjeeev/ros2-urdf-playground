# My Box Bot Description

This ROS2 package contains URDF files for the custom My Box Robot.

## Package Structure

The package Tree structure is as follows:

```.
├── CMakeLists.txt
├── config
├── launch
├── meshes
├── package.xml
├── README.md
├── rviz
└── urdf
```
`urdf:` 

This directory contains various URDF files used to describe the custom my_box_robot. Each file has been created to explore different available tags and their usage for simulation in a physics simulator.

- `box_bot_simple.urdf:` Contains two links and one joint.
- `box_bot_geometric.urdf:` Defines the box bot whose shape is described using simple geometric primitives available in URDF format.
- `box_bot_geometric_meshes.urdf:` Defines the box bot whose shape is described using separately created mesh files available in the meshes directory.
- `box_bot_meshes_collisions_inertias.urdf:` Defines the collision tag in the URDF file to enable physics simulation of the robot in any physics simulator, such as Gazebo.
- `box_bot_physical_properties.urdf:` Includes extra tags to define physical properties for the physics simulator (e.g., Gazebo).
- `box_bot_physical_control.urdf:` Includes plugins required to publish and control the joint states of different movable joints for a physics simulator (e.g., Gazebo).
- `box_bot_control_complete_velocity.urdf:` Incorporates plugins and a configuration file needed to control the rotating velocity of the laser sensor present on the robot's head.
- `box_bot_control_complete_sensor.urdf:` Integrates plugins and a configuration file needed to control the rotating velocity and vertical position of the laser sensor present on the robot's head.
- `box_bot_control_complete.urdf:` This is the complete URDF file to simulate the robot in the Gazebo physics simulator along with sensors.

`meshes:` This directory contains the mesh files needed to describe the visual appearance of the robot.

`launch:` This directory contains launch files, a key feature of ROS used to initiate multiple nodes from a single file.

`config:` Contains YAML-based configuration files to configure the parameters of the controllers used to control the different articulated joints in the Gazebo Physics Simulator.

`rviz:` Contains the configuration file to load the pre-saved configuration of RViz.


