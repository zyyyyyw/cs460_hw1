#!/usr/bin/env python
import rospy
from turtlebot_ctrl.msg import TurtleBotState

def callback(data):
		rospy.loginfo(rospy.get_caller_id() + "\nX:{} Y:{} Goal_Reached:{}".format(data.x.data,data.y.data,data.goal_reached.data))

def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("turtlebot_state", TurtleBotState, callback)
	rospy.spin()

if __name__ == '__main__':
     listener()
