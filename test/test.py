mins = int(input("Enter a number: "))
print("===================")
print("homework details ")
print("===================")
if mins >= 60:
    print("long term homework!")
elif mins >= 30:
    print("medium homework")
else:
    print("short term homework!")