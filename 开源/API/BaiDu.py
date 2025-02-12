import requests  # 导入requests库，用于发送网络请求
import base64  # 导入base64库，用于对图片进行编码
import json  # 导入json库，用于处理json数据

'''
通用物体和场景识别并比较两张图片的相似度，同时展示识别结果 
'''

# 第一张图片的本地路径，需要修改为你的本地路径
image_path_1 = 'D:/Python Files/自制项目/钓鱼脚本/ImageDetection/image 3.png'
# 第二张图片的本地路径，需要修改为你的本地路径
image_path_2 = 'D:/Python Files/自制项目/钓鱼脚本/ImageDetection/image 7.png'


def recognize_image(image_path):
    # 二进制方式打开图片文件
    f = open(image_path, 'rb')
    img = base64.b64encode(f.read())  # 将图片内容读取出来并进行base64编码
    f.close()

    params = {"image": img}  # 构造请求参数，将编码后的图片作为参数
    access_token = '***********'  # 百度AI平台的access_token，用于认证
    request_url = "************" + "?access_token=" + access_token  # 请求的url地址
    headers = {'content-type': 'application/x-www-form-urlencoded'}  # 请求头，指定内容类型
    response = requests.post(request_url, data=params, headers=headers)  # 发送post请求
    if response:
        return response.json()  # 如果请求成功，返回json格式的响应内容
    else:
        return None  # 如果请求失败，返回None


# 识别两张图片
result_1 = recognize_image(image_path_1)  # 调用函数识别第一张图片
result_2 = recognize_image(image_path_2)  # 调用函数识别第二张图片


# 比较两张图片的识别结果
def compare_results(result_1, result_2):
    if result_1 and result_2:  # 如果两张图片都识别成功
        # 获取识别结果中的主要物体和场景及其可信度
        items_1 = {item['keyword']: item['score'] for item in result_1.get('result', [])}  # 获取第一张图片的识别结果字典
        items_2 = {item['keyword']: item['score'] for item in result_2.get('result', [])}  # 获取第二张图片的识别结果字典

        # 找出两张图片中都识别到的物体或场景
        common_items = set(items_1.keys()) & set(items_2.keys())

        # 比较可信度
        for item in common_items:  # 遍历共同识别到的物体或场景
            score_1 = items_1[item]  # 获取第一张图片中该物体或场景的可信度
            score_2 = items_2[item]  # 获取第二张图片中该物体或场景的可信度
            if score_1 >= 0.7 and score_2 >= 0.7:  # 如果两张图片中该物体或场景的可信度都大于等于0.7
                print("极为相似")  # 打印极为相似
                break  # 跳出循环
            elif score_1 >= 0.5 and score_2 >= 0.5:  # 如果两张图片中该物体或场景的可信度都大于等于0.5
                print("较为相似")  # 打印较为相似
                break  # 跳出循环
        else:  # 如果循环正常结束，即没有break
            print("不像")  # 打印不像

        # 打印识别结果
        print("\n第一张图片识别结果：")  # 打印提示信息
        for item in sorted(result_1.get('result', []), key=lambda x: x['score'], reverse=True):  # 按可信度降序排序并遍历第一张图片的识别结果
            print(f"'score': {item['score']}, 'root': '{item['root']}', 'keyword': '{item['keyword']}'")  # 打印识别结果

        # 首先 for 在字典 item 中遍历：使用.get()方法，从字典中取值，取字典中的 键 -> 列表
        # key -> 按这个依据 + lambda -> 匿名函数 = x:x['score']  以 score 为依据，进行排列，顺序(reverse)为逆序(True)
        # 使用f""方法输出信息： item['score'] -> 当前物体/场景的 可信度 item['root'] -> 当前物体/场景的 分类  item['keyword'] -> 当前物体/场景的名称

        print("\n第二张图片识别结果：")  # 打印提示信息
        for item in sorted(result_2.get('result', []), key=lambda x: x['score'], reverse=True):  # 按可信度降序排序并遍历第二张图片的识别结果
            print(f"'score': {item['score']}, 'root': '{item['root']}', 'keyword': '{item['keyword']}'")  # 打印识别结果
    else:  # 如果有图片识别失败
        print("图片识别失败")  # 打印图片识别失败


compare_results(result_1, result_2)  # 调用函数比较两张图片的识别结果