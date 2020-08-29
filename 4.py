import pandas as pd
df = pd.read_excel(io="D:\\WeChat Files\\wxid_lf48k3xpfwz322\\FileStorage\\File\\2020-07\\【20200730】亚信-调度任务进展-日报.xlsx"\
                   ,sheet_name="Sheet1",usecols=[0,1],names=["prov_id", "interface_id"])
pd.set_option('display.max_rows', None)#显示所有行
'''#pd.set_option('display.max_columns', None)#显示所有列
pd.set_option('max_colwidth',100)#设置上面的最大显示长度为100，默认50（可省略）
#pd.set_option('display.width',None)#显示宽度无限
#agg({"count":})'''
#df.sort_values('prov_id',ascending=False,inplace=True)
#res=df.groupby('interface_id').count()
#print(res)
groupData=df.sort_index(ascending=False).groupby("interface_id").count()
print(groupData)


#.sort()排序
#.sort(reverse=True)逆序排序
