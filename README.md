# ROS_spider_robot
> Spider robot implementation in ROS
![](robot_picture.png)


## Description

robot_description:
```sh
ROS package to visualize urdf model of robot in rVIZ
```
robot_gazebo:
```sh
ROS package to visualize urdf model of robot in Gazebo simulator
```

spider_robot_control:
```sh
ROS package to control joints of robot
```

## Running the project
* put package to src folder of your ros workspace
* write "catkin_make"(in terminal)
* write "source devel/setup.bash" (in terminal)
* write "roslaunch" + "name_of_package" + "name_of_launch_file"(for example "roslaunch robot_gazebo display.launch")
* to see how control works first run model of robot in gazebo

