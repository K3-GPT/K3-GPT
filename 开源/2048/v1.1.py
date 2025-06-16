# 2024.9.25  18:43
'''
实现项目：
1. 新引入了一个随机包,并改善了单元格和画布间距,使单元格看起来居中画布
2. 创建了一个字符集，限制了随机生成的数字，并在整个表格中，随机位置显示字符集内容

效果：画布表格居中，每个单元格中都有 2---4096 的随机数
'''

import tkinter as tk  #窗口包
import random  #随机包
# 主窗口、画布
列 = 4  # 列
行 = 5  # 行
单元格大小 = 100  # 单元格大小

窗口 = tk.Tk()
窗口.title("2048")       # 窗口名称
canvas = tk.Canvas(窗口, width=列 *单元格大小+20, height=行 * 单元格大小+20)  # 设置控件的宽度和高度,增加 20 像素
canvas.pack()  #实现窗口、表格可以被显示

字符集 = "2","4","8","16","32","64","128","256","512","1024","2048","4096"
# 绘制表格
for row in range(行):
    for col in range(列):
        x1 = col * 单元格大小 + 10  # 左侧增加 10 像素
        y1 = row * 单元格大小 + 10  # 顶部增加 10 像素
        x2 = x1 + 单元格大小
        y2 = y1 + 单元格大小
        canvas.create_rectangle(x1, y1, x2, y2, outline="black")

        # 随机生成一个字符串并显示在单元格中
        random_string = ''.join(random.choices(字符集, k=1))
    #  随机字符串 = 随机的列表 .join成字符串，来自 random.choices的字符集，选取k个
        canvas.create_text(x1 + 单元格大小//2, y1 + 单元格大小//2, text=random_string)
窗口.mainloop()
