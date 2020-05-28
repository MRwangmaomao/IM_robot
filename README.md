# IM(Intelligent Manufacture) Robot

This robot is combine car with arm.

--------------------------------

    作 者 : 王 培 荣

    版 本 : Ver1.0

    时 间 : 2020.05.20

    如欲合作，可wechat联系：13713917385
---------------------------------

实物图

![IM-robot](doc/img/IM-Robot.png)
![discription1](doc/img/robot_discription1.jpeg)
![discription2](doc/img/robot_discription2.jpeg)

机械图

![IM-robot](doc/img/model_robot.png)

urdf模型和手眼标定

![IM-robot](doc/img/rviz_robot_calib.png)

SLAM建图

![slam](doc/img/slam.gif)

机械臂抓取

![grasp](doc/img/grasp_QR.gif)

rgbd相机，单线雷达和tagslam结合定位导航

![rgbd_grasp1](doc/img/rgbd_grasp1.png)
![rgbd_grasp2](doc/img/rgbd_grasp2.png)
![rgbd_grasp3](doc/img/rgbd_lidar_grasp.png)

## 1 How to work
 
```
roslaunch thurobot move_grasp_robot.launch
```
  


## 2 All package about robot 

定位导航部分包含模块：

[tagslam_robot](https://github.com/MRwangmaomao/tagslam_robot)

[semantic_slam_nav_ros](https://github.com/MRwangmaomao/semantic_slam_nav_ros)

[MYNT-EYE-D-SDK](https://github.com/slightech/MYNT-EYE-D-SDK)

机械臂视部分包含模块：

[aubo_arm_usr](https://github.com/MRwangmaomao/aubo_arm_usr)

[aubo_robot](https://github.com/MRwangmaomao/aubo_robot)

[dh_hand_driver](https://github.com/MRwangmaomao/dh_hand_driver)

[apriltag_ros](https://github.com/MRwangmaomao/apriltag_ros)
  
[easy_handeye](https://github.com/MRwangmaomao/easy_handeye)

[easy_handeye](https://github.com/MRwangmaomao/find_cup_ros)

[visp_hand2eye_calibration](https://github.com/arushk1/visp_hand2eye_calibration)

[iai_kinect2](https://github.com/MRwangmaomao/iai_kinect2)