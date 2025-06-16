import tkinter as tk
import random

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
def generate_number():
    row = random.randint(0, 行 - 1)
    col = random.randint(0, 列 - 1)
    while canvas.itemcget(元素[row][col], "text") != "":
        row = random.randint(0, 行 - 1)
        col = random.randint(0, 列 - 1)
    canvas.itemconfig(元素[row][col], text="2")

generate_number()
generate_number()

# 定义函数,根据按键移动元素
def move_elements(direction):
    if direction == "up":
        move_up()
    elif direction == "left":
        move_left()
    elif direction == "right":
        move_right()
    elif direction == "down":
        move_down()
    generate_number()  # 每次移动后生成新数字

def move_up():
    changed = False
    for col in range(列):
        column = [canvas.itemcget(元素[row][col], "text") for row in range(行)]
        non_empty = [x for x in column if x != ""]
        new_column = []
        while non_empty:
            if len(non_empty) > 1 and non_empty[0] == non_empty[1]:
                new_column.append(str(int(non_empty[0]) * 2))
                non_empty = non_empty[2:]
            else:
                new_column.append(non_empty[0])
                non_empty = non_empty[1:]
        new_column += [""] * (行 - len(new_column))
        for row in range(行):
            if canvas.itemcget(元素[row][col], "text") != new_column[row]:
                changed = True
                canvas.itemconfig(元素[row][col], text=new_column[row])
    if changed:
        generate_number()

def move_left():
    changed = False
    for row in range(行):
        row_elements = [canvas.itemcget(元素[row][col], "text") for col in range(列)]
        non_empty = [x for x in row_elements if x != ""]
        new_row = []
        while non_empty:
            if len(non_empty) > 1 and non_empty[0] == non_empty[1]:
                new_row.append(str(int(non_empty[0]) * 2))
                non_empty = non_empty[2:]
            else:
                new_row.append(non_empty[0])
                non_empty = non_empty[1:]
        new_row += [""] * (列 - len(new_row))
        for col in range(列):
            if canvas.itemcget(元素[row][col], "text") != new_row[col]:
                changed = True
                canvas.itemconfig(元素[row][col], text=new_row[col])
    if changed:
        generate_number()

def move_right():
    changed = False
    for row in range(行):
        row_elements = [canvas.itemcget(元素[row][col], "text") for col in range(列 - 1, -1, -1)]
        non_empty = [x for x in row_elements if x != ""]
        new_row = []
        while non_empty:
            if len(non_empty) > 1 and non_empty[0] == non_empty[1]:
                new_row.append(str(int(non_empty[0]) * 2))
                non_empty = non_empty[2:]
            else:
                new_row.append(non_empty[0])
                non_empty = non_empty[1:]
        new_row += [""] * (列 - len(new_row))
        new_row.reverse()
        for col in range(列):
            if canvas.itemcget(元素[row][col], "text") != new_row[col]:
                changed = True
                canvas.itemconfig(元素[row][col], text=new_row[col])
    if changed:
        generate_number()

def move_down():
    changed = False
    for col in range(列):
        column = [canvas.itemcget(元素[row][col], "text") for row in range(行 - 1, -1, -1)]
        non_empty = [x for x in column if x != ""]
        new_column = []
        while non_empty:
            if len(non_empty) > 1 and non_empty[0] == non_empty[1]:
                new_column.append(str(int(non_empty[0]) * 2))
                non_empty = non_empty[2:]
            else:
                new_column.append(non_empty[0])
                non_empty = non_empty[1:]
        new_column += [""] * (行 - len(new_column))
        new_column.reverse()
        for row in range(行):
            if canvas.itemcget(元素[row][col], "text") != new_column[row]:
                changed = True
                canvas.itemconfig(元素[row][col], text=new_column[row])
    if changed:
        generate_number()

# 绑定键盘事件
窗口.bind("<Up>", lambda event: move_elements("up"))
窗口.bind("<Left>", lambda event: move_elements("left"))
窗口.bind("<Right>", lambda event: move_elements("right"))
窗口.bind("<Down>", lambda event: move_elements("down"))

# 运行主循环
窗口.mainloop()
