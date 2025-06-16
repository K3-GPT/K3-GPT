'''
实现项目：
根据v1.4 版的理论，更改了映射器和监视器
功能实现：
1.使用户能够上下左右移动
2.初次合并
'''

import tkinter as tk
import random
import keyboard

# 主窗口、画布
列 = 4
行 = 5
单元格大小 = 100

窗口 = tk.Tk()
窗口.title("2048")
canvas = tk.Canvas(窗口, width=列 * 单元格大小 + 20, height=行 * 单元格大小 + 20)
canvas.pack()

字符集 = "2", "4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096"

# 绘制表格
单元格 = []
元素 = []
for row in range(行):
    row_cells = []
    row_elements = []
    for col in range(列):
        x1 = col * 单元格大小 + 10
        y1 = row * 单元格大小 + 10
        x2 = x1 + 单元格大小
        y2 = y1 + 单元格大小
        cell = canvas.create_rectangle(x1, y1, x2, y2, outline="blue")
        element = canvas.create_text(x1 + 单元格大小 // 2, y1 + 单元格大小 // 2, text="", font=("Arial", 40))
        row_cells.append(cell)
        row_elements.append(element)
    单元格.append(row_cells)
    元素.append(row_elements)

# 随机生成两个位置,并在这两个位置绘制 2 和 4
第一个数_行 = random.randint(0, 行 - 1)
第一个数_列 = random.randint(0, 列 - 1)
第2个数_行 = random.randint(0, 行 - 1)
第2个数_列 = random.randint(0, 列 - 1)

# 确保两个随机位置不同
while (第一个数_行 == 第2个数_行 and 第一个数_列 == 第2个数_列):
    第2个数_行 = random.randint(0, 行 - 1)
    第2个数_列 = random.randint(0, 列 - 1)

canvas.itemconfig(元素[第一个数_行][第一个数_列], text="2")
canvas.itemconfig(元素[第2个数_行][第2个数_列], text="2")

# 定义函数,根据按键移动元素
def move_elements(key):
    if key == "up":
        move_up()
    elif key == "left":
        move_left()
    elif key == "right":
        move_right()
    elif key == "down":
        move_down()

def move_up():
    changed = False
    for col in range(列):
        column = [canvas.itemcget(元素[row][col], 'text') for row in range(行)]
        non_empty = [num for num in column if num != ""]
        new_column = []
        while non_empty:
            if len(non_empty) > 1 and non_empty[0] == non_empty[1]:
                new_value = str(int(non_empty[0]) * 2)
                new_column.append(new_value)
                non_empty = non_empty[2:]
                changed = True
            else:
                new_column.append(non_empty[0])
                non_empty = non_empty[1:]
        new_column += [""] * (行 - len(new_column))
        for row in range(行):
            if canvas.itemcget(元素[row][col], 'text') != new_column[row]:
                changed = True
                canvas.itemconfig(元素[row][col], text=new_column[row])
    return changed

def move_left():
    changed = False
    for row in range(行):
        row_elements = [canvas.itemcget(元素[row][col], 'text') for col in range(列)]
        non_empty = [num for num in row_elements if num != ""]
        new_row = []
        while non_empty:
            if len(non_empty) > 1 and non_empty[0] == non_empty[1]:
                new_value = str(int(non_empty[0]) * 2)
                new_row.append(new_value)
                non_empty = non_empty[2:]
                changed = True
            else:
                new_row.append(non_empty[0])
                non_empty = non_empty[1:]
        new_row += [""] * (列 - len(new_row))
        for col in range(列):
            if canvas.itemcget(元素[row][col], 'text') != new_row[col]:
                changed = True
                canvas.itemconfig(元素[row][col], text=new_row[col])
    return changed

def move_right():
    changed = False
    for row in range(行):
        row_elements = [canvas.itemcget(元素[row][col], 'text') for col in range(列 - 1, -1, -1)]
        non_empty = [num for num in row_elements if num != ""]
        new_row = []
        while non_empty:
            if len(non_empty) > 1 and non_empty[0] == non_empty[1]:
                new_value = str(int(non_empty[0]) * 2)
                new_row.append(new_value)
                non_empty = non_empty[2:]
                changed = True
            else:
                new_row.append(non_empty[0])
                non_empty = non_empty[1:]
        new_row = ([""] * (列 - len(new_row))) + new_row
        for col in range(列):
            if canvas.itemcget(元素[row][col], 'text') != new_row[col]:
                changed = True
                canvas.itemconfig(元素[row][col], text=new_row[col])
    return changed

def move_down():
    changed = False
    for col in range(列):
        column = [canvas.itemcget(元素[row][col], 'text') for row in range(行 - 1, -1, -1)]
        non_empty = [num for num in column if num != ""]
        new_column = []
        while non_empty:
            if len(non_empty) > 1 and non_empty[0] == non_empty[1]:
                new_value = str(int(non_empty[0]) * 2)
                new_column.append(new_value)
                non_empty = non_empty[2:]
                changed = True
            else:
                new_column.append(non_empty[0])
                non_empty = non_empty[1:]
        new_column = ([""] * (行 - len(new_column))) + new_column
        for row in range(行):
            if canvas.itemcget(元素[row][col], 'text') != new_column[row]:
                changed = True
                canvas.itemconfig(元素[row][col], text=new_column[row])
    return changed


# 监听键盘输入
keyboard.on_press_key("up", lambda _: move_elements("up"))
keyboard.on_press_key("left", lambda _: move_elements("left"))
keyboard.on_press_key("right", lambda _: move_elements("right"))
keyboard.on_press_key("down", lambda _: move_elements("down"))

# 运行主循环
窗口.mainloop()