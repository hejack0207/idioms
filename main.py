import random
from pypinyin import lazy_pinyin

def idiom_exists(CY): 
    with open('idiom.txt','r') as f:
        for i in set(f.readlines()):
            if CY ==i.strip():
                return True
        return False

def idiom_select(x): 
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
        x = input("请输入：")
        if idiom_exists(x):
            print(idiom_select(x))
        else:
            print("不存在，结束")
            break
main()
