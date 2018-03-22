#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 导入Tkinter库
import Tkinter

# 创建窗口对象的背景色
root = Tkinter.Tk()
root.title = "gui"

# 创建两个列表
li = ['C', 'python', 'php', 'html', 'SQL', 'java']
movie = ['CSS', 'jQuiry', 'BootStrap']

# 创建两个列表
listb1 = Tkinter.Listbox(root)
listb2 = Tkinter.Listbox(root)

# 将数据添加进列表
for item in li:
    listb1.insert(0, item)

for item in movie:
    listb2.insert(0, item)

button = Tkinter.Button(root, text="show")
button.pack()

# 将小部件放置在主窗口中
listb1.pack()
listb2.pack()

# 进入消息循环
root.mainloop()
