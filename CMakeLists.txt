cmake_minimum_required(VERSION 3.5)
project(lore_competition_bot)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

# Install Python modules
ament_python_install_package(${PROJECT_NAME})

# Install Python executables
install(PROGRAMS
  scripts/your_script.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()