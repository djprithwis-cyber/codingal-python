print("===========")
print("smart school planer")
print("===========")
whether = int(input("put the the whether (use 1 to 10 to tell how bad the whether is)"))
day = (input("tell the day ( sunday to saterday)"))
homework_status = (input("status of your homework"))
print("=======")
print("FILE")
print("=======")
print(f"=== the day is{day}")
if day in ("saturday","sunday"):
    print("enjoy your weekend")
elif day in ("monday"):
    print("it is the beginning of the week")
elif day in ("friday"):
    print("last day of the day of the week")
elif day in ("tuesday","wednesday","thursday"):
    print("it is the middle of the week (normal school day)")
else: 
    print("error 404(not found day)")
    






