from mysql import connector
from Future_loan.Common.GetConf import GetConf

class Mysql:
    '''操作数据库'''


    def do_Mysql(self,query):
        '''操作数据库'''

        conn_data=GetConf('MYSQL','conn_data').get_Tuple_list()#根据配置文件获取连接数据
        # operation=GetConf('MYSQL','operation').get_Str()
        # conn_data={'host':'47.107.168.87','port':'3306','user':'python','password':'python666','database':'future'}#连接数据
        conn=connector.connect(**conn_data)#创建连接
        cursor=conn.cursor()#获取游标
        operation=query#要执行的操作
        cursor.execute(operation)#执行操作
        res=cursor.fetchone()#获取操作的一行结果
        # res=cursor.fetchall()#获取操作的所有结果

        return res



if __name__ == '__main__':
    res=Mysql().do_Mysql('select Pwd from member where MobilePhone=13652875781')
    print(res[0])
    print(type(res[0]))