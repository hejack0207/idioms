import random
from pypinyin import lazy_pinyin

def idiom_exists(CY):  #判断成语是否存在
    with open('idiom.txt','r') as f:
        for i in set(f.readlines()):
            if CY ==i.strip():
                return True
        return False

def idiom_select(x):                               #参数为x的成语，返回该成语的接龙匹配成语
        with open('idiom.txt','r') as f:
            base = f.readlines()
            random.shuffle(base)
            for i in base:
                if i[:-1] == x or len(i) != 5:
                    continue
                if lazy_pinyin(i[0])==lazy_pinyin(x[-1]):
                    return i[:-1]

def main():
    while True:
        x = input("请输入成语：")
        if idiom_exists(x):
            print(idiom_select(x))
        else:
            print("该成语不存在，结束")
            break
main()
