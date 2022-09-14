"""
查看由爬虫获取的数据集是否存在某些日期的缺失
"""

import os
import datetime
 
def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y%m%d')
    except ValueError:
        return False
    return True

dirs = 'dataset'
items = os.listdir(dirs)

for i in range(20200120, 20220723):
    if not validate(str(i)):
        continue
    notFound = True
    for item in items:
        num = int(item.split('.')[0])
        if num == i:
            notFound = False
            break
    if notFound:
        print(f'{i}.csv not Found')