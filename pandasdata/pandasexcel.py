import pandas as pd
df = pd.read_excel(
    'C://Users/wlntu/Desktop/模型上线清单/数据整合_已上线模型清单_V0.1_20190906.xls', sheetname='模型清单')
# windows路径的写法，所有的反斜杠是和windows相反的，盘符后跟双斜线
data = df.head()
print("最终获取到的数据是：{0}".format(data))
