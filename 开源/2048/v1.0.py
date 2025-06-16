# 2024.9.25  11:56
'''
实现项目：
1. 绘制出了画布,也定义了数字生成的单元格以及画布和单元格的大小.
效果：一个白色填充画布和一个4x5表格
'''

import tkinter as tk
# 定义表格大小和单元格大小
列 = 4
行 = 5
单元格大小 = 100

# 创建主窗口和画布
窗口 = tk.Tk()
窗口.title("2048")
画布 = tk.Canvas(窗口, width=列 * 单元格大小, height=行 * 单元格大小)
画布.pack()

# 绘制表格
for row in range(行):
    for col in range(列):
        x1 = col * 单元格大小
        y1 = row * 单元格大小
        x2 = x1 + 单元格大小
        y2 = y1 + 单元格大小
        画布.create_rectangle(x1, y1, x2, y2, outline="black")

窗口.mainloop()