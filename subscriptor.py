#!/usr/bin/env python
# license removed for brevity

import rospy
from std_msgs.msg import String

def callback(msg):
	rospy.loginfo("mensaje recibido:%s",msg.data)

def memory_subscriber():
	rospy.init_node("suscriptor_basico_gabriel",anonymous=True)
	#el primer argumento es el nombre topic al que queremos suscribirmos
	#el segundo argumento es el tipo de mensaje,
	rospy.Subscriber('chatter',String,callback)
	rospy.spin()

if __name__=="__main__":
	try:
		memory_subscriber()
	except rospy.ROSInterruptExceptiopn:
		pass	
