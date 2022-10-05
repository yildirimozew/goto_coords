#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import sqrt, pow
from circle_tutorial4.srv import send_coords

rospy.init_node("pose_publisher", anonymous = True)
rate = rospy.Rate(1)
pose = Pose()
rospy.loginfo("%d %d", pose.x, pose.y)

def update_pose(data):
  global pose
  rospy.loginfo("%d %d", data.x, data.y)
  pose = data

def euclidean_distance(goal_pose):
  return sqrt(pow((goal_pose.x_coord - pose.x), 2) + pow((goal_pose.y_coord - pose.y), 2))

def goto_place(goal_pose):
  tolerance = 0.01
  vel = Twist()
  while euclidean_distance(goal_pose) >= tolerance:
    vel.linear.x, vel.linear.y, vel.linear.z = 0.5 * (goal_pose.x_coord - pose.x), 0.5 * (goal_pose.y_coord - pose.y), 0
    vel.angular.x, vel.angular.y, vel.angular.z = 0, 0, 0
    publisher.publish(vel)
    rate.sleep()
  return True

pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, update_pose)
publisher = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=100)
service = rospy.Service("/move_to_goal", send_coords, goto_place)

rospy.spin()

