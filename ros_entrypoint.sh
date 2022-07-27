#!/usr/bin/env bash
rm -r /catkin_ws/src/ros_kortex/kortex_scripts
ln -s /ros_kortex/kortex_scripts /catkin_ws/src/ros_kortex/kortex_scripts
source /opt/ros/noetic/setup.bash
catkin build
source /catkin_ws/devel/setup.bash
exec "$@"