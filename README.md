# trans-bot
## Introduction
嗷呜编码~

## Usage

```python
# 待编码字符串
s1 = "我爱北京天安门,天安门上太阳升~"
s2 = "https://github.com/LeapSpace"
# 使用默认字符集
bot = LangBot()
# 编码
res = bot.encode(s1)
print(res)
# 解码
print(bot.decode(res))
# 使用自定义字符集
# 第一个参数是使用的编码字符集，第二个参数是补全位使用的字符
bot1 = LangBot(['哈', '嘿', '嘻'], '!')
# 编码
res1 = bot1.encode(s2)
print(res1)
# 解码
print(bot1.decode(res1))
```

