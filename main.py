import random
from pypinyin import lazy_pinyin
import fire

def _idiom_exists(CY): 
    with open('idiom.txt','r') as f:
        for i in set(f.readlines()):
            if CY ==i.strip():
                return True
        return False

def _idiom_select(x): 
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

def shou_wei_zi(): 
    sz = dict()
    wz = dict()
    with open('idiom.txt','r') as f:
        for l in set(f.readlines()):
            s,w = l[0],l[-2]
            if s in sz:
                sz[s]=sz[s]+1
            else:
                sz[s]=1
            if w in wz:
                wz[w]=wz[w]+1
            else:
                wz[w]=1

        sz_sorted = sorted(sz.items(), key=lambda i:i[1]) 
        wz_sorted = sorted(wz.items(), key=lambda i:i[1]) 
        for k,v in sz_sorted:
            print("{0:s},{1:d}".format(k,v))

        print(len(sz))
        szs,wzs=set(sz.keys()),set(wz.keys())
        print("{} in both,{} only in shouzi,{} in weizi".format(len(szs & wzs),len(szs - wzs), len(wzs - szs)))


def interactive():
    while True:
        try:
            x = input()
            if _idiom_exists(x):
                tongxing, tongyin = _idiom_select(x)
                print('\n'.join(tongxing))
            else:
                print("不存在，结束")
        except EOFError as error:
            break

def main():
    fire.Fire()

main()
