import sys
import time

print("welcome to airport")
print("=========")
print("")
print("sign in ")
passport = input("show your passport")
if passport == "no":
    print("sorry show passport to begun")
    passport = input("yes or no(passport)")
    if passport == "no":
        print("sorry restart the game ")
        sys.exit()
    elif passport == "yes":
        print("you can go ")
    else:
        print("eroor code yn1383")
        sys.exit()
elif passport == "yes":
    print("you can go ")
else:
    print("please answer yes or no")
    sys.exit()
destination = input("where do you want to go(london,paris)")
state = input("economy, pre economy, Business, first,wich one ")
print("loding(plese wait)")
time.sleep(2)
print("checking your passport")
time.sleep(2)
print("printing your passport")
time.sleep(2)
print("done")
print("--------------")
print("")
print("")
print("=========")
print("=.......=")
print("=.......=")
print("=.......=")
print("")
print("hello let me see you passport")
yes_no = (input("yes or no"))
if yes_no == "no":
    print("please restart the game")
    sys.exit()
elif yes_no != "yes":
    print("please answer yes or no")
    sys.exit()
