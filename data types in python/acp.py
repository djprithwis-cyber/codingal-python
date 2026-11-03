goal = input("Write your goal here")
name = input("what is your name")
print(goal)
plan1 = "Practice every day"
plan2 = "pratice every 2 days"
plan3 = "pratice every 3 days"
daily_min = 30
print("==========")
print("your goal")
print("==========")
print("name:",name)
print("goal:",goal)
print("daily mins",daily_min)
import random

chosen_plan = random.choice([plan1, plan2, plan3])
print(chosen_plan) # this is a littel help from the ai in vs code 
