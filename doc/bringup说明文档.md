
## 1 arduino_serial_node  

src/rosserial/rosserial_arduino/nodes/serial_node.py

1. 设置串口属性，波特率
2. 进入循环，执行SerialClient任务，接收并转发单片机发送的数据

## 2 apply_calib

src/imu_calib/src/accl_calib/apply_calib_node.cpp 
                           --apply_calib.cpp
