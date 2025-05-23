#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


def callback(msg):
    move = Twist()
    vector = msg.ranges
    print("Right: {}, Front: {}, Left: {}".format(vector[359], vector[179], vector[0]))
    if vector[179] > 1:
       move.linear.x = 0.5

    if vector[179] < 1:
        move.angular.z = 0.5

    if vector[359] < 1:
        move.angular.z = 0.5

    if vector[0] < 1:
        move.angular.z = -0.5

    pub.publish(move)


rospy.init_node("angles_node", anonymous = True)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()
