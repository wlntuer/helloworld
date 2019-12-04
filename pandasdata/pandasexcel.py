import pandas as pd
import jieba
from collections import Counter
df = pd.read_excel(
    'D://DIP/模型上线清单/数据整合_已上线模型清单_V0.1_20190906.xls', sheet_name='模型清单')
# windows路径的写法，所有的反斜杠是和windows相反的，盘符后跟双斜线
data = df.head()
# print("最终获取到的数据是：{0}".format(data))
cnt_model = df.loc[:, '模型说明（100~150字之间）'].head(5)
#ata = cnt_model.head()
# print("最终获取到的数据是：{0}".format(ata))
lg_cnt = ("".join(i for i in cnt_model))
# print(lg_cnt)
seg_list = jieba.cut(lg_cnt, cut_all=True)  # generate生成器
# print('\n'.join(seg_list))
# print(type(seg_list))
res = Counter(seg_list)  # collections.Counter
print(type(res))
print(res)
print('-------------another method-----------------')
result = pd.value_counts(list(seg_list))
print(type(result))  # pandas.core.series.Series
