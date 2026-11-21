import time

x = 5

if (type(x) is int):
    time.sleep(2)
    print("true")
else:
    print("false")
x = 5.5
if (type(x) is not float):
    print("true")
else:
    print("false")
x = 20
y = 20
if (x is y):
    print("x and y same identy")
y = 30 
if (x is not y):
    print("x amd y have diffrent identy")
