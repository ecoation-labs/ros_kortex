# To RUN Simulation:

## Terminal 1

        cd ros_kortex
        xhost +local:docker
        docker-compose -f docker-compose-gazebo.yaml up

## Terminal 2

        cd ros_kortex
        docker exec -it ros_kortex_gazebo_1 bash
        rosrun kortex_scripts move_with_vias.py
        rosrun kortex_scripts execute_plan_from_file.py
        rosrun kortex_scripts execute_plan_from_file_fixed.py
        
# To RUN Real Arm:

### If the ip address of the arm is not 11.11.0.2 then change line 23 in the docker-compose-driver.yaml to the correct ip

## Terminal 1

        cd ros_kortex
        xhost +local:docker
        docker-compose -f docker-compose-driver.yaml up

## Terminal 2

        cd ros_kortex
        docker exec -it ros_kortex_gazebo_1 bash
        rosrun kortex_scripts move_with_vias.py
        rosrun kortex_scripts execute_plan_from_file.py
        rosrun kortex_scripts execute_plan_from_file_fixed.py
