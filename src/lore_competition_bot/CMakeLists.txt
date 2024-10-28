# Set minimum required CMake version for ROS 2
cmake_minimum_required(VERSION 3.5)
project(lore_competition_bot)

# Find dependencies, in this case, we’re using Python (rclpy) and other ROS 2 libraries
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
# You can add other dependencies here as needed, such as std_msgs, geometry_msgs, etc.

# Include directories, you can uncomment and add specific directories if you have headers
# include_directories(include ${ament_INCLUDE_DIRS})

# Specify Python scripts for installation (move_robot.py script in this case)
install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}/
)

install(
  PROGRAMS
    node/move_robot.py
  DESTINATION lib/${PROJECT_NAME}
)

install(
  DIRECTORY urdf
  DESTINATION share/${PROJECT_NAME}
)

install(
  DIRECTORY media
  DESTINATION share/${PROJECT_NAME}
)

install(
  DIRECTORY models
  DESTINATION share/${PROJECT_NAME}
)

install(
  DIRECTORY worlds
  DESTINATION share/${PROJECT_NAME}
)

# Export package dependencies
ament_package()

