from Future_loan.Common.GetConf import GetConf
import re

class Get_attribute:
    COOKIES=None#HTTP请求cookies
    LOANID=None#标ID
    MemberID=None#用户ID
    Expect_LeaveAmount = None  # 用户账户余额（期望值）

    phone_num=GetConf('PARAMS','mobilephone').get_Str()#用户账号
    password=GetConf('PARAMS','password').get_Str()#用户密码
    invest_amount=GetConf('PARAMS','invest_amount').get_Str()#投资金额
    memberid=GetConf('PARAMS','memberid').get_Str()#用户id
    recharge_amount=GetConf('PARAMS','recharge_amount').get_Str()

    def replace(self,tar):
        '''替换数据'''
        p='#(.*?)#'
        while re.search(p, tar):
            i=re.search(p,tar)
            key=i.group(1)
            value=getattr(Get_attribute,key)
            tar=re.sub(p,value,tar,count=1)
        return tar

if __name__ == '__main__':
    res=Get_attribute().replace('{"mobilephone":"#phone_num#","pwd":"#password#"}')
    print(res)
