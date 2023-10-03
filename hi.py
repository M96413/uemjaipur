
#CLOCK WITH GREATING

name = input("Enter Your Name: ").title()

import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)
timestamp1 = int(time.strftime("%H"))
print(timestamp1)
timestamp2 = int(time.strftime("%M"))
print(timestamp2)
timestamp3 = int(time.strftime("%S"))
print(timestamp3)

if 4 <= timestamp1 < 12:
    print(timestamp,"AM GOOD MORNING",name)
elif 12 <= timestamp1 <15:
    print(timestamp,"PM GOOD AFTERNOON",name)
elif 15 <= timestamp1 <21:
    print(timestamp,"PM GOOD EVENING",name)
elif 21 <= timestamp1 < 0  . union(0 , 4):
    print(timestamp,"PM GOOD NIGHT",name)
else:
    print("Something Went Wrong")

