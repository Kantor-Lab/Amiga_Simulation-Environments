import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Path to your URDF file (it should be a processed URDF, not a XACRO file)
    urdf_path = os.path.join(get_package_share_directory('amiga_description'), 'urdf', 'farm-ng.urdf')

    return LaunchDescription([
        # Declare the robot_description argument
        DeclareLaunchArgument(
            'robot_description',
            default_value=urdf_path,
            description='Path to the URDF file or robot description as a string'
        ),
        
        # Start the robot_state_publisher node
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': urdf_path}]
        ),
        
        # Start RViz2 to visualize the robot
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            # arguments=['-d', os.path.join(get_package_share_directory('your_package_name'), 'rviz', 'your_config.rviz')]
        ),
    ])
