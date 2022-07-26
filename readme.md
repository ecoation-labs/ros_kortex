# To RUN Simulation:

## Terminal 1

        cd ros_kortex
        xhost +local:docker
        docker-compose -f docker-compose-sim.yaml up

## Terminal 2

        cd ros_kortex
        docker exec -it ros_kortex_sim_1 bash

### Works
        roslaunch kortex_examples cartesian_poses_with_notifications_python.launch 
        roslaunch kortex_examples moveit_example.launch
        rosrun kortex_scripts move_with_vias.py
        rosrun kortex_scripts execute_plan_from_file.py
        rosrun kortex_scripts execute_plan_from_file_fixed.py

### Does not Work
        roslaunch kortex_examples waypoint_action_client_python.launch
        roslaunch kortex_examples full_arm_movement_python.launch

# To RUN Real Arm:

### CHANGE THE IP ADRESS IN THE .env FILE! default: 11.11.0.2

## Terminal 1

        cd ros_kortex
        xhost +local:docker
        docker-compose -f docker-compose-kortex.yaml up

## Terminal 2

        cd ros_kortex
        docker exec -it ros_kortex_kortex_1 bash
        roslaunch kortex_examples cartesian_poses_with_notifications_python.launch
        
### Works 
        roslaunch kortex_examples moveit_example.launch
        roslaunch kortex_examples waypoint_action_client_python.launch
        roslaunch kortex_examples full_arm_movement_python.launch

### Does not work
        roslaunch kortex_examples cartesian_poses_with_notifications_python.launch
        rosrun kortex_scripts move_with_vias.py
        rosrun kortex_scripts execute_plan_from_file.py
        rosrun kortex_scripts execute_plan_from_file_fixed.py
