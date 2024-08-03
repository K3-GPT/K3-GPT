import tkinter as tk  #导入标准GUI库
import time             #导入时间戳
import pickle           #保存、加载数据包
import os               #交互模块（按钮）

class Stopwatch:
    def __init__(self, root):
        self.root = root                         #传参：将传递给 __init__ 方法的 root 对象（即主窗口实例）保存到 self.root 实例变量中。
        self.root.title("秒表")                  #窗口名称
        self.root.geometry("500x350")  # 设置初始窗口大小

        # 配置网格布局以支持动态调整
        self.root.grid_rowconfigure(0, weight=1)  #设置第0行的权重为2
        self.root.grid_rowconfigure(1, weight=1)  #第1行的权重为1   ("开始"，"暂停"，"重置"按钮的 行高 )
        self.root.grid_rowconfigure(2, weight=1)  #第2行的权重为1  ("开始"按钮 和 "设置时间"按钮的 间隔行高 )
        self.root.grid_rowconfigure(3, weight=1) #第3行的权重为1  ("设置时间"按钮 和"输入时间" 输入行的 间隔行高 )
        self.root.grid_rowconfigure(4, weight=1) #第4行的权重为1  ("输入时间" 输入行 和"窗口"按钮的 间隔行高 )
        self.root.grid_columnconfigure(0, weight=1)  # 第 0 列的 权重为1 ("开始"按钮的列宽)
        self.root.grid_columnconfigure(1, weight=1) #  第1列的 权重为1 ("暂停"按钮的列宽)
        self.root.grid_columnconfigure(2, weight=1) #  第2列的 权重为1 ("重置"按钮的列宽)

        # 选择层级的下拉菜单
        self.level_var = tk.StringVar(value="窗口")        # StringVar 是 Tkinter 提供的一个变量类，用于存储和管理字符串值，关联下拉菜单的当前选择。
        self.level_menu = tk.OptionMenu(root, self.level_var, "桌面底部", "窗口顶部", "全屏", "窗口", command=self.set_window_level)        #创建一个下拉菜单，并赋值给 self.level_menu。该菜单放置在 root 窗口上，self.level_var 用于跟踪当前选中的选项，当用户选择其中一项时，调用 self.set_window_level 函数
        self.level_menu.grid(row=4, column=0, columnspan=3, pady=0, sticky="ew")
        #将创建的下拉菜单，以网格布局的方式放置：row：组件放置在第 4 行，column：组件放置在第 0 列 ，columnspan=3 组件跨越3列，pady=5 上下空出 5 像素间距，sticky="ew" 使得下拉菜单在水平方向上（东西方向）填满可用空间。
        '''
        "n": 向北（上）对齐
    "s": 向南（下）对齐
    "e": 向东（右）对齐
    "w": 向西（左）对齐
    "ns": 在上下两个方向上填满
    "ew": 在左右两个方向上填满
    "nsew": 在四个方向上都填满
        '''
        self.time_display = tk.Label(root, text="00:00:00", font=("Helvetica", 48))  #初始值为:"00:00:00"，字体大小：48
        self.time_display.grid(row=0, column=0, columnspan=3, padx=0, pady=0, sticky="nsew")  # 时间表的位置  pad x/ y：时间表的宽/长度(接受的最小窗口宽度)

        # 创建按钮并设置颜色
        self.start_button = tk.Button(root, text="开始", command=self.toggle_start_pause, bg="lightgreen")
        #command=self.toggle_start_pause 函数调用，用于切换按钮的状态，比如从“开始”切换到“暂停”  bg="lightgreen" ：按钮底纹颜色
        self.start_button.grid(row=1, column=0, sticky="nsew")

        self.pause_button = tk.Button(root, text="暂停", command=self.toggle_start_pause, bg="yellow")
        self.pause_button.grid(row=1, column=1, sticky="nsew")

        self.reset_button = tk.Button(root, text="重置", command=self.reset, bg="red")
        self.reset_button.grid(row=1, column=2, sticky="nsew")

        self.set_time_button = tk.Button(root, text="设置时间", command=self.set_time)
        self.set_time_button.grid(row=2, column=0, columnspan=3, pady=5, sticky="ew")

        #虽然没有在窗口中展现，但是是关键部分         不建议修改
        self.time_input_label = tk.Label(root, text="输入时间（hh:mm:ss）：")
        self.time_input_label.grid(row=3, column=0, columnspan=3, pady=5, sticky="ew")

        #输入框的长宽和位置         不建议修改
        self.time_input = tk.Entry(root)
        self.time_input.grid(row=3, column=1, columnspan=1, padx=5, pady=5, sticky="ew")

        #用于检测时间表是否在运行，当秒表没运作时，为False，这一段用于=>当用户点击"开始"后再次点击"开始"则暂停记时，同理，暂停键也是
        self.running = False
        self.start_time = None
        self.elapsed_time = self.load_elapsed_time()
        self.is_paused = False

        self.update_display()
        self.set_window_level(self.level_var.get())  # 初始化窗口层级，用于更新界面显示和根据当前设置调整窗口级别


    def update_display(self):       #更新界面上的时间显示
        if self.running and not self.is_paused:     #检查计时器是否 正在运行 且 未暂停。当两个条件都满足时，才进行持续的时间更新
            elapsed = time.time() - self.start_time + self.elapsed_time   #计算经过的时间=返回当前的时间戳(秒数)-计时器开始时的时间戳+已经经过的时间
            self.time_display.config(text=self.format_time(elapsed))    #更新 time_display 标签上的文本，显示格式化后的经过时间。
            self.root.after(100, self.update_display)       #设置一个定时器，每隔 100 毫秒调用一次 update_display 方法。这使得时间显示能持续更新
            # => 可以更改为更快/慢，但会更加占用CPU，数值越小占用越多
        else:
            self.time_display.config(text=self.format_time(self.elapsed_time))  # 计时器暂停，则显示当前经过时间，不再更新

    def format_time(self, seconds):     #时间进制转换，60进制
        minutes, seconds = divmod(int(seconds), 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def toggle_start_pause(self):
        if self.running:        #检查计时器是否正在运行
            if self.is_paused:      #布尔变量，指示计时器的运行状态。
                # 如果已经暂停，点击“开始”恢复计时
                self.is_paused = False      #从暂停状态恢复
                self.start_time = time.time()  #重新设置，开始新的计时周期=> 点击"重置"后的操作
                self.update_display()       #更新界面上的时间显示
                self.start_button.config(text="暂停")     #指示用户当前可暂停计时器
            else:
                # 如果正在计时，点击“开始”暂停计时
                self.is_paused = True
                self.elapsed_time += time.time() - self.start_time
                self.save_elapsed_time()
                self.start_button.config(text="继续")
        else:
            # 如果秒表没有运行，点击“开始”启动计时
            self.running = True
            self.is_paused = False
            self.start_time = time.time()
            self.update_display()
            self.start_button.config(text="暂停")
    '''
    以上代码用于：当秒表没有走时，用户点击开始后，开始走时，当再次点击"开始"后(此刻已经变为"暂停")则暂停走时，和"暂停"同样作用
    而再次点击(已变为"继续")就继续走时，同理，"暂停键"一样
    '''

    def reset(self):        #重置计时器的状态和显示内容
        self.running = False    #重置计时器第一步，确保计时器不再计时
        self.is_paused = False  #确保计时器在重置后不会进入暂停状态
        self.elapsed_time = 0   #将 elapsed_time 重置为 0：计时器经过时间被清零，为重置后重新开始计时
        self.save_elapsed_time()        #将当前的经过时间保存到持久存储中
        self.time_display.config(text="00:00:00")

        # 删除日志文件，减少存储空间，可这样容易报错，但这么小的程序，无所谓了
        if os.path.exists("elapsed_time.pkl"):
            os.remove("elapsed_time.pkl")

        # 恢复组件的文本和状态
        self.start_button.config(text="开始")
        self.time_input.delete(0, tk.END)  # 清空时间输入框

    def set_time(self):
        user_input = self.time_input.get()
        try:
            # 解析用户输入
            parts = user_input.split(':')       #就算用的是中文冒号 ： 也会自动转换为标准英文冒号
            if len(parts) != 3:
                raise ValueError("输入格式错误，应为 hh:mm:ss")  #错得太离谱才报错
            hours, minutes, seconds = map(int, parts)
            # 按照60进制进行转换
            total_seconds = hours * 3600 + minutes * 60 + seconds
            self.elapsed_time = total_seconds
            self.time_display.config(text=self.format_time(self.elapsed_time))
            self.save_elapsed_time()
        except ValueError:
            try:
                # 尝试将输入值作为60进制处理
                hours = int(user_input)
                minutes, seconds = divmod(hours, 60)
                hours, minutes = divmod(minutes, 60)
                total_seconds = hours * 3600 + minutes * 60 + seconds
                self.elapsed_time = total_seconds
                self.time_display.config(text=self.format_time(self.elapsed_time))
                self.save_elapsed_time()
            except ValueError:
                print("错误: 输入无效")

    def save_elapsed_time(self):                #save  存储当前的时间刻到elapsed_time.pkl日志文件中
        with open("elapsed_time.pkl", "wb") as f:
            pickle.dump(self.elapsed_time, f)

    def load_elapsed_time(self):                #load  读取elapsed_time.pkl日志文件中的时间刻，用于继续上次关闭的时间
        try:
            with open("elapsed_time.pkl", "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return 0

#以下用于修改窗口的层级
    def set_window_level(self, level):
        if level == "桌面底部":     #窗口不总在最上层且不全屏 => 层级在最底下，任意窗口可以覆盖
            self.root.attributes("-topmost", False)
            self.root.attributes("-fullscreen", False)  # 确保不在全屏模式
        elif level == "窗口顶部":       #窗口总在最上层且不全屏  => 层级在最上面，基本任意窗口不可覆盖
            self.root.attributes("-topmost", True)
            self.root.attributes("-fullscreen", False)  # 确保不在全屏模式
        elif level == "全屏":         #窗口全屏且总在最上层  => 全屏模式，秒表，按钮等放在最中间
            self.root.attributes("-topmost", True)
            self.root.attributes("-fullscreen", True)
        elif level == "窗口":         #窗口恢复为普通模式
            self.root.attributes("-topmost", False)
            self.root.attributes("-fullscreen", False)


#主程序
if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()