# Amiga Simulation In ROS2-Foxy

## Try it
Download and set up the [ros2 foxy](https://docs.ros.org/en/foxy/Installation.html) first.
### Install Foxy dependent packages
```
sudo apt update
sudo apt install ros-foxy-husky-*
sudo apt install ros-foxy-gazebo-*
sudo apt install ros-foxy-velodyne-*
```
### Install the package
```
mkdir -p amiga_ws/src
cd amiga_ws/src
git clone -b ros2-foxy https://github.com/Kantor-Lab/Amiga_Simulation-Environments
cd ~/amiga_ws && colcon build
```
### Launch the world
```
ros2 launch amiga_gazebo amiga_playen.launch.py
```
### Check
Publish velocity message to /cmd_vel, the Amiga robot should move.
