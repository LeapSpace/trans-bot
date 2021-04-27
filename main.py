#!/usr/bin/python3
# coding=utf-8
#
# @author Space
# @date 2021/4/26 18:00

def _get_len(base: int) -> int:
    for i in range(9):
        if base ** i >= 256:
            return i
    return 8


class LangBot:
    char_set = ["嗷", "呜"]
    just_char = '~'
    base = len(char_set)
    n_length = _get_len(base)

    def __init__(self, char_set=None, just_char=None):
        if char_set is not None:
            self._char_set = list(set(char_set))
        else:
            self._char_set = list(set(LangBot.char_set))
        sorted(self._char_set)
        self._base = len(self._char_set)
        if self._base < 2:
            raise Exception("char set size must be bigger than 2")
        if self._base > 256:
            raise Exception("char set size must be less than 256")
        if just_char is not None:
            self._just_char = just_char
        else:
            self._just_char = LangBot.just_char
        if len(self._just_char) > 1:
            raise Exception("just char size must be 1")
        self._n_length = _get_len(self._base)

    def _base_n(self, num: int) -> str:
        """
        十进制 转 self._base进制
        :param num: 十进制数
        :return:
        """
        return ((num == 0) and self._char_set[0]) or \
               (self._base_n(num // self._base).lstrip(self._char_set[0]) + self._char_set[num % self._base])

    def encode(self, txt: str) -> str:
        if txt is None or txt == "":
            return ""
        _res = []
        bys = txt.encode("utf-8")
        for b in bys:
            _res.append(self._base_n(b).ljust(self._n_length, self._just_char))
        return ''.join(_res)

    def decode(self, txt: str) -> str:
        if txt is None or txt == "":
            return ""
        t = len(txt) % self._n_length
        if t != 0:
            txt = txt.ljust(len(txt) + (self._n_length - t), self._just_char)
        table = {}
        i = 0
        for v in self._char_set:
            table[v] = i
            i = i + 1
        result = bytearray()
        for i in range(0, len(txt), self._n_length):
            tmp = txt[i:i + self._n_length].strip(self._just_char)
            _res = 0
            _l = len(tmp)
            for j in range(_l):
                _res += table[tmp[_l - j - 1]] * (self._base ** j)
            result.append(_res)
        return result.decode("utf-8")


if __name__ == '__main__':
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
