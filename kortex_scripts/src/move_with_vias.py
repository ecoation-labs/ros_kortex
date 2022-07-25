#! /bin/python3

import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from os.path import exists, abspath, realpath
import time
import yaml

joint_state_topic = ['joint_states:=/my_gen3/joint_states']
moveit_commander.roscpp_initialize(joint_state_topic)
rospy.init_node('move_group_python', anonymous=True)

robot = moveit_commander.RobotCommander(robot_description="/my_gen3/robot_description")
scene = moveit_commander.PlanningSceneInterface(ns="/my_gen3")    
arm = moveit_commander.MoveGroupCommander(robot_description="my_gen3/robot_description", ns="/my_gen3", name="arm")

pose_1 = geometry_msgs.msg.Pose()
pose_1.position.x = 0.496007026846657
pose_1.position.y = -0.00016859935409193504
pose_1.position.z = 0.429995711
pose_1.orientation.x = 0.5076062594739036
pose_1.orientation.y = 0.5009659209901607
pose_1.orientation.z = 0.4953241975394833
pose_1.orientation.w = 0.496007026846657

pose_2 = geometry_msgs.msg.Pose()
pose_2.position.x = 0.07110348774435855
pose_2.position.y = -0.14485530800688015
pose_2.position.z = 0.670051622
pose_2.orientation.x = 0.930384494684353
pose_2.orientation.y = 0.2971137890065663
pose_2.orientation.z = 0.12039983779679371
pose_2.orientation.w = 0.17779754635992331

pose_3 = geometry_msgs.msg.Pose()
pose_3.position.x = 0.1946163890380395
pose_3.position.y = 0.000398998794612297
pose_3.position.z = 0.704779331
pose_3.orientation.x = 0.6711407976702359
pose_3.orientation.y = 0.6650125572050123
pose_3.orientation.z = 0.2326555377948797
pose_3.orientation.w = 0.23065066484965052

pose_4 = geometry_msgs.msg.Pose()
pose_4.position.x = 0.10111174863135082
pose_4.position.y = 0.19909403411003235
pose_4.position.z = 0.658934979
pose_4.orientation.x = 0.2420943172930874
pose_4.orientation.y = 0.939328076866123
pose_4.orientation.z =  0.2213546219777988
pose_4.orientation.w = 0.10027580403293407

waypoints = [ pose_1, pose_2, pose_3, pose_4, pose_1]
fraction = 0

while fraction<1.0:
    (plan, fraction) = arm.compute_cartesian_path(
    waypoints, 0.01, 0  # waypoints to follow  # eef_step
    )  # jump_threshold
arm.execute(plan, wait=True)

# save plan to file in saved_trajectories directory
plan_list = []
plan_list.append(plan)
file_name = "test2.yaml"
real_path = realpath(__file__)
destination_file_path = abspath(real_path+"/../../saved_trajectories/"+ file_name)
with open(destination_file_path, 'w') as file:
    yaml.dump(plan_list, file, default_flow_style=True)

moveit_commander.roscpp_shutdown()
