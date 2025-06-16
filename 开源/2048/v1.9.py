'''
实现项目：
1.加入"重玩 " 功能键
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

# 添加重玩按钮
def reset_game():
    for row in range(行):
        for col in range(列):
            canvas.itemconfig(元素[row][col], text="")
            update_cell_color(row, col, "")  # 清空颜色
    generate_number()
    generate_number()

重玩按钮 = tk.Button(窗口, text="重玩", command=reset_game)
重玩按钮.pack(side=tk.TOP)

元素 = []
单元格 = []
for row in range(行):
    row_elements = []
    for col in range(列):
        x1 = col * 单元格大小 + 10
        y1 = row * 单元格大小 + 10
        # 绘制单元格边框
        cell = canvas.create_rectangle(x1, y1, x1 + 单元格大小, y1 + 单元格大小, outline="blue")
        element = canvas.create_text(x1 + 单元格大小 // 2, y1 + 单元格大小 // 2, text="", font=("Arial", 40))
        row_elements.append(element)
        单元格.append(cell)
    元素.append(row_elements)

# 颜色映射
颜色映射 = {
    "2": "#FFFFFF",
    "4": "#F0E68C",
    "8": "#FFB565",
    "16": "#FF8C00",
    "32": "#FFFFE0",
    "64": "#FFFF00",
    "128": "#E6E6FA",
    "256": "#90EE90",
    "512": "#008000",
    "1024": "#FFB6C1",
    "2048": "#FF0000",
    "4096": "#FFBFFF",
    "8192": "#FFC0CB"
}

# 随机生成数字
def generate_number():
    empty_cells = [(row, col) for row in range(行) for col in range(列) if canvas.itemcget(元素[row][col], 'text') == ""]
    if empty_cells:
        row, col = random.choice(empty_cells)
        canvas.itemconfig(元素[row][col], text="2")
        canvas.itemconfig(单元格[row * 列 + col], fill=颜色映射["2"])

# 初始化两个数字
generate_number()
generate_number()

# 检查游戏状态
def check_game_over():
    all_filled = all(canvas.itemcget(元素[row][col], 'text') != "" for row in range(行) for col in range(列))
    if not all_filled:
        return False

    for row in range(行):
        for col in range(列):
            if col < 列 - 1 and canvas.itemcget(元素[row][col], 'text') == canvas.itemcget(元素[row][col + 1], 'text'):
                return False
            if row < 行 - 1 and canvas.itemcget(元素[row][col], 'text') == canvas.itemcget(元素[row + 1][col], 'text'):
                return False

    game_over_window = tk.Toplevel(窗口)
    tk.Label(game_over_window, text="游戏失败", font=("Arial", 64)).pack(padx=20, pady=20)
    tk.Button(game_over_window, text="关闭", command=game_over_window.destroy).pack(pady=10)

# 更新单元格颜色
def update_cell_color(row, col, value):
    color = 颜色映射.get(value, "white")
    canvas.itemconfig(单元格[row * 列 + col], fill=color)

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

# 各个方向的移动函数
def move_up():
    for col in range(列):
        column = [canvas.itemcget(元素[row][col], 'text') for row in range(行)]
        non_empty = [num for num in column if num != ""]
        new_column = []
        i = 0
        while i < len(non_empty):
            if i + 1 < len(non_empty) and non_empty[i] == non_empty[i + 1]:
                new_value = str(int(non_empty[i]) * 2)
                new_column.append(new_value)
                i += 2
            else:
                new_column.append(non_empty[i])
                i += 1
        new_column += [""] * (行 - len(new_column))
        for row in range(行):
            canvas.itemconfig(元素[row][col], text=new_column[row])
            update_cell_color(row, col, new_column[row])
    generate_number()
    check_game_over()

def move_left():
    for row in range(行):
        row_elements = [canvas.itemcget(元素[row][col], 'text') for col in range(列)]
        non_empty = [num for num in row_elements if num != ""]
        new_row = []
        i = 0
        while i < len(non_empty):
            if i + 1 < len(non_empty) and non_empty[i] == non_empty[i + 1]:
                new_value = str(int(non_empty[i]) * 2)
                new_row.append(new_value)
                i += 2
            else:
                new_row.append(non_empty[i])
                i += 1
        new_row += [""] * (列 - len(new_row))
        for col in range(列):
            canvas.itemconfig(元素[row][col], text=new_row[col])
            update_cell_color(row, col, new_row[col])
    generate_number()
    check_game_over()

def move_right():
    for row in range(行):
        row_elements = [canvas.itemcget(元素[row][col], 'text') for col in range(列 - 1, -1, -1)]
        non_empty = [num for num in row_elements if num != ""]
        new_row = []
        i = 0
        while i < len(non_empty):
            if i + 1 < len(non_empty) and non_empty[i] == non_empty[i + 1]:
                new_value = str(int(non_empty[i]) * 2)
                new_row.append(new_value)
                i += 2
            else:
                new_row.append(non_empty[i])
                i += 1
        new_row = ([""] * (列 - len(new_row))) + new_row
        for col in range(列):
            canvas.itemconfig(元素[row][col], text=new_row[col])
            update_cell_color(row, col, new_row[col])
    generate_number()
    check_game_over()

def move_down():
    for col in range(列):
        column = [canvas.itemcget(元素[row][col], 'text') for row in range(行 - 1, -1, -1)]
        non_empty = [num for num in column if num != ""]
        new_column = []
        i = 0
        while i < len(non_empty):
            if i + 1 < len(non_empty) and non_empty[i] == non_empty[i + 1]:
                new_value = str(int(non_empty[i]) * 2)
                new_column.append(new_value)
                i += 2
            else:
                new_column.append(non_empty[i])
                i += 1
        new_column = ([""] * (行 - len(new_column))) + new_column
        for row in range(行):
            canvas.itemconfig(元素[row][col], text=new_column[row])
            update_cell_color(row, col, new_column[row])
    generate_number()
    check_game_over()

# 监听键盘输入
keyboard.on_press_key("up", lambda _: move_elements("up"))
keyboard.on_press_key("left", lambda _: move_elements("left"))
keyboard.on_press_key("right", lambda _: move_elements("right"))
keyboard.on_press_key("down", lambda _: move_elements("down"))

# 运行主循环
窗口.mainloop()
