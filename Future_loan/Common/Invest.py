import json
import unittest

from ddt import ddt, data

from Future_loan.Common.Do_Excel import Do_Excel
from Future_loan.Common.HttpRequest import HttpRequest
from Future_loan.Common.Test_log import TestLog
from Future_loan.Common.Get_attriibute import Get_attribute
from Future_loan.Common.Mysql import Mysql

param_data=Do_Excel().read_Excel('invest')#读取测试数据

@ddt
class Invest(unittest.TestCase):

    def setUp(self):#每条用例执行之前都会执行一次，进行测试前的初始化工作
        print('开始执行用例测试')


    def tearDown(self):#每条用例执行完毕之后都会执行一次，进行测试后的清除工作
        print('测试执行完毕')


    @data(*param_data)
    def test_login(self,param_data):
        '''执行接口的请求操作，并接收响应的结果，与预期结果进行比对
        把请求的响应结果写回Excel表中去'''
        global COOKIES
        global LOANID
        global MemberID

        # if param_data["Params"].find('loanid')!=-1 and param_data["Params"].find('memberid')!=-1 and param_data["Params"].find('password')!=-1:#判断Params中是否存在loanid和memberid，如果存在，就替换掉


        # else:
        #     params=param_data["Params"]

        if param_data["Sql"] is not None:
            # if param_data["Sql"].find('leaveamount')!=-1:
            leaveamount=Mysql().do_Mysql(eval(param_data["Sql"])["leaveamount"])#投资前查询账户余额
            print('投资前账户余额：',leaveamount[0])
            LOANID = Mysql().do_Mysql(eval(param_data["Sql"])["loanid"])  # 查询竞标id
            # MemberID = Mysql().do_Mysql(eval(param_data["Sql"])["memberid"])  # 查询用户id
            setattr(Get_attribute, 'loanid', str(LOANID[0]))
            # setattr(Get_attribute, 'memberid', str(MemberID[0]))


        params=Get_attribute().replace(param_data["Params"])

        # else:
        #     params=param_data["Params"]

        TestLog().info('-----正在执行第{}条用例->>{}模块-----'.format(param_data["Case_Id"],param_data["Module"]))
        actual = HttpRequest().get_method(param_data["Url"],eval(params),param_data["Method"],cookies=getattr(Get_attribute,'COOKIES'))#执行接口请求，并接收请求响应的结果
        TestLog().info('执行结果为：{}'.format(actual.text))

        if actual.cookies:
            setattr(Get_attribute,'COOKIES',actual.cookies)
        try:
            if param_data["Sql"]!=None:
                invest_amount = eval(params)["amount"]  # 投资金额
                print('投资金额：', invest_amount)
                after_leaveamount=Mysql().do_Mysql(eval(param_data["Sql"])["leaveamount"])#查询投资后账户余额
                print('投资后账户余额：',after_leaveamount[0])

                self.assertEqual(after_leaveamount[0],leaveamount[0]-int(invest_amount))#断言，比对投资后的余额跟投资前的余额减去投资金额的差是否相等
        except Exception as e:
            print('错误是：{}'.format(e))

        try:
            self.assertEqual(json.loads(actual.text)["status"],eval(param_data["ExpectedResult"])["status"])#断言，用请求响应的结果，来跟预期结果做比对
            TestRes='Pass'

        except AssertionError as e:#断言出错，把出错结果抓起来，并打印出来
            TestLog().error('断言错误：{}'.format(e))
            TestRes = 'Failed'
            raise e
        #
        # finally:
        #     Do_Excel().write_excel('invest',param_data["Case_Id"]+1,9,actual.text)#把请求的响应结果写回Excel中
        #     Do_Excel().write_excel('invest',param_data["Case_Id"]+1,10, TestRes)#把比对之后的结论写回Excel中

