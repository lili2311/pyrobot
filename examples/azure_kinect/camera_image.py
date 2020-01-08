# Copyright (c) Facebook, Inc. and its affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
Example to show how to read images from the camera. 
"""
from __future__ import print_function
from IPython import embed

import sys
ros_path = '/opt/ros/kinetic/lib/python2.7/dist-packages'
if ros_path in sys.path:
    sys.path.remove(ros_path)
    import cv2
sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')

import numpy as np
from pyrobot import Robot

if __name__ == "__main__":
    bot = Robot('azure_kinect')
    rgb, depth = bot.camera.get_rgb_depth()
    actual_depth_values = depth.astype(np.float64) / bot.camera.DepthMapFactor
    cv2.imshow('Color', rgb[:, :, ::-1])
    cv2.imshow('Depth', depth)
    print("Press any Key to Exit")
    cv2.waitKey(0)
