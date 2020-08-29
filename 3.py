import xlrd
class ExcelData():
    def __init__(self,data_path,sheetname):
        self.data_path = data_path   #定义路径
        self.sheetname = sheetname   #传入表名
        self.data = xlrd.open_workbook(self.data_path)  #打开工作簿
        self.table = self.data.sheet_by_name(self.sheetname)  #指定表明打开
        self.keys = self.table.row_values(0)  #指定第一行为字典的key
        self.rowNum = self.table.nrows    #获取表的行数
        self.colNum = self.table.ncols    #获取表的列数
        self.falg = 0
        self.count = 0
        print(self.rowNum)
        
    def Readexcel(self):
        if self.rowNum < 2:
            print("行内无数据")
        else:
            List = []  #列表L存放读取出的数据
            for i in range(1,self.rowNum):
                sheet_data = {}   #将读取的数据保存在字典中
                # sheet_data.setdefault('count', 0)
                for j in range(self.colNum):     #j对应读取的列，若是只有2列 在前面回有记录
                    sheet_data[self.keys[j]] = self.table.row_values(i)[j]   #把第i行第j列的值取出来付给第j列的键值，构成字典
                List.append(sheet_data)     #一行取完追加到字典中
            return List
         


     #定义一个标记 若接口号不同则将标记置为0
xunhuan_flag = 0
count = 0
last_jiekou= '06058'
result = []
date_dict = {}
if __name__ == '__main__':
    data_path = "D:\\WeChat Files\\wxid_lf48k3xpfwz322\\FileStorage\\File\\2020-07\\【20200730】亚信-调度任务进展-日报.xlsx"    #这里写绝对路径
    sheetname = "Sheet1"                                              #这里写表名
    Get_data = ExcelData(data_path,sheetname)
    get_data = Get_data.Readexcel()


'''
            以下是对读出来的数据进行处理

'''
for i in get_data:
    if xunhuan_flag == 0 :   #遍历第一个接口
        xunhuan_flag +=1
        last_jiekou = i['接口号']
        count += 1
        #last_jiekou = i['接口号']  #利用一个参数接收第一个接口的接口号
        '''if i['接口号'] == last_jiekou:
            count += 1
        else :
           xunhuan_flag = 0

        last_jiekou = i['接口号']'''
           
    elif i['接口号'] == last_jiekou: #第二个接口号和第一个接口号一样，则count 会+1
        count += 1

    elif i['接口号'] != last_jiekou:# 如果第二个接口号和第一个接口号不相同
        #count +=1  #count原本是0 所以要加1
        date_dict[last_jiekou] = count   #将接口号和count写入字典
        result.append(date_dict)
        count = 1  #已匹配到新的接口，count=1
        date_dict[i['接口号']] = count   #将接口号和count写入字典
        result.append(date_dict)
        xunhuan_flag = 0
        #count =0

'''for j in date_dict:
    if date_dict[j] == 1:
        date = date_dict[j]-1
        print(date)
   '''     
print(date_dict)



'''第一次02046==02046...21021!=02046,21021 == 21021,,,发现在count1后面的count值要减一才符合'''
        




















