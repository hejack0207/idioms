import urllib.request
import re


def get_html(url):#下载页面
    page = urllib.request.urlopen(url)
    html = page.read()
    page.close()
    return html

def get_dictionary(html): #匹配成语
    reg = "<a href=\"/cy(\d+)/(\d+).html\">(.*?)</a>"
    dic = re.compile(reg)
    html = html.decode('gbk')
    diclist = dic.findall(html)
    return diclist

def get_ItemSite():#手工把每个字母开头的页面数统计下来
    itemSite = {}#申明为空字典
    itemSite["A"] = 3
    itemSite["B"] = 21
    itemSite["C"] = 19
    itemSite["D"] = 18
    itemSite["E"] = 2
    itemSite["F"] = 14
    itemSite["G"] = 13
    itemSite["H"] = 15
    itemSite["J"] = 23
    itemSite["K"] = 6
    itemSite["L"] = 15
    itemSite["M"] = 12
    itemSite["N"] = 5
    itemSite["O"] = 1
    itemSite["P"] = 6
    itemSite["Q"] = 16
    itemSite["R"] = 8
    itemSite["S"] = 26
    itemSite["T"] = 12
    itemSite["W"] = 13
    itemSite["X"] = 16
    itemSite["Y"] = 35
    itemSite["Z"] = 21
    return itemSite

if __name__=="__main__":
    dicfile=open('./idiom.txt',"w+")
    domainsite='http://chengyu.t086.com/list/'
    itemsite = get_ItemSite()
    for key,values in itemsite.items():
        for index in range(1,values+1):
             site = key +"_"+str(index)+".html"
             print(domainsite+site)
             dictionary = get_dictionary(get_html(domainsite+site))
             for dic in dictionary:
                 dicfile.write(dic[2]+"\n")


        print(key+"字母成语抓取完毕")
    dicfile.close()
    print("全部成语抓取完毕")
