# # try-except
# 程式異常 一個除數為0的錯誤
def division(x, y):
    try:  # tr-except指令
        return x / y
    except ZeroDivisionError:  # 除數為0時執行
        print("除數不可為0")


print(division(10, 2))  # 列出10/2
print(division('a', 'b'))  # 列出'a'/'b'
print(division(6, 3))  # 列出6/3
