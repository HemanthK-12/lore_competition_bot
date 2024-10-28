#! /usr/bin/env python3

import rclpy
import numpy as np
import cv2
from scipy.ndimage import center_of_mass
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from rclpy.node import Node

# Constants
TURN_LEFT_SPD = 0.1
TURN_RIGHT_SPD = 0.125
STRAIGHT_SPD = 0.25
ANGULAR_VEL = 1.25
OFFSET_Y = 500

# Global Variable that holds previous CoM
prev = (400, 400)

class MoveRobot(Node):
    def __init__(self):
        super().__init__('move_robot')
        self.bridge = CvBridge()
        self.prev = prev
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscriber = self.create_subscription(Image, '/robot/camera/image_raw', self.callback, 10)
    
    def callback(self, data):
        try:
            # Process grayscale and binary mask
            img_grayscale = self.bridge.imgmsg_to_cv2(data, 'mono8')
            _, img_bin = cv2.threshold(img_grayscale, 128, 1, cv2.THRESH_BINARY_INV)

            # Compute center of mass of bottom 300 rows
            coords_bin = center_of_mass(img_bin[-300:])
            y = coords_bin[0] + OFFSET_Y
            x = coords_bin[1]

            # if CoM is NaN, take previous iteration's value of CoM
            if np.isnan(x) or np.isnan(y):
                x = self.prev[0]
                y = self.prev[1]
            else:
                self.prev = (x, y)

            print((x, y))

            # new Twist object
            move = Twist()

            # turn left or right or go straight
            if x < 350:
                move.linear.x = TURN_LEFT_SPD
                move.angular.z = ANGULAR_VEL
            elif x >= 350 and x <= 450:
                move.linear.x = STRAIGHT_SPD
                move.angular.z = 0
            else:
                move.linear.x = TURN_RIGHT_SPD
                move.angular.z = -1 * ANGULAR_VEL

            self.pub.publish(move)

        except CvBridgeError as e:
            self.get_logger().error(f'CV Bridge Error: {e}')

def main(args=None):
    rclpy.init(args=args)
    move_robot = MoveRobot()
    rclpy.spin(move_robot)
    move_robot.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

