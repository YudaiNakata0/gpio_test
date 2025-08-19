#!/bin/bash

ROS_MASTER_IP="192.168.1.57"
THIS_PC_IP="192.168.1.226"
#SCRIPT_PATH="/home/khadas/ros/jsk_aerial_robot_ws/src/jsk_aerial_robot/robots/gimbalrotor/gpio_input_read.py"
SCRIPT_PATH="/home/khadas/gpio_test/gpio_input_read.py"
WORKSPACE_SETUP="/home/khadas/ros/jsk_aerial_robot_ws/devel/setup.bash"


sudo bash -c "
  source /opt/ros/noetic/setup.bash &&
  source $WORKSPACE_SETUP &&
  export ROS_MASTER_URI=http://$ROS_MASTER_IP:11311 &&
  export ROS_HOSTNAME=$THIS_PC_IP &&
  python3 $SCRIPT_PATH
"
