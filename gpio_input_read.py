#!/usr/bin/env python3
import rospy
import time
import os
from std_msgs.msg import Empty, String

def setup_gpio(input_num, output_num, path):
    # GPIOエクスポート
    if not os.path.exists(f"{path}/gpio{input_num}"):
        with open(f"{path}/export", "w") as f:
            f.write(str(input_num))

    if not os.path.exists(f"{path}/gpio{output_num}"):
        with open(f"{path}/export", "w") as f:
            f.write(str(output_num))

    # 入力モード設定
    with open(f"{path}/gpio{input_num}/direction", "w") as f:
        f.write("in")

    # 出力モード設定
    with open(f"{path}/gpio{output_num}/direction", "w") as f:
        f.write("out")

def input_read(input_num, path):
    with open(f"{path}/gpio{input_num}/value", "r") as f:
        value = f.read().strip()
        return int(value)

def output_on(output_num, path):
    with open(f"{path}/gpio{output_num}/value", "w") as f:
        f.write("1")

def output_off(output_num, path):
    with open(f"{path}/gpio{output_num}/value", "w") as f:
        f.write("0")

def publish(pub):
    msg = "touched"
    pub.publish(msg)

if __name__ == "__main__":
    input_num = 491
    output_num = 501
    path = "/sys/class/gpio"
    print("reading sensor value...")
    rospy.init_node("test_node")
    pub = rospy.Publisher("/read_sensor", String, queue_size=10)
    setup_gpio(input_num, output_num, path)
    try:
        while not rospy.is_shutdown():
            value = input_read(input_num, path)
            if value == 1:
                rospy.loginfo("GPIO %s input value: 1", input_num)
                output_on(output_num, path)
                publish(pub)
                time.sleep(0.5)
                output_off(output_num, path)
                time.sleep(5.0)
            else:
                time.sleep(0.5) 
            
    except KeyboardInterrupt:
        print("Exiting...")
