# Amiga_Simulation-Environments

We perform simulation in Gazebo simulator and utilize [cropcraft tool](https://github.com/Romea/cropcraft) to generate the crop field environments.

## Installation
### Installation of Gazebo environment package
```
cd ~/catkin_ws/src
git clone https://github.com/Kantor-Lab/Amiga_Simulation-Environments
cd ~/catkin_ws && catkin_make
```
### [Installation of Amiga robot URDF description from branch "ruiji"](https://github.com/Kantor-Lab/amiga_cmu_description/tree/ruiji) 
Follow the instructions in README.md file

## Add Gazebo Models
```
cd ~/.gazebo/models
```
Move every model in [models file](https://github.com/Kantor-Lab/Amiga_Simulation-Environments/tree/main/models) to this path. 
