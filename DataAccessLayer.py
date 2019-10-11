import pymysql

def connect():
    return pymysql.connect("awstest.cuo6db9gvsjw.us-east-1.rds.amazonaws.com",
                           "admin",
                           "12345678",
                           "testDB")

def getcursor():
    return connect().cursor()

def getFetchall(sql):
    cursor=getcursor()
    cursor.execute(sql)
    return cursor.fetchall()


sqlDate = "SELECT 日期 FROM StockMarket"
sqlTotalMarketValue = "SELECT 总市值 FROM StockMarket"
sqlBeforeClosing = "SELECT 前收盘价 FROM StockMarket"  # 前收盘价
sqlTheOpening = "SELECT 开盘价 FROM StockMarket"  # 开盘价
sqlTheHighest = "SELECT 最高价 FROM StockMarket"  # 最高价
sqlTheLowest = "SELECT 最低价 FROM StockMarket"  # 最低价
sqlAveragePrice = "SELECT 均价 FROM StockMarket"  # 均价
sqlTurnoverRate = "SELECT 换手率 FROM StockMarket"  # 换手率
sqlLowestClosing = "SELECT 最低收盘价 FROM StockMarket"  # 最低收盘价
sqlVolume  = "SELECT 成交量 FROM StockMarket"  # 成交量
sqlClinchADealAmount = "SELECT 成交金额 FROM StockMarket"  # 成交金额
sqlRiseAndFall = "SELECT 涨跌 FROM StockMarket"  # 涨跌
sqlApplies = "SELECT 涨跌幅 FROM StockMarket"  # 涨跌幅
sqlAveragePrice = "SELECT 均价 FROM StockMarket"  # 均价
sqlAshareCurrentMarketValue = "SELECT A股流通市值 FROM StockMarket"  # A股流通市值
sqlBsharesOutstandingMarketValue = "SELECT B股流通市值 FROM StockMarket"  # B股流通市值
sqlTotalMarketValue = "SELECT 总市值 FROM StockMarket"  # 总市值
sqlAshareCirculatingCapitalStock = "SELECT A股流通股本 FROM StockMarket"  #  A股流通股本
sqlBsharesCirculatingCapitalStock = "SELECT B股流通股本 FROM StockMarket"  # B股流通股本
sqlTotalEquity = "SELECT 总股本 FROM StockMarket"  # 总股本
sqlPeRatio = "SELECT 市盈率 FROM StockMarket"  # 市盈率
sqlPriceToBook = "SELECT 市净率 FROM StockMarket"  # 市净率
sqlPriceToSalesRatio = "SELECT 市销率 FROM StockMarket"  # 市销率
TheCityRate = "SELECT 市现率 FROM StockMarket"  # 市现率

