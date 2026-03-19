import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class WallFollower(Node):
    def __init__(self):
        super().__init__('wall_follower')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)
        self.get_logger().info("Wall Follower Node Started")

    def scan_callback(self, msg):
        # Divide ranges into zones
        front = min(min(msg.ranges[0:10] + msg.ranges[-10:]), 10.0)
        left = min(min(msg.ranges[80:100]), 10.0)
        right = min(min(msg.ranges[260:280]), 10.0)

        cmd = Twist()

        # Wall-following rule: avoid front collision, keep space
        if front > 0.5:
            cmd.linear.x = 0.2
            if left < 0.3:
                cmd.angular.z = -0.3  # too close to wall on left, turn right slightly
            elif right < 0.3:
                cmd.angular.z = 0.3  # too close to wall on right, turn left slightly
            else:
                cmd.angular.z = 0.0
        else:
            cmd.linear.x = 0.0
            cmd.angular.z = 0.5  # turn if obstacle ahead

        self.publisher_.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = WallFollower()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
