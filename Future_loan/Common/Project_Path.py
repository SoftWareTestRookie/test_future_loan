
import os

project_path=os.path.split(os.path.split(__file__)[0])[0]#切割当前文件路径，获取想要的路径
testcase_path=os.path.join(project_path,'Test_Cases','前程贷--接口自动化测试用例.xlsx')#用切割好的路径拼接对应的文件路径，拼接测试数据的路径
conf_path=os.path.join(project_path,'Test_Cases','TestCaseID.conf')#用切割好的路径拼接对应的文件路径，拼接配置文件的路径
log_path=os.path.join(project_path,'Test_Result','test.log')
report_path=os.path.join(project_path,'Test_Result','前程贷接口测试报告.html')
print(report_path)
# project_path_2='C:\\Users\Administrator\PycharmProjects\test rookie\Future_loan\Test_Cases\前程贷--接口自动化测试用例.xlsx'
# if testcase_path==project_path_2:
#     print('pass')
# else:
#     print('failed')