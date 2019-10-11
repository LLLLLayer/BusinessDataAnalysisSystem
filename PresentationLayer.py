import tkinter
import tkinter.messagebox
# import BusinessLogicLayer
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
import socket
import struct
from PIL import Image,ImageTk

class MyWin:
    def drawWin(self):
        # 主窗口设置
        self.root.title("Business data analysis system")
        self.root.geometry("700x900+500+100")
        # label标题
        labelTitle = tkinter.Label(self.root, text="Business data analysis system", font=("黑体", 35))
        labelTitle.place(x=120, y=20, width=500, height=40)
        # label查询内容
        labelChoose = tkinter.Label(self.root, text="Queries:", font=("黑体", 20))
        labelChoose.place(x=30, y=70, width=100, height=25)
        # label图表类型
        labelType = tkinter.Label(self.root, text="Chart type:", font=("黑体", 20))
        labelType.place(x=350, y=70, width=100, height=25)
        # 查询内容选择
        variableChoose = tkinter.StringVar(self.root)
        variableChoose.set("defult")  # default value
        OptionMenuChoose = tkinter.OptionMenu(self.root, variableChoose, "前收盘价和开盘价", "最高价和最低价","均价","换手率")
        OptionMenuChoose.place(x=150, y=70, width=150, height=25)
        # 图表类型选择
        variableType = tkinter.StringVar(self.root)
        variableType.set("defult")  # default value
        OptionType = tkinter.OptionMenu(self.root, variableType, "折线图", "散点图")
        OptionType.place(x=480, y=70, width=150, height=25)
        # button ok
        def getChooses():
            # print(variableChoose.get())
            # print(variableType.get())
            # 图表绘制
            cstr = variableChoose.get()
            tstr = variableType.get()
            if((cstr == "defult") or (tstr=="defulet")):
                tkinter.messagebox.showinfo('Prompt', 'Selection error!')
                return

            # BP = BusinessLogicLayer.BusinessProcess(1,cstr,tstr)
            # self.figure = BP.CreatMatplotlib()
            # print(self.figure)
            # self.canvas = FigureCanvasTkAgg(self.figure, self.root)
            # self.canvas.draw()
            # self.canvas.get_tk_widget().place(x=0, y=0)
            # #self.toolbar = NavigationToolbar2Tk(self.canvas, self.root)
            # #self.toolbar.update()
            # self.canvas._tkcanvas.place(x=50, y=140)

            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(('139.196.161.28', 8888))
            data = cstr + tstr
            data = data.encode('utf-8')
            client.sendall(b'1' + data)
            # with open("/Users/layer/PycharmProjects/BusinessDataAnalysisSystem/temp.png", "wb") as file:
            while True:
                    fileinfo_size = struct.calcsize('128sq')
                    buf = client.recv(fileinfo_size)  # 接收图片名
                    if buf:
                        filename, filesize = struct.unpack('128sq', buf)
                        recvd_size = 0
                        fp = open("/Users/layer/PycharmProjects/BusinessDataAnalysisSystem/temp.png", 'wb')
                        while not recvd_size == filesize:
                            if filesize - recvd_size > 1024:
                                data = client.recv(1024)
                                recvd_size += len(data)
                            else:
                                data = client.recv(1024)
                                recvd_size = filesize
                            fp.write(data)
                        fp.close()
                    client.close()
                    break

            load=Image.open("/Users/layer/PycharmProjects/BusinessDataAnalysisSystem/temp.png")
            render=ImageTk.PhotoImage(load)
            img=tkinter.Label(self.root,image=render)
            img.image=render
            img.place(x=50, y=140)

        buttonOK = tkinter.Button(self.root, text="OK", command=getChooses)
        buttonOK.place(x=480, y=110, width=140, height=25)

        # 上证指数计算
        def ShanghaiCompositeIndex():
            top=tkinter.Toplevel()
            top.title("The Shanghai composite index")
            top.geometry("530x200")

            labeldate1 = tkinter.Label(top, text="报告期:", font=("黑体", 15))
            labeldate1.place(x=0, y=8, width=100, height=15)
            labeldate1 = tkinter.Label(top, text="基期:", font=("黑体", 15))
            labeldate1.place(x=0, y=35, width=100, height=15)

            # 年
            variableyear1 = tkinter.StringVar(top)
            variableyear1.set("defult")  # default value
            OptionMenuyear1 = tkinter.OptionMenu(top, variableyear1, "1999", "2000", "2001", "2002","2003",
                                                 "2004","2005","2006","2007","2008","2009","2010","2011","2012",
                                                 "2013","2014","2015","2016")
            OptionMenuyear1.place(x=100, y=3, width=100, height=25)

            labeldyear1 = tkinter.Label(top, text="年", font=("黑体", 15))
            labeldyear1.place(x=210, y=8, width=15, height=15)
            # 月
            variablemon1 = tkinter.StringVar(top)
            variablemon1.set("defult")  # default value
            OptionMenumon1 = tkinter.OptionMenu(top, variablemon1, "01", "02", "03", "04","05",
                                                 "06","07","08","09","10","11","12")
            OptionMenumon1.place(x=230, y=3, width=100, height=25)
            labeldmon1 = tkinter.Label(top, text="月", font=("黑体", 15))
            labeldmon1.place(x=340, y=8, width=15, height=15)
            # 日
            variableday1 = tkinter.StringVar(top)
            variableday1.set("defult")  # default value
            OptionMenuday1 = tkinter.OptionMenu(top, variableday1, "01", "02", "03", "04","05",
                                                 "06","07","08","09","10","11", "12", "13", "14","15",
                                                 "16","17","18","19","20","21", "22", "23", "24","25",
                                                 "26","27","28","29","30","31")
            OptionMenuday1.place(x=370, y=3, width=100, height=25)
            labeldday1 = tkinter.Label(top, text="日", font=("黑体", 15))
            labeldday1.place(x=480, y=8, width=15, height=15)

            # 年
            variableyear2 = tkinter.StringVar(top)
            variableyear2.set("defult")  # default value
            OptionMenuyear2 = tkinter.OptionMenu(top, variableyear2, "1999", "2000", "2001", "2002","2003",
                                                 "2004","2005","2006","2007","2008","2009","2010","2011","2012",
                                                 "2013","2014","2015","2016")
            OptionMenuyear2.place(x=100, y=35, width=100, height=25)

            labeldyear2 = tkinter.Label(top, text="年", font=("黑体", 15))
            labeldyear2.place(x=210, y=38, width=15, height=15)
            # 月
            variablemon2 = tkinter.StringVar(top)
            variablemon2.set("defult")  # default value
            OptionMenumon2 = tkinter.OptionMenu(top, variablemon2, "01", "02", "03", "04","05",
                                                 "06","07","08","09","10","11","12")
            OptionMenumon2.place(x=230, y=35, width=100, height=25)
            labeldmon2 = tkinter.Label(top, text="月", font=("黑体", 15))
            labeldmon2.place(x=340, y=38, width=15, height=15)
            # 日
            variableday2 = tkinter.StringVar(top)
            variableday2.set("defult")  # default value
            OptionMenuday2 = tkinter.OptionMenu(top, variableday2, "01", "02", "03", "04","05",
                                                 "06","07","08","09","10","11", "12", "13", "14","15",
                                                 "16","17","18","19","20","21", "22", "23", "24","25",
                                                 "26","27","28","29","30","31")
            OptionMenuday2.place(x=370, y=35, width=100, height=25)
            labeldday2 = tkinter.Label(top, text="日", font=("黑体", 15))
            labeldday2.place(x=480, y=38, width=15, height=15)

            labels = tkinter.Label(top, text="上证指数:", font=("黑体", 15))
            labels.place(x=0, y=125, width=100, height=15)

            outs = tkinter.Variable()
            entryouts = tkinter.Entry(top, textvariable=outs)
            entryouts.place(x=100, y=120, width=350, height=25)

            def getIndex():
                data1=variableyear1.get()+variablemon1.get()+variableday1.get()
                data2=variableyear2.get()+variablemon2.get()+variableday2.get()
                print(data1+"\n"+data2)
                #BP = BusinessLogicLayer.BusinessProcess(2, data1, data2)
                #res = BP.getShanghaiCompositeIndex()
                #print(str(res))
                #outs.set(str(res))

                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect(('139.196.161.28', 8888))
                while True:
                    data = data1+data2
                    data = data.encode('utf-8')
                    if data == b'quit':
                        print(b'connect quit.')
                        break
                    else:#
                        client.sendall(b'2'+data)
                        rec_data = client.recv(1024)
                        print(b'form server receive:' + rec_data)
                        break
                btos = str(rec_data, encoding="utf8")
                client.sendall(b'quit')
                client.close()
                outs.set(btos)

            buttonIndex = tkinter.Button(top, text="OK", command=getIndex)
            buttonIndex.place(x=350, y=80, width=140, height=25)

            top.mainloop()

        buttonIndex = tkinter.Button(self.root, text="The Shanghai composite index", command=ShanghaiCompositeIndex)
        buttonIndex.place(x=150, y=110, width=300, height=25)

        # search
        def Search():
            searchtop=tkinter.Toplevel()
            searchtop.title("Search")
            searchtop.geometry("530x200")

            labeldate = tkinter.Label(searchtop, text="日期:", font=("黑体", 15))
            labeldate.place(x=0, y=8, width=100, height=15)
            labelsearch = tkinter.Label(searchtop, text="内容:", font=("黑体", 15))
            labelsearch.place(x=0, y=40, width=100, height=15)

            # 年
            variableyear = tkinter.StringVar(searchtop)
            variableyear.set("defult")  # default value
            OptionMenuyear = tkinter.OptionMenu(searchtop, variableyear, "1999", "2000", "2001", "2002", "2003",
                                                 "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012",
                                                 "2013", "2014", "2015", "2016")
            OptionMenuyear.place(x=100, y=3, width=100, height=25)

            labeldyear = tkinter.Label(searchtop, text="年", font=("黑体", 15))
            labeldyear.place(x=210, y=8, width=15, height=15)
            # 月
            variablemon = tkinter.StringVar(searchtop)
            variablemon.set("defult")  # default value
            OptionMenumon = tkinter.OptionMenu(searchtop, variablemon, "01", "02", "03", "04", "05",
                                                "06", "07", "08", "09", "10", "11", "12")
            OptionMenumon.place(x=230, y=3, width=100, height=25)
            labeldmon = tkinter.Label(searchtop, text="月", font=("黑体", 15))
            labeldmon.place(x=340, y=8, width=15, height=15)
            # 日
            variableday = tkinter.StringVar(searchtop)
            variableday.set("defult")  # default value
            OptionMenuday = tkinter.OptionMenu(searchtop, variableday, "01", "02", "03", "04", "05",
                                                "06", "07", "08", "09", "10", "11", "12", "13", "14", "15",
                                                "16", "17", "18", "19", "20", "21", "22", "23", "24", "25",
                                                "26", "27", "28", "29", "30", "31")
            OptionMenuday.place(x=370, y=3, width=100, height=25)
            labeldday = tkinter.Label(searchtop, text="日", font=("黑体", 15))
            labeldday.place(x=480, y=8, width=15, height=15)

            # 内容
            variablesearch = tkinter.StringVar(searchtop)
            variablesearch.set("defult")  # default value
            OptionMenuesearch = tkinter.OptionMenu(searchtop, variablesearch, "市盈率", "市净率", "市销率", "市现率")
            OptionMenuesearch.place(x=100, y=35, width=400, height=25)

            def dosearch():
                strday=variableyear.get()+variablemon.get()+variableday.get()
                strsearch=variablesearch.get()
                print(strday+strsearch)
                # BP = BusinessLogicLayer.BusinessProcess(3,strday,strsearch)
                # outs.set(BP.getSearchRes())

                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect(('139.196.161.28', 8888))
                while True:
                    data = strday+strsearch
                    data = data.encode('utf-8')
                    if data == b'quit':
                        print(b'connect quit.')
                        break
                    else:#
                        client.sendall(b'3'+data)
                        rec_data = client.recv(1024)
                        print(b'form server receive:' + rec_data)
                        break
                btos = str(rec_data, encoding="utf8")
                client.sendall(b'quit')
                client.close()
                outs.set(btos)

            # ok
            buttonSearch = tkinter.Button(searchtop, text="OK", command=dosearch)
            buttonSearch.place(x=370, y=90, width=70, height=25)
            # out
            outs = tkinter.Variable()
            entryouts = tkinter.Entry(searchtop, textvariable=outs)
            entryouts.place(x=30, y=140, width=450, height=25)

            searchtop.mainloop()



        buttonIndex = tkinter.Button(self.root, text="Search", command=Search)
        buttonIndex.place(x=50, y=110, width=70, height=25)

    def __init__(self):
        self.root = tkinter.Tk()
        self.drawWin()
        self.root.mainloop()


if __name__ == "__main__":
    # client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client.connect(('139.196.161.28', 8888))
    # while True:
    #     data = input()
    #     data = data.encode('utf-8')
    #     if data == b'quit':
    #         print(b'connect quit.')
    #         break
    #     else:
    #         client.sendall(data)
    #         rec_data = client.recv(1024)
    #         print(b'form server receive:' + rec_data)
    #         break
    #
    # client.sendall(b'quit')
    # client.close()

    MyWin=MyWin()

