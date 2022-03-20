import pandas as pd
import numpy as np
import sys
from pypinyin import pinyin

infile = sys.argv[1]
data = pd.read_table(infile, sep='\t', header=None)
py_in = data.values
inset = np.array(py_in)
outfile = sys.argv[2]
file = open(outfile, 'w', encoding='utf-8')
count = inset.shape[0]
prov = sys.argv[3]
pro = []
for p in inset[:, 0]:
    sum = 0
    for q in range(count):
        if inset[q][0] == p:
            sum = sum+inset[q][2]
    if (sum, p) not in pro:
        pro.append((sum, p))
pro.sort(reverse=True)
pro_sum = np.array(pro)

if prov is None:
    for i in pro_sum[:, 1]:
        for a in range(pro_sum.shape[0]):
            if pro_sum[a][1] == i:
                file.write("%s\t%s\n" % (i , pro_sum[a][0]))
        v = []   #初始化一个横坐标数组
        c = 0
        for j in range(count):
            if inset[j][0] == i:
                v.append(j)  #将横坐标存入数组
                c = c+1
        for x in v[:]: #开始排序
            for y in range(x+1, v[0]+c):
                if inset[x][2] < inset[y][2]:
                    inset[x][2], inset[y][2] = inset[y][2], inset[x][2]
                    inset[x][1], inset[y][1] = inset[y][1], inset[x][1]
                if inset[x][2] == inset[y][2]:
                    city = [inset[x][1], inset[y][1]]
                    city.sort(key=lambda string: pinyin(string))
                    inset[x][1] = city[0]
                    inset[y][1] = city[1]
            file.write("%s\t" % inset[x][1])
            file.write("%d\n" % inset[x][2])
else:
    for a in range(pro_sum.shape[0]):
        if pro_sum[a][1] == prov:
            file.write("%s\t %s\n" %( prov, pro_sum[a][0]))
    v = []  # 初始化一个横坐标数组
    c = 0
    for j in range(count):
        if inset[j][0] == prov:
            v.append(j)  # 将横坐标存入数组
            c = c + 1
    for x in v[:]:  # 开始排序
        for y in range(x + 1, v[0] + c):
            if inset[x][2] < inset[y][2]:
                inset[x][2], inset[y][2] = inset[y][2], inset[x][2]
                inset[x][1], inset[y][1] = inset[y][1], inset[x][1]
            if inset[x][2] == inset[y][2]:
                city = [inset[x][1], inset[y][1]]
                city.sort(key=lambda string: pinyin(string))
                inset[x][1] = city[0]
                inset[y][1] = city[1]
        file.write("%s\t" % inset[x][1])
        file.write("%d\n" % inset[x][2])