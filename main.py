import random
from pypinyin import lazy_pinyin

#tongyin=[]
#tongxing=[]

def idiom_exists(CY): 
    with open('idiom.txt','r') as f:
        for i in set(f.readlines()):
            if CY ==i.strip():
                return True
        return False

def idiom_select(x): 
    tongyin=[]
    tongxing=[]
    with open('idiom.txt','r') as f:
        base = f.readlines()
        random.shuffle(base)
        for i in base:
            if i[:-1] == x:
                continue
            if i[0]==x[-1]:
                tongxing.append(i[:-1])
                continue
            if lazy_pinyin(i[0])==lazy_pinyin(x[-1]):
                tongyin.append(i[:-1])
    return tongxing, tongyin

def main():
    while True:
        x = input("请输入：")
        if idiom_exists(x):
            tongxing, tongyin = idiom_select(x)
            print('\n'.join(tongxing))
        else:
            print("不存在，结束")
            break
main()
