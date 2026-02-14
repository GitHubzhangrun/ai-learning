import os
from openai import OpenAI

# 创建与AI大模型交互的客户端对象（DEEPSEEK_API_KEY环境变量的名字，值就是DeepSeek的API_KEY的）
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

# 与AI大模型进行交互（参数）
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一名ai生活助理，你叫小花，今年1岁啦，请用温柔的语气跟我交流。"},
        {"role": "user", "content": "我是一名男生，30岁，身高175，体重69KG，目前有半年健身基础，目标想在2026年12月31日增肌到75Kg，请你为我做一套三分化训练计划，谢谢。"},
    ],
    stream=False
)

# 输出大模型返回的结果
print(response.choices[0].message.content)