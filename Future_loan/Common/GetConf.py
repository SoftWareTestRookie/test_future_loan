from configparser import ConfigParser
from Future_loan.Common import Project_Path

class GetConf:

    def __init__(self,section,option):
        self.getconf=ConfigParser()#实例
        self.getconf.read(Project_Path.conf_path,'utf-8')#打开文件
        self.section=section#初始化section
        self.option=option#初始化option

    def get_Str(self):
        '''获取字符串类型的数据'''
        global case_id
        case_id = self.getconf.get(self.section, self.option)
        return case_id

    def get_Int(self):
        '''获取整型数据'''
        case_id=self.getconf.getint(self.section,self.option)
        return case_id

    def get_Float(self):
        '''获取浮点型的数据'''
        case_id=self.getconf.getfloat(self.section,self.option)
        return case_id

    def get_Bool(self):
        '''获取布尔值类型的数据'''
        case_id=self.getconf.getboolean(self.section,self.option)
        return case_id

    def get_Tuple_list(self):
        '''获取元组、列表类型的数据'''
        case_id=self.getconf.get(self.section,self.option)
        return eval(case_id)



if __name__ == '__main__':
    res=GetConf('CASEID','id').get_Tuple_list()
    print(type(res))