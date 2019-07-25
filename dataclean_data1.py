import os
import xlrd
import pandas as pd


def access_data(row):
    tittle_list.append(row[0])
    auth_list.append("null")
    time_list.append("null")
    content_list.append(row[1])


def read_excel(file_name):
    wb = xlrd.open_workbook(filename=file_name)  # 打开文件
    print(wb.sheet_names())  # 获取所有表格名字
    sheet1 = wb.sheet_by_index(0)  # 通过索引获取表格
    print(sheet1.nrows)
    for i in range(sheet1.nrows):
        rows = sheet1.row_values(i)  # 获取行内容
        access_data(rows)
        # print(rows)


tittle_list = []
auth_list = []
time_list = []
content_list = []
g = os.walk(r"data1")

for path, dir_list, file_list in g:
    for file in file_list:
        print(os.path.join(path, file))
        read_excel(os.path.join(path, file))

c = {"tittle": tittle_list,
     "auth_list": auth_list,
     "time_list": time_list,
     'content_list': content_list}  # 将列表list换成字典

data = pd.DataFrame(c)
print(data)
data.to_csv('data1.csv')

# res = pd.concat([data,data1],axis=0,ignore_index=True) 合并代码
# res.to_csv('11w_mian.csv')
