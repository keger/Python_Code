# 依鍵排序 與 遍歷字典
players = {'Stephen Curry': 'Golden State Warriors',
           'Kevin Durant': 'Golden State Warriors',
           'lebron James': 'Cleveland Cavaliers',
           'James Harden': 'Houston Rockets',
           'Paul Gasol': 'San Antonio Spurs'}
for name in sorted(players.keys()):
    print(name)
    print("Hi! %s 我喜歡看你在 %s 的表現" % (name, players[name]))
