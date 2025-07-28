#!/bin/bash
set -e

source "/opt/ros/$ROS_DISTRO/setup.bash"
source "/ros2_test_ws/install/setup.bash"

exec "$@"