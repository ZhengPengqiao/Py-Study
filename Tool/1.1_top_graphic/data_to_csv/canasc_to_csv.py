#!/usr/bin/python3

import sys
import random
import csv
import numpy as np

if ( len(sys.argv) < 2 ):
    print("USED: programe file_name")
    exit()

file_name = sys.argv[1]
print("file_name:"+file_name)

index=0
name = []
flog = []
arrY= [[] for i in np.arange(40)]

name.append("HAP_FD1")
name.append("HAP_FD3")

# 读取文件中的数据
with open(file_name, 'r') as f:
    lines = f.readlines()

    # 处理每一行
    for y in np.arange(len(name)):
        for x in np.arange(len(lines)):
            if ( name[y] in lines[x] ):
                item = lines[x].replace("  "," ").replace("  "," ").strip(' ').split(" ")
                print(item[0],item[20])
                tmp_time = float(item[0])
                tmp_val = float(item[0])
                arrY[index].append(tmp_time+","+tmp_val)
        index=index+1

for x in np.arange(len(name)):
    print(name[x], "arrY[",len(arrY[x]),"]=", arrY[x])

line=[]
with open(file_name+".csv", 'w+') as f:
    writer = csv.writer(f)
    for y in np.arange(len(name)):
        line.clear()
        line.append(name[y])
        for item in (np.arange(len(arrY[y]))):
            line.append(arrY[y][item])
        print(line)
        writer.writerow(line)

print("\n")
print("===================================================================")
print("               需要保证在意的进程尽量有数据，不然时间轴会存在偏差          ")
print("===================================================================")
