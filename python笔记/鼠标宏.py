import pyautogui
import random
import time

# 获取屏幕的宽度和高度
screen_width, screen_height = pyautogui.size()

# 设置滑动次数
num_moves = 1000

for _ in range(num_moves):
    # 生成随机目标位置
    target_x = random.randint(0, screen_width)
    target_y = random.randint(0, screen_height)
    
    # 模拟鼠标移动到目标位置
    pyautogui.moveTo(target_x, target_y, duration=0.5)
    
    # 等待一段随机时间
    time.sleep(random.uniform(0.5, 1.5))
