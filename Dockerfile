FROM ros:humble

#set env variables
ENV ROS_DISTRO=humble
ENV DEBIAN_FRONTEND=noninteractive

#Install git and other dependencies
RUN apt-get update && \
    apt-get install -y git python3-pip && \
    rm -rf /var/lib/apt/lists/*

#Create workspace
RUN mkdir -p /ros2_test_ws/src
WORKDIR /ros2_test_ws/src

#Clone the repository
RUN git clone https://github.com/venugopalreddykollan/ros2_test_ws.git

#Set the working directory
WORKDIR /ros2_test_ws

#update ros dep and install dependencies
RUN apt-get update && \
    rosdep update && \
    ./opt/ros/${ROS_DISTRO}/setup.sh && \
    rosdep install --from-paths src --ignore-src -r -y && \
    rm -rf /var/lib/apt/lists/*

#Build the package
RUN . /opt/ros/${ROS_DISTRO}/setup.sh && \
    . install/setup.sh && \
    colcon build --packages-select ros2_test_ws && \
    . install/setup.sh

#Source the setup file
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.sh" >> /root/.bashrc && \
    echo "source /ros2_test_ws/install/setup.sh" >> /root/.bashrc

#!/bin/bash
source /opt/ros/$ROS_DISTRO/setup.bash
source /ros2_test_ws/install/setup.bash
exec "$@"

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]