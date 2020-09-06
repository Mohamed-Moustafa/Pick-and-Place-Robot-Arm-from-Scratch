#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
flag_1= 0
flag_2= 0
flag_3= 0

def robot_move():

    global flag_1,flag_2,flag_3
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('joint_state_publisher', anonymous=True)
    rate = rospy.Rate(20) 
    joints = JointState()
    joints.header = Header()
    joints.header.stamp = rospy.Time.now()
    joints.name = ['joint_1', 'joint_3','joint_4']
    joints.position = [ 0, 0, 0]
    #joints.velocity = []
    #joints.effort = [] 

    while not rospy.is_shutdown():
        joints.header.stamp = rospy.Time.now()
        if  flag_1 == 0 :
            joints.position[0] -= 0.05
            if joints.position[0] < -3.14: 
                flag_1 = 1
        elif  flag_1 == 1  :
            joints.position[0] += 0.05
            if joints.position[0] >= 1.57:
                flag_1 = 0
        if  flag_2 == 0 and flag_1==0 :
            joints.position[1] -= 0.01
            if joints.position[1] <  -0.5:
                flag_2 = 1
        elif flag_2 == 1 and flag_1==1  :
            joints.position[1] += 0.01
            if joints.position[1] > 0:
                flag_2 = 0

        if  flag_3 == 0 and flag_1==0 :
            joints.position[2] -= 0.1
            if joints.position[2] <  -1.55:
                flag_3 = 1
        elif flag_3 == 1 and flag_1==1 :
            joints.position[2] += 0.1
            if joints.position[2] >= 1.55:
                flag_3 = 0


        pub.publish(joints)
        rate.sleep()
	
if __name__ == '__main__':
    try:
        robot_move()
    except rospy.ROSInterruptException:
        pass