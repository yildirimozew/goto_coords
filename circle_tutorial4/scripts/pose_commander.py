#!/usr/bin/env python3

import rospy
from circle_tutorial4.srv import send_coords

rospy.init_node("pose_commander")
rospy.wait_for_service("/move_to_goal")

pose_commander = rospy.ServiceProxy("/move_to_goal", send_coords)
x_coord = int(input("Please enter x coord"))
y_coord = int(input("Please enter y coord"))
#msg = send_coords()
#msg.x_coord = x_coord
#msg.y_coord = y_coord
pose_commander.call(x_coord,y_coord)