# 1，下载zip包并解压

链接：[github.com](https://github.com/modelscope/FunASR)

# 2，准备工作

```python
# 1 进入文件所在位置
cd "D:\Python Files\Personal projects\FunASR-main"

# 2 安装所需要的包/依赖
pip3 install -e ./

# 3 创建虚拟环境
python -m venv funasr_env
```

```python
# 4 激活虚拟环境
funasr_env\Scripts\activate

# 在虚拟环境安装这个包(测试，未知原因)
pip install torchaudio

# 5 更改模型安装位置，下载模型，检查模型安装位置
$env:MODELSCOPE_CACHE="D:\Python Files\Personal projects\FunASR-main\models"

pip install -U modelscope

echo $env:MODELSCOPE_CACHE
```

![image-20250428235745042](png/image-20250428235745042.png)

```
# 6 在主路径下创建这个文件
from funasr import AutoModel
import soundfile
import os

# 设置模型参数
chunk_size = [0, 10, 5]  # [0, 10, 5] 表示 600ms，[0, 8, 4] 表示 480ms
encoder_chunk_look_back = 4  # 编码器自注意力回溯的块数
decoder_chunk_look_back = 1  # 解码器交叉注意力回溯的块数

# 加载 paraformer-zh-streaming 模型
model = AutoModel(model="paraformer-zh-streaming", cache_dir='D:\\Python Files\\Personal projects\\FunASR-main\\models')

# 指定音频文件路径
wav_file = os.path.join('D:\\Python Files\\Personal projects\\FunASR-main\\models\\paraformer-zh-streaming', "asr_example.wav")

# 读取音频文件
speech, sample_rate = soundfile.read(wav_file)

# 计算音频块的大小
chunk_stride = chunk_size[1] * 960  # 600ms

# 初始化缓存和总块数
cache = {}
total_chunk_num = int((len(speech) - 1) / chunk_stride) + 1

# 逐块处理音频
for i in range(total_chunk_num):
    speech_chunk = speech[i * chunk_stride:(i + 1) * chunk_stride]
    is_final = i == total_chunk_num - 1
    res = model.generate(
        input=speech_chunk,
        cache=cache,
        is_final=is_final,
        chunk_size=chunk_size,
        encoder_chunk_look_back=encoder_chunk_look_back,
        decoder_chunk_look_back=decoder_chunk_look_back
    )
    print(res)
    
    
# 7 安装模型
 python download_paraformer_zh.py 
```







