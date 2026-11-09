Teem1 = 120
teem2 = 180
teem3 = 239
teem4 = 290
total = Teem1 + teem2 + teem3 + teem4
avg = total / 5
print("total points :",total)
print("avg per teem",avg)
stars_per_point = 2
reward = total * stars_per_point
print("total rewards stars ",reward)
boxes = reward // 25
leftover = reward % 25
print("full box packed",boxes)
print("leftover stars",leftover)
last_week = 500
print("better than last week",total > last_week)
print("same as last week",total == last_week)
print("at lest as good?",total >= last_week)
total += 15
print("after bonus point",total) 
total -=15
print("after missed tasks:",total)
reward = total * stars_per_point
boxes = reward // 25 
print("final boxes packed:",boxes)


