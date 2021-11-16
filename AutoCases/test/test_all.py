import unittest,os,pytest
from AutoCases.lib.HTMLTestRunner import HTMLTestRunner
from AutoCases.test.test_homework import Test_HomeWork

class Test_all():
    def Test_Unittest(self):
        suite = unittest.TestSuite()
        suite.addTest(Test_HomeWork("test_strLen"))
        suite.addTest(Test_HomeWork("test_strAppend"))
        suite.addTest(Test_HomeWork("test_strMax"))
        suite.addTest(Test_HomeWork("test_dayAdd1"))
        suite.addTest(Test_HomeWork("test_num"))

        # 使用HTMLTestRunner 生成html 报告
        with open("logs/Test_Unittest_Report.html", "wb") as f:
            HTMLTestRunner(
                stream=f,
                title="Unittest测试报告",
                description="这是描述测试",
                verbosity=2
            ).run(suite)

    def Test_Pytest(self):
        pytest.main(["--html=logs/Test_Pytest_Report.html", "test/test_homework.py"])

    def Test_Allure(self):
        # 生成json类型的测试报告，命令不要写错，是-，不是下划线，否则会报乱码错误
        pytest.main(['--alluredir', 'logs/report/result', 'test/test_homework.py'])
        # 将测试报告转换为html格式，
        split = 'allure ' + 'generate ' + 'logs/report/result ' + '-o ' + 'logs/report/html ' + '--clean'
        # system函数可以将字符串转换成命令在服务器上运行
        os.system(split)

