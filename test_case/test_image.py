# coding=utf-8

import unittest
import pyrealsense2 as rs
import numpy as np

class TestImage(unittest.TestCase):
    """Test image data"""

    def setUp(self):
        self.pipeline = rs.pipeline()
        profile = self.pipeline.start()

    def tearDown(self):
        self.pipeline.stop()

    def test_getImageData(self):
        """get image data """
        for i in range(0, 1):
            frames = self.pipeline.wait_for_frames()
            color_frame = frames.get_color_frame()
            color_image = np.asanyarray(color_frame.get_data())
            self.assertGreater(color_image.size,0,msg='image data check failed')
            # for f in frames:
            #     print(f.profile)

    def test_getDepthData(self):
        """get depth data """
        for i in range(0, 1):
            frames = self.pipeline.wait_for_frames()
            depth_frame = frames.get_depth_frame()
            depth_image = np.asanyarray(depth_frame.get_data())
            self.assertGreater(depth_image.size,0,msg='depth data check failed')

    def test_getDeviceInfo(self):
        """get device info """
        device = rs


if __name__ == "__main__":
    unittest.main()