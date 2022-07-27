#!/bin/env python3
import yaml
from genericpath import isfile
from os.path import exists, abspath, realpath
import sys
import rospy
import moveit_commander
import signal
from geometry_msgs.msg import PoseStamped
import geometry_msgs.msg
import yaml
from moveit_msgs.srv import GetPositionFK, GetPositionFKRequest, GetPositionFKResponse
from sensor_msgs.msg import JointState
from moveit_msgs.msg import RobotState, Constraints, PositionIKRequest
from moveit_msgs.srv import GetPositionIK

class KortexPathExecuter:

    def execute_file(self, filename):
        print("request_to_execute: " + filename)
        real_path = realpath(__file__)
        file_path = abspath(real_path+"/../../saved_trajectories/"+filename)
        if not isfile(file_path):
            print("ERROR 3: file does not exist, try again")
        else:
            with open(file_path, 'r') as file_open:
                self.contents =  yaml.unsafe_load(file_open)
            
            for i in range(1):
                for x in range(len(self.contents)):
                    self.group.execute(self.contents[x])

    def goto_start(self):
        group_variable_values = self.group.get_current_joint_values()
        group_variable_values[5] = -1.56442
        group_variable_values[4] = -0.859211
        group_variable_values[1] = -0.316307
        group_variable_values[2] = 2.13135
        group_variable_values[0] = 3.1343
        group_variable_values[3] = -0.0192573
        self.group.set_joint_value_target(group_variable_values)
        plan2 = self.group.plan()
        self.group.go(wait=True)

    def __init__(self):
        rospy.init_node('path_executer_service', anonymous=True)
        self.joint_state_topic = ['joint_states:=/my_gen3/joint_states']
        moveit_commander.roscpp_initialize(self.joint_state_topic)
        self.robot = moveit_commander.RobotCommander(robot_description="/my_gen3/robot_description") 
        self.group = moveit_commander.MoveGroupCommander(robot_description="my_gen3/robot_description", ns="/my_gen3", name="arm")
        self.scene = moveit_commander.PlanningSceneInterface(ns="/my_gen3")
        self.contents = None

    def main(self):
        def signal_handler(sig, frame):
            print('\nYou pressed Ctrl+C!')
            sys.exit(0)
        signal.signal(signal.SIGINT, signal_handler)
        
        self.goto_start()
        self.execute_file("test.yaml")
        

if __name__ == "__main__":
    ex = KortexPathExecuter()
    ex.main()
