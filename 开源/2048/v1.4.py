'''
实现项目：
因为v1.3 版 只能实现按 上 时，移动到顶部，
为了检测键盘是否能正常检测，写了v1.4 版
同时，此版本为  "贪吃蛇" 项目留下了构想
'''
import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("方向键监听")

# 创建画布
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# 在中心创建一个10x10的实心方框
x1, y1 = 190, 190
x2, y2 = 210, 210
rect = canvas.create_rectangle(x1, y1, x2, y2, fill="black")

# 定义函数,根据按键移动方框
def move_rect(event):
    global x1, y1, x2, y2
    if event.keysym == "Up":
        canvas.move(rect, 0, -10)
        y1 -= 10
        y2 -= 10
    elif event.keysym == "Left":
        canvas.move(rect, -10, 0)
        x1 -= 10
        x2 -= 10
    elif event.keysym == "Right":
        canvas.move(rect, 10, 0)
        x1 += 10
        x2 += 10
    elif event.keysym == "Down":
        canvas.move(rect, 0, 10)
        y1 += 10
        y2 += 10

# 绑定键盘事件
root.bind("<KeyPress>", move_rect)

# 运行主循环
root.mainloop()
