# robotics-description & video to my robot

my robot is simple pick & place robot arm mechanism

links:
1) base_link 	: which is the blue box near the ground
2) link_1 		: which is the white cylinder
3) link_2		: black cuboid
4) link_3		: the blue cylinder
5) link_4		: the white box

joints:
1) joint_1		: revolute joint between base_link & link_1
2) joint_2		: fixed joint between link_1 & link_2
3) joint_3 		: prismatic joint between link_2 & link_3
4) joint_4		: continuous joint between link_3 & link_4
			          (assemble wrist joint ) for end effector

the python code (robot_move.py) is to make the three movable joints to work simultensouly to a specific poisition , after this position is reached it get back
to it`s original position


link to the video of the robot :
https://drive.google.com/file/d/13JXFBWBeMeXjQIq1tefdk6CKdTSVdG9V/view?usp=drivesdk
