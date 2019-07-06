import requests

from Future_loan.Common.Test_log import TestLog


class HttpRequest:
    '''HTTP请求类，根据请求方法来决定发起的HTTP请求，是GET还是POST方法
    url：接口地址，发送请求的接口地址
    param：请求参数，以字典的形式随接口发送的请求参数
    method：请求方法,GET、POST，HTTP的请求方式'''



    # def __init__(self,url,param):
    #     '''初始化请求地址、参数'''
    #     self.url=url
    #     self.param=param
        # self.cookies=cookies

    def get_method(self,url,param,method_name,cookies):
        '''根据传入的方法名来执行对应的请求方法'''
        log=TestLog()#创建日志类实例
        if method_name.lower() == 'get':#如果传入的方法名为'get'，则调用get方法
            try:
               res=requests.get(url,params=param,cookies=cookies)
            except Exception as e:
                log.error('请求出错了：{}'.format(e))

        elif method_name.lower() =='post':#如果传入的方法名为'post'，则调用get方法
            try:
                res=requests.post(url,data=param,cookies=cookies)
            except Exception as e:
                log.error('请求出错：{}'.format(e))
        else:
            log.error('不支持该种请求方式！')
            res=None
        return res#返回请求结果

if __name__ == '__main__':
    res=HttpRequest({"mobilephone":"13652875782","pwd":"chen1"}).get_method('get').text
    print(res)