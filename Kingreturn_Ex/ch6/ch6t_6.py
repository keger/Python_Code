# 重新設計 ch6_40.py 增加平均欄位
sc = [['洪錦魁', 80, 95, 88, 0, 0], ['洪冰儒', 98, 97, 96, 0, 0]]
sc[0][4] = sum(sc[0][1:4])
sc[1][4] = sum(sc[1][1:4])
sc[0][5] = round(sc[0][4] / 3, 1)
sc[1][5] = round(sc[1][4] / 3, 1)
print(sc[0])
print(sc[1])
