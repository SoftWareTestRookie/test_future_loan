import unittest
from Future_loan.Common.UnitTest import UnitTest
import HTMLTestRunnerNew
from Future_loan.Common import Project_Path
from Future_loan.Common.Recharge import Recharge

suite=unittest.TestSuite()
load=unittest.TestLoader()
suite.addTest(load.loadTestsFromTestCase(UnitTest))
suite.addTest(load.loadTestsFromTestCase(Recharge))
with open(Project_Path.report_path,'wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(file,title='前程贷接口测试报告',tester='雄贰丶')
    runner.run(suite)
