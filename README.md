# gazebo-line-follower

This whole repo was configured for ros1, make this supported for ros2

I changed the package.xml and CMakeLists.txt
to make them compatible for ros2

For ros2, keep ament_cmake instead of catkin for ros1
Same for rclpy for ros2 instead of rospy for ros1

colcon is for

`sudo apt install ros-humble-cv-bridge ros-humble-sensor-msgs ros-humble-geometry-msgs`

```
sudo apt install ros-humble-ros-base
sudo apt install python3-colcon-common-extensions
```

`colcon build`
See dependencies are installed or not first

Install files anmd dependencies from the package.xml file

`sudo apt install python3-rosdep2`
`rosdep update`

`rosdep install --from-paths ./ --ignore-src -r -y`

`source /opt/ros/humble/setup.bash `

`ros2 --version`

`gazebo --version`

`ros2 pkg list`

`python3 -m pip show numpy opencv-python scipy`

if anything missing, install them
ROS2

```
sudo apt update
        sudo apt install ros-humble-gazebo-ros-pkgs ros-humble-cv-bridge ros-humble-sensor-msgs ros-humble-geometry-msgs
```

Python
       ` python3 -m pip install numpy opencv-python scipy`


### Explanation of Files and Their Roles

1. **CMakeLists.txt:**
   * Defines the minimum CMake version and project name.
   * Finds necessary packages ([`ament_cmake`](vscode-file://vscode-app/snap/code/172/usr/share/code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.esm.html), [`rclpy`](vscode-file://vscode-app/snap/code/172/usr/share/code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.esm.html)).
   * Installs Python modules and scripts.
   * Calls `ament_package()` to finalize the package.
2. **package.xml:**
   * Defines the package metadata (name, version, description, maintainer, license).
   * Lists dependencies ([`ament_cmake`](vscode-file://vscode-app/snap/code/172/usr/share/code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.esm.html), [`rclpy`](vscode-file://vscode-app/snap/code/172/usr/share/code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.esm.html)).
   * Specifies build type ([`ament_cmake`](vscode-file://vscode-app/snap/code/172/usr/share/code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.esm.html)).
3. **models/track/model.config:**
   * Defines the model metadata (name, version, author, description).
   * Specifies the SDF file for the model.
4. **urdf/macros.xacro:**
   * Defines macros for different inertial properties (cylinder, box, sphere).
5. **media/materials/scripts/track.material:**
   * Defines the material properties for the track model.
6. **launch/move_robot.launch:**
   * Launches the `move_robot.py` node from the [`lore_competition_bot`](vscode-file://vscode-app/snap/code/172/usr/share/code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.esm.html) package.
7. **models/track/track.sdf:**
   * Defines the SDF model for the track, including collision and visual properties.
8. **urdf/robot.xacro:**
   * Defines the URDF model for the robot, including material properties for wheels.
9. **worlds/353_ros_lab.world:**
   * Defines the Gazebo world, including the track model and camera settings.
10. **launch/robot.launch:**
    * Spawns the robot model in Gazebo using the URDF description.
11. **launch/laun.launch:**
    * Includes other launch files to set up the Gazebo environment and launch the robot and its control nodes.

See `~/node/move_robot.py` for the implementation. First, we grayscale a frame from the robot's camera feed, then apply a binary mask. Finally, the center of mass of the binary mask is computed, and the robot's movement is adjusted.

Visit https://youtu.be/BuUYXrn7hKo for a video.
