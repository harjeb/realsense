# coding=utf-8

import unittest
from test_case import test_image

#构造测试集
suite = unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_image.TestImage))


if __name__=='__main__':
    #执行测试
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)