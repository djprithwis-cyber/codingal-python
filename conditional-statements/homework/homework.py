age = (input("Put your age: "))
import time
print("loding")
time.sleep(2)
pay=(input("pay elry( say yes no)"))
time.sleep(2)
print("===============")
print("chart")
print("===============")
print("notice")
print("if it is a infant then it is a 4 digit code but a child  or teennager 5 digit if aduilt it is a 6 to 7  didit code ")
print("you can pass on to payment")
if age <= 5:
    print("you are inf(infan) pass")
    print("code:1734")
elif age <=8:
    print("child(mid shallow water)")
    print("code 29563")
elif age <=13:
    print("midchild. (shllowdeep water)")
elif age <=14:
    print("teenager(deep waters(if parrent permition))")
    print("code:18365")

elif age <= 18:
    print("aduilt (any pool)")
    print("code:9283613")
else:
    print("404(not found (try typing numbers in the age (pis restart to play this game agine)))")
if pay == "yes":
    print("Payment done erly")
else:
    paynow = input("Would you like to pay now? (yes/no): ")
print("done! Wait here so we can check if you actually paid or not")
