# IM(Intelligent Manufacture) Robot

这是一个基于人工智能和视觉等多传感器融合的移动抓取机器人项目。

应用领域：

- 无人工厂车间中的作业

- 医院手术室中协作

- 餐饮服务机器人

--------------------------------

    作 者 : 南 山 二 毛

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




------------------------------------

## 1 如何启动

------------------------------------ 
在终端中输入该命令，机器人上发出运行正常提示音，激光雷达开始旋转，RIVZ打开，可以在窗口中看到机器人当前位置和周围获取的深度点云信息。

```
roslaunch thurobot move_grasp_robot.launch
```

------------------------------------

## 2 部分功能测试

------------------------------------

启动机器人后，执行如下命令测试机器人各个功能。

抓取一个茶杯

```
rosservice call /grasp_cup "grasp_cup_num: 2" 
```


抓取一个贴有标签的木快

```
rosservice call /graspcube "grasp_cube_num: 1" 
```

机器人握手

```
rosservice call /shake_hand "shake_num: 3" 
```

在满足容许误差的情况下，控制机器人移动到某个位置

```
rosservice call /nav_dest "{goal_x: -0.053950, goal_y: -1.654546, goal_yaw: -0.001081, distance_tolerance: 0.3, angle_tolerance: 0.1}"
```

------------------------------------

## 3 包含的程序包

------------------------------------

  

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