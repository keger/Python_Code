# 搜尋時使用大括號設定比對次數
import re


def searchStr(pattern, msg):
    txt = re.search(pattern, msg)
    if txt == None:  # 搜尋失敗
        print("搜尋失敗", txt)
    else:  # 搜尋成功
        print("搜尋成功", txt.group())


msg5 = 'sonsonsonsonson'
pattern = '(son){3,5}?'  # 非貪婪模式
searchStr(pattern, msg5)
