'''
#1 第一版 可以输入英文和数字，但中文只能使用拼音

import pyautogui
import time

# 模拟在微信窗口中发送消息
def send_wechat_messages(message, count):
    print("请在5秒内将光标放置在微信的聊天输入框...")
    time.sleep(5)  # 给用户时间将光标放到输入框

    for i in range(count):
        pyautogui.typewrite(message)  # 输入消息
        pyautogui.press("space")  # 模拟按下空格键
        pyautogui.press("enter")  # 模拟按下回车键发送消息
        print(f"第 {i + 1} 条消息已发送：{message}")
       # time.sleep(1)  # 间隔1秒发送一条消息

if __name__ == "__main__":
    message = input("请输入要发送的消息: ")
    count = int(input("请输入发送的次数: "))
    send_wechat_messages(message, count)
'''

'''
#2 第二版 可以输入中文，使用粘贴板的方式复制用户输入的内容进行粘贴发送

import pyautogui
import time
import pyperclip  # 用于操作剪贴板

# 模拟在微信窗口中发送中文或其他复杂字符的消息
def send_wechat_messages(message, count):
    print("请在5秒内将光标放置在微信的聊天输入框...")
    time.sleep(5)  # 给用户时间将光标放到输入框

    for i in range(count):
        # 使用剪贴板方式粘贴中文
        pyperclip.copy(message)  # 将消息复制到剪贴板
        pyautogui.hotkey("ctrl", "v")  # 粘贴消息
        pyautogui.press("enter")  # 模拟按下回车键发送消息
        print(f"第 {i + 1} 条消息已发送：{message}")
        time.sleep(0.5)  # 间隔0.5秒发送一条消息

if __name__ == "__main__":
    message = input("请输入要发送的消息: ")  # 支持输入中文
    count = int(input("请输入发送的次数: "))
    send_wechat_messages(message, count)
'''

'''
#3 第三版 添加了ui，但是没有发送延时

import pyautogui
import pyperclip
import time
import tkinter as tk
from tkinter import messagebox

# 模拟在微信窗口中发送消息
def send_wechat_messages(message, count):
    if not message or count <= 0:
        messagebox.showerror("错误", "请输入有效的消息和次数！")
        return

    messagebox.showinfo("提示", "请在5秒内将光标放置在微信的聊天输入框...")
    time.sleep(5)  # 给用户时间将光标放到输入框

    for i in range(count):
        pyperclip.copy(message)  # 将消息复制到剪贴板
        pyautogui.hotkey("ctrl", "v")  # 粘贴消息
        pyautogui.press("enter")  # 模拟按下回车键发送消息
        print(f"第 {i + 1} 条消息已发送：{message}")
        time.sleep(0.5)  # 间隔0.5秒发送一条消息

    messagebox.showinfo("完成", "消息发送完成！")

# 创建主界面
def create_ui():
    root = tk.Tk()
    root.title("微信消息自动发送")

    # 消息输入框
    tk.Label(root, text="要发送的消息:").grid(row=0, column=0, padx=10, pady=10)
    message_entry = tk.Entry(root, width=30)
    message_entry.grid(row=0, column=1, padx=10, pady=10)

    # 次数输入框
    tk.Label(root, text="发送的次数:").grid(row=1, column=0, padx=10, pady=10)
    count_entry = tk.Entry(root, width=10)
    count_entry.grid(row=1, column=1, padx=10, pady=10)

    # 开始按钮
    def start_sending():
        message = message_entry.get()
        try:
            count = int(count_entry.get())
        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字作为次数！")
            return

        send_wechat_messages(message, count)

    tk.Button(root, text="开始发送", command=start_sending).grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_ui()
'''

'''
#4 第四版 完成了自定义间隔时长，缺少ui自适应

import pyautogui
import pyperclip
import time
import tkinter as tk
from tkinter import messagebox

# 模拟在微信窗口中发送消息
def send_wechat_messages(message, count, interval):
    if not message or count <= 0 or interval < 0:
        messagebox.showerror("错误", "请输入有效的消息、次数和时间间隔！")
        return

    messagebox.showinfo("提示", "请在5秒内将光标放置在微信的聊天输入框...")
    time.sleep(5)  # 给用户时间将光标放到输入框

    for i in range(count):
        pyperclip.copy(message)  # 将消息复制到剪贴板
        pyautogui.hotkey("ctrl", "v")  # 粘贴消息
        pyautogui.press("enter")  # 模拟按下回车键发送消息
        print(f"第 {i + 1} 条消息已发送：{message}")
        time.sleep(interval)  # 间隔指定的时间发送下一条消息

    messagebox.showinfo("完成", "消息发送完成！")

# 创建主界面
def create_ui():
    root = tk.Tk()
    root.title("消息轰炸小程序")

    # 消息输入框
    tk.Label(root, text="要发送的消息:").grid(row=0, column=0, padx=10, pady=10)
    message_entry = tk.Entry(root, width=30)
    message_entry.grid(row=0, column=1, padx=10, pady=10)

    # 次数输入框
    tk.Label(root, text="发送的次数:").grid(row=1, column=0, padx=10, pady=10)
    count_entry = tk.Entry(root, width=10)
    count_entry.grid(row=1, column=1, padx=10, pady=10)

    # 时间间隔输入框
    tk.Label(root, text="时间间隔(秒):").grid(row=2, column=0, padx=10, pady=10)
    interval_entry = tk.Entry(root, width=10)
    interval_entry.grid(row=2, column=1, padx=10, pady=10)

    # 开始按钮
    def start_sending():
        message = message_entry.get()
        try:
            count = int(count_entry.get())
            interval = float(interval_entry.get())
        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字作为次数和时间间隔！")
            return

        send_wechat_messages(message, count, interval)

    tk.Button(root, text="开始发送", command=start_sending).grid(row=3, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_ui()
'''

'''
#5 第五版 完善了UI自适应，按钮可跟随用户拖动窗口变化

import pyautogui
import pyperclip
import time
import tkinter as tk
from tkinter import messagebox

# 模拟在微信窗口中发送消息
def send_wechat_messages(message, count, interval):
    if not message or count <= 0 or interval < 0:
        messagebox.showerror("错误", "请输入有效的消息、次数和时间间隔！")
        return

    messagebox.showinfo("提示", "请在5秒内将光标放置在微信的聊天输入框...")
    time.sleep(5)  # 给用户时间将光标放到输入框

    for i in range(count):
        pyperclip.copy(message)  # 将消息复制到剪贴板
        pyautogui.hotkey("ctrl", "v")  # 粘贴消息
        pyautogui.press("enter")  # 模拟按下回车键发送消息
        print(f"第 {i + 1} 条消息已发送：{message}")
        time.sleep(interval)  # 间隔指定的时间发送下一条消息

    messagebox.showinfo("完成", "消息发送完成！")

# 创建主界面
def create_ui():
    root = tk.Tk()
    root.title("消息轰炸小程序")
    root.geometry("400x200")  # 初始窗口大小

    # 设置网格的行和列扩展权重
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    root.grid_columnconfigure(1, weight=1)

    # 消息输入框
    tk.Label(root, text="要发送的消息:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    message_entry = tk.Entry(root)
    message_entry.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    # 次数输入框
    tk.Label(root, text="发送的次数:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    count_entry = tk.Entry(root)
    count_entry.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    # 时间间隔输入框
    tk.Label(root, text="时间间隔(秒):").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    interval_entry = tk.Entry(root)
    interval_entry.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

    # 开始按钮
    def start_sending():
        message = message_entry.get()
        try:
            count = int(count_entry.get())
            interval = float(interval_entry.get())
        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字作为次数和时间间隔！")
            return

        send_wechat_messages(message, count, interval)

    tk.Button(root, text="开始发送", command=start_sending).grid(row=3, column=0, columnspan=2, pady=10, sticky="nsew")

    root.mainloop()

if __name__ == "__main__":
    create_ui()

'''

import pyautogui
import pyperclip
import time
import tkinter as tk
from tkinter import messagebox

# 模拟在微信窗口中发送消息
def send_wechat_messages(message, count, interval):
    if not message or count <= 0 or interval < 0:
        messagebox.showerror("错误", "请输入有效的消息、次数和时间间隔！")
        return

    messagebox.showinfo("提示", "请在5秒内将光标放置在微信的聊天输入框...")
    time.sleep(5)  # 给用户时间将光标放到输入框

    for i in range(count):
        pyperclip.copy(message)  # 将消息复制到剪贴板
        pyautogui.hotkey("ctrl", "v")  # 粘贴消息
        pyautogui.press("enter")  # 模拟按下回车键发送消息
        print(f"第 {i + 1} 条消息已发送：{message}")
        time.sleep(interval)  # 间隔指定的时间发送下一条消息

    messagebox.showinfo("完成", "消息发送完成！")

# 创建主界面
def create_ui():
    root = tk.Tk()
    root.title("消息轰炸小程序")
    root.geometry("400x200")  # 初始窗口大小

    # 设置网格的行和列扩展权重
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    root.grid_columnconfigure(1, weight=1)

    # 消息输入框
    tk.Label(root, text="要发送的消息:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    message_entry = tk.Entry(root)
    message_entry.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    # 次数输入框
    tk.Label(root, text="发送的次数:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    count_entry = tk.Entry(root)
    count_entry.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    # 时间间隔输入框
    tk.Label(root, text="时间间隔(秒):").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    interval_entry = tk.Entry(root)
    interval_entry.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

    # 开始按钮
    def start_sending():
        message = message_entry.get()
        try:
            count = int(count_entry.get())
            interval = float(interval_entry.get())
        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字作为次数和时间间隔！")
            return

        send_wechat_messages(message, count, interval)

    tk.Button(root, text="开始发送", command=start_sending).grid(row=3, column=0, columnspan=2, pady=10, sticky="nsew")

    root.mainloop()

if __name__ == "__main__":
    create_ui()
