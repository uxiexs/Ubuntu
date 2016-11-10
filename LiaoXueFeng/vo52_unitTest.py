#/usr/bin/python3
#coding:utf-8

#*******************************************************************************
# 为了编写单元测试，我们需要引入Python自带的unittest模块，编写mydict_test.py如下：
#*******************************************************************************

import unittest

from vo51_mydict import Dict

class TestDict( unittest.TestCase):
    def test_init(self):
        d = Dict(a = 1, b = 'test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
# class TestDict(unittest.TestCase):
#
#     def setUp(self):
#         print('setUp...')
#
#     def tearDown(self):
#         print('tearDown...')
if __name__ == '__main__':
    unittest.main()

#*******************************************************************************
# 运行单元测试
# 一旦编写好单元测试，我们就可以运行单元测试。最简单的运行方式是在mydict_test.py的最后加上两行代码：
# if __name__ == '__main__':
#     unittest.main()
# 这样就可以把mydict_test.py当做正常的python脚本运行：
# $ python3 mydict_test.py
# 另一种方法是在命令行通过参数-m unittest直接运行单元测试：
# $ python3 -m unittest mydict_test
# 这是推荐的做法，因为这样可以一次批量运行很多单元测试，并且，有很多工具可以自动来运行这些单元测试。
#*******************************************************************************

#*******************************************************************************
# 单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。
# 单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。
# 单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。
# 单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。
#*******************************************************************************
