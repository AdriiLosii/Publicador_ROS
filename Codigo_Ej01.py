#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
	rospy.init_node('talker')
	pub=rospy.Publisher('gabriel',String,queue_size=10)

	rate=rospy.Rate(4) #4hz
	
	try:
		numero = int(input("Dame un numero: "))
	except ValueError:
		print("Error, ha introducido un valor distinto a int.")
		input("Pulse ENTER para finalizar.")
		exit()
	
	mensaje = "Mensaje enviado %i" % numero

	pub.publish(mensaje)
	rate.sleep()

if __name__=='__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
