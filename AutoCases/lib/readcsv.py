import csv

class ReadCsv():

    def readCsv(self,file):

        datas = []
        c = csv.reader(open(file,"r",encoding="utf-8"))
        print(c)
        for row in c:
            datas.append(row)
        return datas

#
# r=ReadCsv()
# print(r.readCsv("../cfg/homework.csv"))