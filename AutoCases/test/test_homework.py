import unittest, allure

from AutoCases.lib.tool import MyTool
from AutoCases.lib.readcsv import ReadCsv

r = ReadCsv()
datas = r.readCsv("cfg/homework.csv")
print(datas)

mtool = MyTool()

class Test_HomeWork(unittest.TestCase):
    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    @allure.feature("字符串长度")
    def test_strLen(self):
        for i in datas:
            assert mtool.strLen(i[0]) == int(i[1])
            self.assertEqual(mtool.strLen(i[0]),int(i[1]))

    @allure.feature("字符串拼接")
    def test_strAppend(self):
        for i in datas:
            assert mtool.strAppend(i[2],i[3]) == i[4]
            self.assertEqual(mtool.strAppend(i[2],i[3]),i[4])

    @allure.feature("字符串返回长度最长的")
    def test_strMax(self):
        for i in datas:
            assert mtool.strMax(i[5],i[6]) == i[7]
            self.assertEqual(mtool.strMax(i[5],i[6]),i[7])

    @allure.feature("返回该日期的后一天日期")
    def test_dayAdd1(self):
        for i in datas:
            assert mtool.dayAdd1(i[8]) == i[9]
            self.assertEqual(mtool.dayAdd1(i[8]),i[9])

    @allure.feature("分数判断")
    def test_num(self):
        for i in datas:
            assert mtool.num(int(i[10])) == i[11]
            self.assertEqual(mtool.num(int(i[10])),i[11])




