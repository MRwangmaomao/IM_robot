# IM(Intelligent Manufacture) Robot

This robot is combine car with arm.

![IM-robot](doc/img/IM-Robot.png)

![grasp](doc/img/grasp_QR.gif)
## 1 car Simulation

### 1.1 navigation
navigation and avoid obstacles by ros move base
```
roslaunch thurobot thurobot_laser_nav_gazabo.launch
roslaunch thurobot nav_cloister_demo_sim.launch
roslaunch thurobot thurobot_teleop.launch
```
 
### 1.2 exploring slam
```
roslaunch thurobot thurobot_laser_nav_gazabo.launch
roslaunch thurobot exploring_slam_demo.launch
rosrun thurobot exploring_slam_sim.py 
```

## 2 car testing in robot


```
roslaunch thurobot bringup.launch 
```

You need to change linear_scale parameter in bringup.launch file.(I set as 1.0)


## 3 arm simulation

```
roslaunch auboi5_moveit_config demo.launch sim:=true
```

Then select "Interact" and move the end-effector to a new goal.

In "Motion Planning" -> "Plan and Execute" to send trajectory to the sim robot

Exit RViz and Ctrl-C the demo.launch window


## 4 bringup.launch
```
roslaunch thurobot bringup.launch
```


## 4 remote move by keyboard
```
roslaunch teleop_twist_keyboard thurobot_teleop.py
```

## 6 remote establish map
```
roslaunch thurobot lidar_slam.launch
```

## 7 navigation by map
```
roslaunch thurobot navigate_multi.launch
```

## 8 automatic map
```
roslaunch thurobot auto_slam.launch
```

