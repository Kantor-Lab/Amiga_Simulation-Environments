# Amiga_Simulation-Environments

We perform simulation in Gazebo simulator and utilize [cropcraft tool](https://github.com/Romea/cropcraft) to generate the crop field environments.

## Installation (tested in ros noetic)
### Install the Husky package
#### Add the Clearpath Robotics repository (if not already added):
```
sudo sh -c 'echo "deb http://packages.clearpathrobotics.com/public/$(lsb_release -sc) $(lsb_release -cs) main" > /etc/apt/sources.list.d/clearpath-latest.list'
wget https://packages.clearpathrobotics.com/public.key -O - | sudo apt-key add -
```
#### install Husky package
```
sudo apt update
sudo apt install ros-noetic-husky-desktop
sudo apt install ros-noetic-husky-control
```
### Installation of Gazebo environment package
```
cd ~/catkin_ws/src
git clone https://github.com/Kantor-Lab/Amiga_Simulation-Environments
cd ~/catkin_ws && catkin_make
```
### Installation of Amiga robot URDF description [from branch "ruiji"](https://github.com/Kantor-Lab/amiga_cmu_description/tree/ruiji) 
Follow the instructions in that repo README.md file

## Add Gazebo Models
```
cd ~/.gazebo/models
```
Move every model in [models file](https://github.com/Kantor-Lab/Amiga_Simulation-Environments/tree/main/models) to this path. 

## Launch Simulation
```
cd ~/catkin_ws
source devel/setup.bash
roslaunch iowa_navigation amiga_playen.launch
```
![Screenshot from 2024-05-24 12-25-07](https://github.com/Kantor-Lab/Amiga_Simulation-Environments/assets/78890103/ab9237cd-536f-40e0-8a37-5a73b460de1d)
## Citation 
if you have used this project in your recent works please reference to it:

```bash

@misc{liu2024overcanopyautonomousnavigationcropagnostic,
      title={Towards Over-Canopy Autonomous Navigation: Crop-Agnostic LiDAR-Based Crop-Row Detection in Arable Fields}, 
      author={Ruiji Liu and Francisco Yandun and George Kantor},
      year={2024},
      eprint={2403.17774},
      archivePrefix={arXiv},
      primaryClass={cs.RO},
      url={https://arxiv.org/abs/2403.17774}, 
}

```
