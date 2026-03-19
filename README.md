<div align="center">
  <h1>🤖 ROS 2 Wall Follower</h1>
  <p><b>Autonomous Navigation & Obstacle Avoidance using TurtleBot3</b></p>

  <img src="https://img.shields.io/badge/ROS2-Humble-blue?style=for-the-badge&logo=ros" alt="ROS2 Humble">
  <img src="https://img.shields.io/badge/Simulator-Gazebo-orange?style=for-the-badge" alt="Gazebo">
  <img src="https://img.shields.io/badge/Robot-TurtleBot3-red?style=for-the-badge" alt="TurtleBot3">
</div>

---

## 📝 Project Overview
This project implements a reactive **Wall Following** behavior for a differential drive robot (TurtleBot3 Burger) in a simulated environment. By processing real-time LIDAR data, the robot maintains a consistent distance from obstacles while navigating through a maze-like environment.

### 🧠 Logic Architecture
The robot operates on a **Sense-Think-Act** cycle:
1.  **Sense:** Subscribes to the `sensor_msgs/msg/LaserScan` topic.
2.  **Think:** Segments the 360° LIDAR data into five strategic zones (Front, Front-Left, Left, Front-Right, Right).
3.  **Act:** Calculates linear and angular velocities, publishing them to the `geometry_msgs/msg/Twist` topic.

---

## ⚙️ Key Features
* ✅ **Real-time LIDAR Processing:** High-frequency scanning to prevent collisions.
* ✅ **Reactive Navigation:** Adjusts steering based on proximity to the wall (Proportional control logic).
* ✅ **Simulation-Ready:** Pre-configured for **Gazebo** physics and **RViz2** visualization.
* ✅ **Modular Code:** Easy to swap between `Burger` and `Waffle` models.

---

## 🛠️ Requirements & Setup
Ensure you have a working **ROS 2 Humble** installation on Ubuntu 22.04.

```bash
sudo apt update
sudo apt install ros-humble-turtlebot3-gazebo ros-humble-turtlebot3-msgs ros-humble-turtlebot3-navigation2
# Set your robot model
export TURTLEBOT3_MODEL=burger
# Launch the world
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
# In a new terminal
ros2 run maze_solver_bot wall_follower
```
---

## 🔮 Future Roadmap
The next development phases for this project will focus on transitioning from reactive behaviors to full autonomy:

* 🗺️ **SLAM Integration:** Implementing `slam_toolbox` to generate real-time 2D occupancy grids while the robot performs wall-following.
* 📍 **Nav2 Implementation:** Integrating the **Navigation 2 Stack** to allow the robot to plan global paths around the maze rather than just reacting to walls.
* 📈 **PID Control Optimization:** Refining the steering logic with a tuned PID controller to eliminate "wobble" and ensure smoother parallel-to-wall movement.
* 🎥 **Vision-Based Navigation:** Adding a camera sensor to perform **Line Following** or **Object Recognition** using OpenCV alongside the LIDAR data.

---

<div align="center">
  <p><i>"Engineering is not just about moving a robot; it's about mastering the logic of autonomy."</i></p>
  <sub>Developed by <b>Omeyimi</b> | Robotics Portfolio 2026</sub>
</div>
