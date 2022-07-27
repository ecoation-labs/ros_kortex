# Replicate issue 1)
## Terminal 1

        cd ros_kortex
        xhost +local:docker
        docker-compose -f docker-compose-sim.yaml up

## Terminal 2

        cd ros_kortex
        docker exec -it ros_kortex_sim_1 bash
        roslaunch kortex_examples waypoint_action_client_python.launch
        roslaunch kortex_examples full_arm_movement_python.launch

# Replicate issue 2)   
### CHANGE THE IP ADRESS IN THE .env FILE! default: 11.11.0.2

## Terminal 1

        cd ros_kortex
        xhost +local:docker
        docker-compose -f docker-compose-kortex.yaml up

## Terminal 2

        cd ros_kortex
        docker exec -it ros_kortex-modified-noetic-devel-kortex_1 bash
        rosrun kortex_scripts move_with_vias.py
        
# Replicate issue 3)

## Terminal 1

        cd ros_kortex
        xhost +local:docker
        docker-compose -f docker-compose-kortex.yaml up

## Terminal 2

        cd ros_kortex
        docker exec -it ros_kortex-modified-noetic-devel-kortex_1 bash
        rosrun kortex_scripts execute_plan_from_file_fixed.py

# To RUN Simulation:

docker-compose -f docker-compose-sim.yaml up

# To RUN Real Arm:

docker exec -it ros_kortex-modified-noetic-devel-kortex_1 bash