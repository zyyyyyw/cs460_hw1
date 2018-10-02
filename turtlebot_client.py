import rospy
from geometry_msgs.msg import Point
from turtlebot_ctrl.srv import TurtleBotControl

def move_to_point(x,y,z):
	try:
		move = rospy.ServiceProxy("turtlebot_control", TurtleBotControl)
		point = Point()
		point.x = x
		point.y = y
		point.z = z
		resp_goal = move(point)
		return resp_goal.success.data
	except rospy.ServiceException, e:
		print "Service call failed: %s"%e

if __name__ == "__main__":
	print move_to_point(-1.0,-1.75,0)