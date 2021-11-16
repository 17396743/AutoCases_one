import time


# 使用pytest写一遍
class StringTool:

    # 应该断言失败
    # 将小写字符串转为大写，你猜猜我有没有帮你转
    def strConvert(self, str=""):
        return str

    # 断言成功
    # 将每个单词首字母转为大写，你猜这个方法能不能完成
    def strConvert2(self, str=""):
        return str.title()

    # 断言失败，index方法如果不存在该字符串，会报错
    # 返回str2在str1中的索引
    def strConvert3(self, str1="", str2=""):
        return str1.index(str2)

    # 断言失败，因为有复姓
    # 传入你的姓名，返回你的姓氏,第一个测试数据必须是你的名字（用意你知道的）
    def strConvert4(self, str=""):
        return str[0]


class DateTool:
    # 1s = 1000ms
    # 传一个时间的毫秒值，将其转换为字符串格式的，如 1636951680481  转换为  2021-11-15 12:48:00
    def time2String(self, date):
        oldDate = time.localtime(int(date) / 1000)

        return time.strftime('%Y-%m-%d %H:%M:%S', oldDate)

    # 传一个日期字符串，将其转换为毫秒值,要求时间格式为：2021-11-15 12:48:00
    # 这个断言应该失败，因为返回的是秒值，不是毫秒值，正确的应该是这个结果再乘以1000
    def str2Time(self, str):
        return time.mktime(time.strptime(str, '%Y-%m-%d %H:%M:%S'))

    # 给定一个年份，判断是否为闰年，自己百度闰年规则
    def yearIsRun(self, year):
        if year % 4 == 0:
            return "闰年"
        else:
            return "平年"


class MyTool():

    # 给定一个字符串，返回字符串长度
    def strLen(self, str):
        return len(str) - 1

    # 给定两个字符串，讲它们拼接到一起，长度在前面，短的在后面，中间使用-隔开
    def strAppend(self, str1, str2):
        le1 = len(str1)
        le2 = len(str2)
        if le1 > le2:
            return str1 + "-" + str2
        else:
            return str2 + "-" + str1

    # 给定两个字符串， 返回长度长的那个
    def strMax(self, str1, str2):
        return str1

    # 给定一个字符串格式的日期，返回该日期的后一天日期，如给定 2021-11-15，返回2021-11-16
    def dayAdd1(self, str):
        last = time.mktime(time.strptime(str, '%Y-%m-%d'))
        now = time.localtime(last + 24 * 3600)
        return time.strftime("%Y-%m-%d", now)

    # 给定一个分数，如果小于0或者大于100，返回分数异常，大于80，返回优秀，大于60且小于80，返回及格，小于60返回不及格
    def num(self, num):
        if num > 100 or num < 0:
            return "分数异常"
        elif num > 80:
            return "优秀"
        elif num > 60:
            return "不及格"
        else:
            return "渣渣"


print(MyTool().dayAdd1("2021-12-31"))

print(DateTool().str2Time("2021-10-1 00:00:00"))

# time.time()*1000 : 获取当前时间的毫秒值
currentTime = time.time() * 1000
print(currentTime)
print(DateTool().time2String("1636951680481"))
