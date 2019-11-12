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
arrY= [[] for i in np.arange(20)]

name.append("Overall Bus Load")
name.append("Read:")
name.append("Write:")
name.append("Total:")


# 读取文件中的数据
with open(file_name, 'r') as f:
    lines = f.readlines()
    for y in np.arange(len(name)):
        for x in np.arange(len(lines)):
            if( name[y] in lines[x] and name[y]=="Overall Bus Load" ):
                item = lines[x].strip('\n').split(":")
                tmp_val = float(item[1].replace("%",""))
                arrY[index].append(tmp_val)
            if ( name[y] in lines[x] and name[y]=="Read:" ):
                item = lines[x].strip('\n').split(" ")
                tmp_val = float(item[1])
                arrY[index].append(tmp_val)
            if ( name[y] in lines[x] and name[y]=="Write:" ):
                item = lines[x].strip('\n').split(" ")
                tmp_val = float(item[6].replace("%",""))
                arrY[index].append(tmp_val)
            if ( name[y] in lines[x] and name[y]=="Total:" ):
                item = lines[x].strip('\n').split(" ")
                tmp_val = float(item[10].replace("%",""))
                arrY[index].append(tmp_val)

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
