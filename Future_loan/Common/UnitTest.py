import json
import unittest

from ddt import ddt, data

from Future_loan.Common.Do_Excel import Do_Excel
from Future_loan.Common.HttpRequest import HttpRequest
from Future_loan.Common.Test_log import TestLog


@ddt
class UnitTest(unittest.TestCase):


    param_data=Do_Excel().read_Excel('TestCase')#读取测试数据
    COOKIES=None
    global COOKIES


    def setUp(self):#每条用例执行之前都会执行一次，进行测试前的初始化工作
        print('开始执行用例测试')


    def tearDown(self):#每条用例执行完毕之后都会执行一次，进行测试后的清除工作
        print('测试执行完毕')


    @data(*param_data)
    def test_login(self,param_data):
        '''执行接口的请求操作，并接收响应的结果，与预期结果进行比对
        把请求的响应结果写回Excel表中去'''
        global COOKIES
        TestLog().info('-----正在执行第{}条用例->>{}模块-----'.format(param_data["Case_Id"],param_data["Module"]))
        actual = HttpRequest().get_method(param_data["Url"],eval(param_data["Params"]),param_data["Method"],cookies=COOKIES)#执行接口请求，并接收请求响应的结果
        TestLog().info('执行结果为：{}'.format(actual.json()))
        if actual.cookies:
            COOKIES=actual.cookies
        try:
            self.assertEqual(json.loads(actual.text)["status"],eval(param_data["ExpectedResult"])["status"])#断言，用请求响应的结果，来跟预期结果做比对
            TestRes='Pass'
            # font.colour_index=2

        except AssertionError as e:#断言出错，把出错结果抓起来，并打印出来
            TestLog().error('断言错误：{}'.format(e))
            TestRes = 'Failed'
            raise e

        finally:
            Do_Excel().write_excel('TestCase',param_data["Case_Id"]+1,9,actual.text)#把请求的响应结果写回Excel中
            Do_Excel().write_excel('TestCase',param_data["Case_Id"]+1,10, TestRes)#把比对之后的结论写回Excel中

