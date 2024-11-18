# Amiga Simulation In ROS2-Foxy

## Try it
Download and set up the [ros2 foxy](https://docs.ros.org/en/foxy/Installation.html) first.

### Install the package
```
mkdir -p amiga_ws/src
cd amiga_ws/src
git clone https://github.com/Kantor-Lab/Amiga_Simulation-Environments
cd ~/amiga_ws && colcon build
```
### Launch the world
```
ros2 launch amiga_gazebo amiga_playen.launch.py
```
### Check
Publish velocity message to /cmd_vel, the Amiga robot should move.
