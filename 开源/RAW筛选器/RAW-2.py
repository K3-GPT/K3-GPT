import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from tkinter import filedialog
import os
import shutil

root = tkinter.Tk()
root.title('RAW筛选器')
max_w, max_h = root.maxsize()
root.geometry('500x300+{}+{}'.format(int((max_w - 500) / 2), int((max_h - 200) / 2)))
root.resizable(width=False, height=False)

def main(directory, suffix):
    # 在用户选中的目录下创建回收站文件夹
    RECYCLE_BIN = os.path.join(directory, "回收站")  # 在用户选定的目录下创建回收站文件夹
    if not os.path.exists(RECYCLE_BIN):
        try:
            os.makedirs(RECYCLE_BIN)  # 创建文件夹
            print(f"{RECYCLE_BIN} 文件夹已创建")
        except Exception as e:
            print("创建文件夹失败:", e)

    filename_counts = {}
    S = 0

    # 遍历用户选中的目录中的所有文件
    for filename in os.listdir(directory):
        base_filename = os.path.splitext(filename)[0]
        if base_filename in filename_counts:
            filename_counts[base_filename] += 1
        else:
            filename_counts[base_filename] = 1

    # 处理删除文件的逻辑
    for filename, count in filename_counts.items():
        if count == 1:
            new_filename = filename + suffix
            file_path = os.path.join(directory, new_filename)
            if os.path.exists(file_path):
                # 将文件移动到回收站文件夹
                shutil.move(file_path, os.path.join(RECYCLE_BIN, new_filename))  # 移动到回收站
                S += 1

    print(f"已移动 {S} 张文件到 {RECYCLE_BIN}")
    return S

#筛选精修
def choose(path, opath):
    # path  存放 未筛选 的文件夹
    # opath 存放 筛选后 的文件夹

    # Define a dictionary to store file names and file paths
    # 定义一个字典来存储文件名和文件路径
    filename_counts = {}
    S = 0

    # Traverse the directory and store file names and file paths in the dictionary
    # 遍历目录并将文件名和文件路径存储在字典中
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_name = os.path.splitext(file)[0]
            if file_name in filename_counts:
                filename_counts[file_name].append(file_path)
                print(file_name)
            else:
                filename_counts[file_name] = [file_path]

    # Create a new directory to store duplicate files
    # 创建新目录以存储重复文件
    if not os.path.exists(opath):
        os.mkdir(opath)

    # Copy duplicate files to the new directory
    # 将重复文件复制到新目录
    for key in filename_counts:
        if len(filename_counts[key]) > 1:
            for file_path in filename_counts[key]:
                shutil.copy2(file_path, opath)
                S += 1
    print("复制了", S, "张")
    return S

def get_path():
    """注意，以下列出的方法都是返回字符串而不是数据流"""
    # 返回一个字符串，且只能获取文件夹路径，不能获取文件的路径。
    path = filedialog.askdirectory(title='请选择一个目录')
    # entry_text.set(path)
    dr = str(path)
    return dr

def get_content():
    suffix = number_int_var.get()
    path = get_path()
    supported_formats = {'.CR3', '.CR2', '.JPG', '.ARW', '.NEF', '.NRW',
                         '.RW2', '.RAW', '.DNG', '.orf', '.raf', '.SRW',
                         '.PEF', '.IQ', '.3FR'}

    if suffix in supported_formats:
        title = main(path, suffix)
        tk.messagebox.showinfo(title='温馨提示', message=f'已删除{title}张{suffix}文件')
    else:
        tk.messagebox.showinfo(title='温馨提示', message=f'不支持的文件格式：{suffix}')

def get_content2():
    path = get_path()
    opath = get_path()
    title = choose(path, opath)
    tk.messagebox.showinfo(title='温馨提示', message='已复制{}张'.format(title))  # type: ignore


# root.geometry('367x134+200+200')
#  透明度的值:0~1 也可以是小数点，0：全透明；1：全不透明
root.attributes("-alpha", 1.0)
# -------------------------------------------------------
# tk.Label(root, text='删除多余文件', font=('黑体', 13), fg="red").grid(row=0, column=1)
# -------------------------------------------------------
text_label_1 = tk.Label(root, text='格式选择: ', font=('黑体', 15))
text_label_1.place(x=50, y=50)
# -------------------------------------------------------
number_int_var = tk.StringVar()
# 创建一个下拉列表
numberChosen = ttk.Combobox(root, textvariable=number_int_var, width=26)
# 设置下拉列表的值
numberChosen['values'] = ('.CR3', '.CR2', '.JPG', '.ARW', '.NEF', '.NRW', '.RW2', '.RAW', '.DNG', '.orf', '.raf', '.SRW', '.PEF', '.IQ', '.3FR')
# 设置其在界面中出现的位置  column代表列   row 代表行
# numberChosen.grid(row=1, column=1, padx=5, pady=5)
numberChosen.place(x=150, y=52.5)
# 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
numberChosen.current(0)

text_label_2 = tk.Label(root, text='·去除废片：把保留的jpg放到有raw的文件夹内，然后选中这个文件夹，会自动删掉不要的raw。', font=('黑体', 8))
text_label_2.place(x=50, y=100)
text_label_2 = tk.Label(root, text='·筛选精修：把要修的jpg放到有raw的文件夹内，然后选中这个文件夹，再选一个你要放精修的新文件夹，会自动', font=('黑体', 8))
text_label_2.place(x=50, y=120)
text_label_2 = tk.Label(root, text='                   会自动把要修的raw单独拷贝到新文件夹。', font=('黑体', 8))
text_label_2.place(x=50, y=140)
text_label_2 = tk.Label(root, text='本操作不可逆，请备份好原文件！', font=('黑体', 15, 'bold'), fg='red')
text_label_2.place(x=145, y=15)
text_label_2 = tk.Label(root, text='（注：文件夹内禁止这两种格式以外的文件，并且jpg必须 <= raw的数量。）', font=('黑体', 8))
text_label_2.place(x=105, y=260)
# -------------------------------------------------------



Button_1 = tk.Button(root, text='去除废片',  command=get_content)
Button_1.place(x=120, y=200)
Button_1.config(width=10, height=2)
Button_2 = tk.Button(root, text='筛选精修',  command=get_content2)
Button_2.place(x=250, y=200)
Button_2.config(width=10, height=2)

root.mainloop()
