# 使用python硬功夫搜尋文字
def taiwanPhoneNum(string):
    """檢查是否有含手機聯絡資訊的台灣手機號碼格式"""
    if len(string) != 12:  # 如果長度不是12
        return False  # 傳回非手機號碼格式

    for i in range(0, 4):  # 如果前4個字元出現非數字字元
        if string[i].isdecimal() == False:  # isdecimal()方法檢查字符串是否僅由十進製字符組成。
            return False  # 傳回非手機號碼格式

    if string[4] != '-':  # 如果不是'-'字元
        return False  # 傳回非手機號碼格式

    for i in range(5, 8):  # 如果中間3個字出現非數字字元
        if string[i].isdecimal() == False:
            return False  # 傳回非手機號碼格式

    if string[8] != '-':  # 如果不是'-'字元
        return False  # 傳回非手機號碼格式

    for i in range(9, 12):  # 如果後面3個字出現非數字字元
        if string[i].isdecimal() == False:
            return False  # 傳回非手機號碼格式
    return True  # 通過以上測試


print("I love Ming-Chi:是台灣手機號碼", taiwanPhoneNum('I love Ming-Chi'))
print("0932-999-199:   是台灣手機號碼", taiwanPhoneNum("0932-999-199"))
