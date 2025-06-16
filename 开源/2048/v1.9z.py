

'''
import os
import subprocess

def open_image(image_path):
    # 检查文件是否存在
    if os.path.exists(image_path):
        # 使用系统默认程序打开图片
        subprocess.Popen([image_path], shell=True)
    else:
        print(f"文件 {image_path} 不存在。")

if __name__ == "__main__":
    # 定义图片路径，这里指定文件夹路径
    folder_path = r"D:\Python Files\2048"  # 替换为你的文件夹路径
    image_name = "4.png"
    image_path = os.path.join(folder_path, image_name)

    # 打开图片
    open_image(image_path)
'''
'''


import os
import subprocess
import tkinter as tk
from tkinter import filedialog


def open_image(image_path):
    # 检查文件是否存在
    if os.path.exists(image_path):
        subprocess.Popen([image_path], shell=True)
    else:
        print(f"文件 {image_path} 不存在。")


def select_file():
    # 创建一个隐藏的 Tk 窗口
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    # 打开文件对话框，选择文件
    file_path = filedialog.askopenfilename(title="选择要打开的文件",
                                           filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])

    if file_path:  # 如果用户选择了文件
        open_image(file_path)


if __name__ == "__main__":
    select_file()
'''

import os
import subprocess
import tkinter as tk
from tkinter import messagebox

def open_image(image_path):
    # 检查文件是否存在
    if os.path.exists(image_path):
        subprocess.Popen([image_path], shell=True)
    else:
        messagebox.showerror("错误", f"文件 {image_path} 不存在。")

def on_open_image():
    # 定义图片路径，这里指定文件夹路径
    folder_path = r"D:\Python Files\2048"  # 替换为你的文件夹路径
    image_name = "4.png"
    image_path = os.path.join(folder_path, image_name)

    # 打开图片
    open_image(image_path)

# 创建主窗口
root = tk.Tk()
root.title("打开图片")

# 创建按钮
open_button = tk.Button(root, text="打开 4.png", command=on_open_image)
open_button.pack(pady=20)

# 运行主循环
root.mainloop()
