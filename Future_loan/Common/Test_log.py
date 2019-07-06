import logging
from Future_loan.Common import Project_Path

from Future_loan.Common.GetConf import GetConf


class TestLog:
    '''日志类'''
    # def __init__(self):
        # self.loger_name=GetConf('LOG','name').get_Str()#从配置文件获取设置的收集器名字
        # self.file_name=GetConf('LOG','filename').get_Str()#从配置文件获取设置的输出文件名字
        # self.loger_Level = GetConf('LOG', 'loger_Level').get_Str()#从配置文件获取设置的收集器级别
        # self.console_Level = GetConf('LOG', 'console_Level').get_Str()#从配置文件获取设置的控制台级别
        # self.file_Level = GetConf('LOG', 'file_Level').get_Str()#从配置文件获取设置的输出文件级别
        # self.formatt = GetConf('LOG', 'formatt').get_Str()#从配置文件获取设置的输出格式

    def get_log(self,level,msg):
        formatt=logging.Formatter('[%(asctime)s]-[%(levelname)s]-[%(filename)s]-[%(funcName)s]-[%(lineno)d]-[日志信息]：%(message)s')
        loger=logging.getLogger('Future_loan')#创建一个名为xxx的日志收集器
        loger.setLevel('INFO')#设置收集器的级别
        streamhd=logging.StreamHandler()#创建一个输出到控制台的输出渠道
        filehd=logging.FileHandler(Project_Path.log_path,encoding='utf-8')#创建一个输出到文件的输出渠道
        streamhd.setLevel('INFO')#设置控制台输出级别
        filehd.setLevel('INFO')#设置文件输出级别
        loger.addHandler(streamhd)#连接控制台
        loger.addHandler(filehd)#连接文件
        streamhd.setFormatter(formatt)#设置控制台输出格式
        filehd.setFormatter(formatt)#设置文件输出格式

        if level == 'DEBUG':
            loger.debug(msg)
        elif level == 'INFO':
            loger.info(msg)
        elif level == 'Warning':
            loger.warning(msg)
        elif level == 'ERROR':
            loger.error(msg)
        else:
            loger.critical(msg)

        loger.removeHandler(filehd)
        loger.removeHandler(streamhd)

    def debug(self,msg):
        '''debug级别的信息'''
        self.get_log('DEBUG',msg)

    def info(self,msg):
        '''info级别的信息'''
        self.get_log('INFO',msg)

    def warning(self,msg):
        '''warning级别的信息'''
        self.get_log('WARNING',msg)

    def error(self,msg):
        '''error级别的信息'''
        self.get_log('ERROR',msg)

    def critical(self,msg):
        '''critical级别的信息'''
        self.get_log('CRITICAL',msg)


if __name__ == '__main__':
    TestLog().info('hello')

