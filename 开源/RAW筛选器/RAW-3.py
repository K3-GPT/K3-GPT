import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from tkinter import filedialog
import os
import shutil

root = tk.Tk()
root.title('RAW筛选器')
max_w, max_h = root.maxsize()
root.geometry('500x300+{}+{}'.format(int((max_w - 500) / 2), int((max_h - 200) / 2)))
root.resizable(width=False, height=False)


# 回收站功能
def move_to_recycle_bin(directory, filename):
    RECYCLE_BIN = os.path.join(directory, "回收站")
    if not os.path.exists(RECYCLE_BIN):
        os.makedirs(RECYCLE_BIN)

    file_path = os.path.join(directory, filename)
    if os.path.exists(file_path):
        shutil.move(file_path, os.path.join(RECYCLE_BIN, filename))
        return True
    return False


# 文件分类功能 （完整 / 单个）
def categorize_files(directory):
    COMPLETE_FOLDER = os.path.join(directory, "完整")
    SINGLE_FOLDER = os.path.join(directory, "单个")

    if not os.path.exists(COMPLETE_FOLDER):
        os.makedirs(COMPLETE_FOLDER)
    if not os.path.exists(SINGLE_FOLDER):
        os.makedirs(SINGLE_FOLDER)

    file_pairs = {}

    for filename in os.listdir(directory):
        name, ext = os.path.splitext(filename)
        if ext.lower() in ['.jpg', '.jpeg', '.png', '.bmp']:
            file_pairs.setdefault(name, []).append(filename)
        elif ext.lower() in ['.cr3', '.cr2', '.arw', '.nef', '.nrw', '.rw2', '.raw', '.dng', '.orf', '.raf', '.srw',
                             '.pef', '.iq', '.3fr']:
            file_pairs.setdefault(name, []).append(filename)

    for name, files in file_pairs.items():
        if len(files) > 1:  # 说明有JPG和RAW
            for file in files:
                shutil.move(os.path.join(directory, file), os.path.join(COMPLETE_FOLDER, file))
        elif len(files) == 1 and files[0].lower().endswith('.jpg'):
            shutil.move(os.path.join(directory, files[0]), os.path.join(SINGLE_FOLDER, files[0]))



def main(directory, suffix):
    filename_counts = {}
    S = 0

    # 移入回收站功能
    for filename in os.listdir(directory):
        base_filename = os.path.splitext(filename)[0]
        if base_filename in filename_counts:
            filename_counts[base_filename] += 1
        else:
            filename_counts[base_filename] = 1

    for filename, count in filename_counts.items():
        if count == 1:
            new_filename = filename + suffix
            if move_to_recycle_bin(directory, new_filename):
                S += 1

    #  文件分类功能
    categorize_files(directory)
    print(f"已移动 {S} 张文件到回收站，并完成分类")
    return S


def choose(path, opath):
    filename_counts = {}
    S = 0

    # 记录文件名（去掉扩展名）对应的文件路径
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_name, ext = os.path.splitext(file)
            if file_name in filename_counts:
                filename_counts[file_name].append(file_path)
            else:
                filename_counts[file_name] = [file_path]

    # 如果目标文件夹不存在，则创建
    if not os.path.exists(opath):
        os.mkdir(opath)

    # 仅复制 RAW 文件
    raw_formats = {'.CR3', '.CR2', '.ARW', '.NEF', '.NRW', '.RW2', '.RAW',
                   '.DNG', '.ORF', '.RAF', '.SRW', '.PEF', '.IQ', '.3FR'}

    for key, files in filename_counts.items():
        if len(files) > 1:  # 说明存在 JPG 和 RAW 文件
            for file_path in files:
                _, ext = os.path.splitext(file_path)
                if ext.upper() in raw_formats:  # 仅复制 RAW 文件
                    shutil.copy2(file_path, opath)
                    S += 1

    print("复制了", S, "张RAW文件")
    return S



def get_path():
    path = filedialog.askdirectory(title='请选择一个目录')
    return str(path)


def get_content():
    suffix = number_int_var.get()
    path = get_path()
    supported_formats = {'.CR3', '.CR2', '.JPG', '.ARW', '.NEF', '.NRW',
                         '.RW2', '.RAW', '.DNG', '.orf', '.raf', '.SRW',
                         '.PEF', '.IQ', '.3FR'}

    if suffix in supported_formats:
        title = main(path, suffix)
        tk.messagebox.showinfo(title='温馨提示', message=f'已将{title}张{suffix}文件移入回收站')
    else:
        tk.messagebox.showinfo(title='温馨提示', message=f'不支持的文件格式：{suffix}')


def get_content2():
    path = get_path()
    opath = get_path()
    title = choose(path, opath)
    tk.messagebox.showinfo(title='温馨提示', message=f'已复制{title}张')


root.attributes("-alpha", 1.0)

text_label_1 = tk.Label(root, text='格式选择: ', font=('黑体', 15))
text_label_1.place(x=50, y=50)

number_int_var = tk.StringVar()
numberChosen = ttk.Combobox(root, textvariable=number_int_var, width=26)
numberChosen['values'] = (
'.CR3', '.CR2', '.JPG', '.ARW', '.NEF', '.NRW', '.RW2', '.RAW', '.DNG', '.orf', '.raf', '.SRW', '.PEF', '.IQ', '.3FR')
numberChosen.place(x=150, y=52.5)
numberChosen.current(0)

text_label_2 = tk.Label(root, text='·去除废片：把保留的jpg放到有raw的文件夹内，然后选中这个文件夹，会自动删掉不要的raw。',
                        font=('黑体', 8))
text_label_2.place(x=50, y=100)
text_label_2 = tk.Label(root,
                        text='·筛选精修：把要修的jpg放到有raw的文件夹内，然后选中这个文件夹，再选一个你要放精修的新文件夹，会自动',
                        font=('黑体', 8))
text_label_2.place(x=50, y=120)
text_label_2 = tk.Label(root, text='                   会自动把要修的raw单独拷贝到新文件夹。', font=('黑体', 8))
text_label_2.place(x=50, y=140)
text_label_2 = tk.Label(root, text='本操作不可逆，请备份好原文件！', font=('黑体', 15, 'bold'), fg='red')
text_label_2.place(x=145, y=15)
text_label_2 = tk.Label(root, text='（注：文件夹内禁止这两种格式以外的文件，并且jpg必须 <= raw的数量。）', font=('黑体', 8))
text_label_2.place(x=105, y=260)

Button_1 = tk.Button(root, text='去除废片', command=get_content)
Button_1.place(x=120, y=200)
Button_1.config(width=10, height=2)
Button_2 = tk.Button(root, text='筛选精修', command=get_content2)
Button_2.place(x=250, y=200)
Button_2.config(width=10, height=2)

root.mainloop()
