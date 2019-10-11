import pymysql
import numpy as np
import matplotlib.pyplot as plt
import DataAccessLayer
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime
from socket import *
from time import ctime

class BusinessProcess:
    def __init__(self,type,queries,chartType):
        if(type==1): # 图表的查询和显示
            self.queries=queries
            self.chartType=chartType
            print(self.queries+self.chartType)
            self.Connect()
        elif(type==2): # 指数的查询和显示
            self.date1=queries
            self.date2=chartType
            print("test"+self.date1+self.date2)
            self.ShanghaiCompositeIndex()
        elif(type==3):
            self.date=queries
            self.search=chartType
            print(self.date+self.search)
            self.Searchsome()

    def Searchsome(self):
        db = DataAccessLayer.connect()
        cursor = db.cursor()
        cursor.execute(DataAccessLayer.sqlDate)
        Date = cursor.fetchall()
        self.floatData = []
        for rowData in Date:
            temp = rowData[0].strftime('%Y-%m-%d')
            temp = temp[0:4] + temp[5:7] + temp[8:10]
            self.floatData.append(float(temp))

        floatdate = float(self.date)
        num1=0
        pos1=0
        pos2=0
        for i in self.floatData:
            if(floatdate==i):
                pos1=num1
                print("找到日期:"+str(pos1))
                break
            num1+=1

        sqlTotalMarketValue = "SELECT " + self.search +" FROM StockMarket"  # 总市值
        cursor.execute(sqlTotalMarketValue)
        self.Value = cursor.fetchall()

        for j in self.Value:
            if(num1==pos1):
                val=j
                print("找到"+self.search+":" + str(val))
                break
            num1+=1
        db.close()
        self.searchres=val[0]

    def getSearchRes(self):
        return self.searchres


    def ShanghaiCompositeIndex(self):
        db = DataAccessLayer.connect()
        cursor = db.cursor()
        sqlDate = DataAccessLayer.sqlDate
        # 日期
        cursor.execute(sqlDate)
        Date = cursor.fetchall()
        self.floatData = []
        for rowData in Date:
            temp = rowData[0].strftime('%Y-%m-%d')
            temp = temp[0:4] + temp[5:7] + temp[8:10]
            self.floatData.append(float(temp))


        floatdate1 = float(self.date1)
        floatdate2 = float(self.date2)
        num1=0
        num2=0
        pos1=0
        pos2=0
        for i in self.floatData:
            if(floatdate1==i):
                pos1=num1
                print("找到日期1:"+str(pos1))
            if(floatdate2==i):
                pos2=num2
                print("找到日期2:"+str(pos2))
            num1+=1
            num2+=1

        sqlTotalMarketValue = DataAccessLayer.sqlTotalMarketValue
        cursor.execute(sqlTotalMarketValue)
        self.Value = cursor.fetchall()
        num1=0
        num2=0

        for j in self.Value:
            if(num1==pos1):
                val1=j
                print("找到市值1:" + str(val1))
            if(num2==pos2):
                val2=j
                print("找到市值2:" + str(val2))
            num1+=1
            num2+=1
        db.close()
        self.result=((val1[0])/(val2[0]))*100

    def getShanghaiCompositeIndex(self):
        return self.result

    def Connect(self):
        # 链接数据库
        # db = pymysql.connect("localhost", "root", "08110811", "testDB")
        db = DataAccessLayer.connect()
        # 读取数据
        cursor = db.cursor()
        sqlDate = DataAccessLayer.sqlDate

        # 日期
        cursor.execute(sqlDate)
        Date = cursor.fetchall()
        self.floatData = []
        for rowData in Date:
            # print(rowData[0])
            temp = rowData[0].strftime('%Y-%m-%d')
            temp = temp[0:4] + temp[5:7] + temp[8:10]
            self.floatData.append(float(temp))

        if(self.queries == "前收盘价和开盘价"):
            sqlBeforeClosing = DataAccessLayer.sqlBeforeClosing  # 前收盘价
            sqlTheOpening = DataAccessLayer.sqlTheOpening  # 开盘价
            # 前收盘价
            cursor.execute(sqlBeforeClosing)
            self.BeforeClosing = cursor.fetchall()
            # 开盘价
            cursor.execute(sqlTheOpening)
            self.TheOpening = cursor.fetchall()
        elif(self.queries == "最高价和最低价"):
            sqlTheHighest = DataAccessLayer.sqlTheHighest  # 最高价
            sqlTheLowest = DataAccessLayer.sqlTheLowest  # 最低价
            # 最高价
            cursor.execute(sqlTheHighest)
            self.Highest = cursor.fetchall()
            # 最低价
            cursor.execute(sqlTheLowest)
            self.Lowest = cursor.fetchall()
        elif(self.queries == "均价"):
            sqlAveragePrice = DataAccessLayer.sqlAveragePrice  # 均价
            cursor.execute(sqlAveragePrice)
            self.Average = cursor.fetchall()
        elif(self.queries == "换手率"):
            sqlTurnoverRate = DataAccessLayer.sqlTurnoverRate  # 换手率
            cursor.execute(sqlTurnoverRate)
            self.TurnoverRate = cursor.fetchall()

        db.close()
        # sqlLowestClosing = "SELECT 最低收盘价 FROM StockMarket"  # 最低收盘价
        # sqlVolume  = "SELECT 成交量 FROM StockMarket"  # 成交量
        # sqlClinchADealAmount = "SELECT 成交金额 FROM StockMarket"  # 成交金额
        # sqlRiseAndFall = "SELECT 涨跌 FROM StockMarket"  # 涨跌
        # sqlApplies = "SELECT 涨跌幅 FROM StockMarket"  # 涨跌幅
        # sqlAveragePrice = "SELECT 均价 FROM StockMarket"  # 均价
        # sqlAshareCurrentMarketValue = "SELECT A股流通市值 FROM StockMarket"  # A股流通市值
        # sqlBsharesOutstandingMarketValue = "SELECT B股流通市值 FROM StockMarket"  # B股流通市值
        # sqlTotalMarketValue = "SELECT 总市值 FROM StockMarket"  # 总市值
        # sqlAshareCirculatingCapitalStock = "SELECT A股流通股本 FROM StockMarket"  #  A股流通股本
        # sqlBsharesCirculatingCapitalStock = "SELECT B股流通股本 FROM StockMarket"  # B股流通股本
        # sqlTotalEquity = "SELECT 总股本 FROM StockMarket"  # 总股本
        # sqlPeRatio = "SELECT 市盈率 FROM StockMarket"  # 市盈率
        # sqlPriceToBook = "SELECT 市净率 FROM StockMarket"  # 市净率
        # sqlPriceToSalesRatio = "SELECT 市销率 FROM StockMarket"  # 市销率
        # TheCityRate = "SELECT 市现率 FROM StockMarket"  # 市现率

    def CreatMatplotlib(self):
        f = plt.figure(figsize=(6, 6))
        a = f.add_subplot(1,1,1) # 添加子图:1行1列第1个
        if(self.queries=="前收盘价和开盘价"):
            plt.title("Before closing and The Opening")
            if(self.chartType=="折线图"):
                plt.plot(self.floatData, self.BeforeClosing, label='Before closing')
                plt.plot(self.floatData, self.TheOpening, label='The Opening')
            elif(self.chartType=="散点图"):
                plt.plot(self.floatData, self.BeforeClosing,'g^')
                plt.plot(self.floatData, self.TheOpening,'r--')
            plt.xlabel('Data(Year)')
            plt.ylabel('Price(Yuan)')
            xTicks = np.arange(19990000, 20170000, 20000)
            plt.xticks(xTicks)
            plt.legend()
        elif(self.queries=="最高价和最低价"):
            plt.title("The Highest and The Lowest")
            if(self.chartType=="折线图"):
                plt.plot(self.floatData, self.Highest, label='The Highest')
                plt.plot(self.floatData, self.Lowest, label='The Lowest')
            elif (self.chartType == "散点图"):
                plt.plot(self.floatData, self.Highest,'g^')
                plt.plot(self.floatData, self.Lowest,'r--')
            plt.xlabel('Data(Year)')
            plt.ylabel('Price(Yuan)')
            xTicks = np.arange(19990000, 20170000, 20000)
            plt.xticks(xTicks)
            plt.legend()
        elif(self.queries=="均价"):
            plt.title("The Average Price")
            if(self.chartType=="折线图"):
                plt.plot(self.floatData, self.Average)
            elif (self.chartType == "散点图"):
                plt.plot(self.floatData, self.Average,'g^')
            plt.xlabel('Data(Year)')
            plt.ylabel('Price(Yuan)')
            xTicks = np.arange(19990000, 20170000, 20000)
            plt.xticks(xTicks)
            # plt.legend()
        elif(self.queries=="换手率"):
            plt.title("The Turnover Rate")
            if(self.chartType=="折线图"):
                plt.plot(self.floatData, self.TurnoverRate)
            elif (self.chartType == "散点图"):
                plt.plot(self.floatData, self.TurnoverRate,'g^')
            plt.xlabel('Data(Year)')
            plt.ylabel('Rete(%)')
            xTicks = np.arange(19990000, 20170000, 20000)
            plt.xticks(xTicks)
            # plt.legend()
        plt.savefig("C:/Users/Administrator/Desktop/temp.png")
        return f




