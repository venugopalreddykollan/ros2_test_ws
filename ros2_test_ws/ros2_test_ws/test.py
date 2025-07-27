#! /usr/bin/env python3
# interpreter line to tell the interpreter to use python3
import rclpy  # import this every time you want to create a ROS2 node with Python
from rclpy.node import Node 

class MyNode(Node):
    # this class inherits from Node, which is the base class for all ROS2 nodes in Python
    def __init__(self): # constructor method
        # call the constructor of the base class Node
        super().__init__('my_first_node')
        # 'my_first_node' is the name of the node, it should be unique in the ROS2 network
        self.get_logger().info('Hello, ROS2!')
        # log a message to the console
    
def main(args=None):
    # main function to run the node
    rclpy.init(args=args)  # initialize the ROS2 Python client library
    node = MyNode()  # create an instance of MyNode
    rclpy.spin(node)  # keep the node running until it is shut down
    node.destroy_node()  # clean up the node when done
    rclpy.shutdown()  # shut down the ROS2 Python client library

if __name__ == '__main__':
    main()  # call the main function to start the node
# This is a simple ROS2 node written in Python that logs a message when started.