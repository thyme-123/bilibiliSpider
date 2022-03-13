import os


def char(st):  # 将字符串转换为cmd可用形式
    chars = ["/", "&", "%", "^", " ", "<", ">", "'","|","\\","?","*",":","\"" ]  # 敏感字符列表
    for char in chars:
        st = st.replace(char, "")
    return st

def changeAV(av):
    table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
    tr = {}
    for i in range(58):
        tr[table[i]] = i
    s = [11, 10, 3, 8, 4, 6]
    xor = 177451812
    add = 8728348608
    av = (av ^ xor) + add
    r = list('BV1  4 1 7  ')
    for i in range(6):
        r[s[i]] = table[av // 58 ** i % 58]
    bv = ''.join(r)
    return bv

def changeBV(bv):
    table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
    tr = {}
    for i in range(58):
        tr[table[i]] = i
    s = [11, 10, 3, 8, 4, 6]
    xor = 177451812
    add = 8728348608
    r = 0
    for i in range(6):
        r += tr[bv[s[i]]] * 58 ** i
    return (r - add) ^ xor

def removeDir(pa):
    if os.path.isfile(pa):
        os.remove(pa)
        return True
    paths=os.listdir(pa)
    for path in paths:
        removeDir(pa+os.sep+path)
    os.rmdir(pa)
    return True