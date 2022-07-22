FROM osrf/ros:noetic-desktop-full

# get python deps
RUN apt-get update && apt-get -y install python3-pip
RUN pip install \
    conan 
ENV CONAN_REVISIONS_ENABLED=1
# get ros deps
RUN apt-get update && apt-get -y install \
    ros-noetic-moveit && apt-get -y install ros-noetic-moveit-kinematics \
    ros-noetic-xacro \
    ros-noetic-ros-controllers ros-noetic-ros-control \
    ros-noetic-catkin python3-catkin-tools \
    git

# set nvidia varables
# ENV NVIDIA_VISIBLE_DEVICES \
#     ${NVIDIA_VISIBLE_DEVICES:-all}
# ENV NVIDIA_DRIVER_CAPABILITIES \
#     ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

# configure and build enviroment
SHELL ["/bin/bash", "-c"]
ENV DEBIAN_FRONTEND=noninteractive
RUN mkdir -p /catkin_ws/src/ros_kortex

# copy packages
COPY . ./catkin_ws/src/ros_kortex

# build
WORKDIR /catkin_ws
RUN /bin/bash -c "source /opt/ros/noetic/setup.bash \
        && catkin build"
RUN echo 'source "/opt/ros/noetic/setup.bash"' >> ~/.bashrc \
    && echo 'source "/catkin_ws/devel/setup.bash"' >> ~/.bashrc

# execute
ADD ros_entrypoint.sh /usr/bin/ros_entrypoint
RUN chmod +x /usr/bin/ros_entrypoint

ENTRYPOINT [ "ros_entrypoint" ]