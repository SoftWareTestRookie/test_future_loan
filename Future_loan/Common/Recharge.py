import json
import unittest

from ddt import ddt, data

from Future_loan.Common.Do_Excel import Do_Excel
from Future_loan.Common.HttpRequest import HttpRequest
from Future_loan.Common.Test_log import TestLog
from Future_loan.Common.Get_attriibute import Get_attribute
from Future_loan.Common.Mysql import Mysql
from Future_loan.Common.GetConf import GetConf

param_data=Do_Excel().read_Excel('recharge')#读取测试数据
mobilephone=GetConf('PARAMS','mobilephone').get_Str()
global MobilePhone
setattr(Get_attribute,'MobilePhone',mobilephone)
# print(getattr(Get_attribute,'MobilePhone'))
# print(param_data)
@ddt
class Recharge(unittest.TestCase):

    def setUp(self):#每条用例执行之前都会执行一次，进行测试前的初始化工作
        print('开始执行用例测试')


    def tearDown(self):#每条用例执行完毕之后都会执行一次，进行测试后的清除工作
        print('测试执行完毕')


    @data(*param_data)
    def test_login(self,param_data):
        '''执行接口的请求操作，并接收响应的结果，与预期结果进行比对
        把请求的响应结果写回Excel表中去'''
        global COOKIES
        global MobilePhone
        global Expect_LeaveAmount
        # setattr(Get_attribute, 'MobilePhone', MobilePhone)  # 利用反射设置值，然后声明为全局变量

        # if param_data["Params"].find('shouji') != -1:
        #     param=param_data["Params"].replace('shouji',getattr(Get_attribute,'MobilePhone'))
        # else:
        #     param=param_data["Params"]
        param=Get_attribute().replace(param_data["Params"])
        if param_data["Sql"] is not None:
            if param_data["Sql"].find('leaveamount')!=-1:  # 充值前查询账户余额
                LeaveAmount = Mysql().do_Mysql(eval(param_data["Sql"])["leaveamount"])  # 如果不为空就取值并传到数据库操作类中，进行对应的数据库操作
            # setattr(Get_attribute, 'LeaveAmount', LeaveAmount)  # 利用反射设置值，然后声明为全局变量
                print('充值前余额：',LeaveAmount)
        TestLog().info('-----正在执行第{}条用例->>{}模块-----'.format(param_data["Case_Id"],param_data["Module"]))
        actual = HttpRequest().get_method(param_data["Url"],eval(param),param_data["Method"],cookies=getattr(Get_attribute,'COOKIES'))#执行接口请求，并接收请求响应的结果
        TestLog().info('执行结果为：{}'.format(actual.text))
        if actual.cookies:
            COOKIES=setattr(Get_attribute,'COOKIES',actual.cookies)
        try:
            if param_data["Sql"] is not None:#判断Sql列的值是否为空
                # MobilePhone = Mysql().do_Mysql(eval(param_data["Sql"])["phone"])#查询用户账号
                if param_data["Sql"].find('leaveamount')!=-1:
                    recharge_amount=eval(param)["amount"]#充值金额
                    print('充值金额：',recharge_amount)
                    after_LeaveAmount = Mysql().do_Mysql(eval(param_data["Sql"])["leaveamount"])#查询充值之后的用户账号余额
                    print('充值后余额：', after_LeaveAmount[0])
                    Expect_LeaveAmount=LeaveAmount[0]+int(recharge_amount)#期望余额
                    setattr(Get_attribute,'Expect_LeaveAmount',Expect_LeaveAmount)#利用反射设置值，然后声明为全局变量
                    print('期望余额：',getattr(Get_attribute,'Expect_LeaveAmount'))

                    self.assertEqual(after_LeaveAmount[0],Expect_LeaveAmount)#断言，期望结果的余额是否和充值之后的实际余额相等
                # if param_data["ExpectedResult"].find('expect_amount')!=-1:
                #     param_data["ExpectedResult"]=param_data["ExpectedResult"].replace('expect_amount',Expect_LeaveAmount)
            self.assertEqual(json.loads(actual.text)["status"],eval(param_data["ExpectedResult"])["status"])#断言，用请求响应的结果，来跟预期结果做比对
            TestRes='Pass'
        except AssertionError as e:#断言出错，把出错结果抓起来，并打印出来
            TestLog().error('断言错误：{}'.format(e))
            TestRes = 'Failed'
#             raise e
#
#         finally:
#             Do_Excel().write_excel('recharge',param_data["Case_Id"]+1,9,actual.text)#把请求的响应结果写回Excel中
#             Do_Excel().write_excel('recharge',param_data["Case_Id"]+1,10, TestRes)#把比对之后的结论写回Excel中

