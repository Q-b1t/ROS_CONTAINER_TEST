# you can change the ros distribution to use
ARG IMAGE=ros:melodic 

FROM ${IMAGE} AS ros_img

FROM ros_img AS env_setup

ARG INTERNAL_WORKSPACE=/workspace

WORKDIR ${INTERNAL_WORKSPACE} 

RUN mkdir src

USER root

ENV NVIDIA_VISIBLE_DEVICES \
    ${NVIDIA_VISIBLE_DEVICES:-all}
    
ENV NVIDIA_DRIVER_CAPABILITIES \
    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

SHELL [ "/bin/bash" , "-c" ]

FROM env_setup AS linux_dependencies
# usefull only if you are using c++ nodes and/or gazebo and/or opencv
RUN apt-get update && \
    apt-get install -y make && \
    apt-get install -y g++ && \ 
    apt-get install -y psmisc && \
    apt-get install -y alsa-utils && \
    apt-get install -y python3-pip 

FROM linux_dependencies AS ros_dependencies

# you can change if necesary
ARG ROS_DISTRO=melodic 

RUN apt-get update && \
apt-get install -y ros-${ROS_DISTRO}-ros-control ros-${ROS_DISTRO}-ros-controllers ros-${ROS_DISTRO}-gazebo-msgs && \
apt-get install -y ros-${ROS_DISTRO}-gazebo-ros ros-${ROS_DISTRO}-gazebo-ros-control && \ 
apt-get install -y ros-${ROS_DISTRO}-rviz && \
apt-get install -y ros-${ROS_DISTRO}-turtlesim && \
apt-get install -y ros-${ROS_DISTRO}-rqt && \
apt-get install -y ros-${ROS_DISTRO}-rqt-graph && \
apt-get install -y ros-${ROS_DISTRO}-rqt-common-plugins

 
# add as many dependencies as you need 

#FROM ros_dependencies AS python-libs
# install opencv
#RUN pip3 install scikit-build && \
#    pip3 install opencv-contrib-python==4.6.0.66 && \
#    pip3 install pygame
CMD ["bash"]