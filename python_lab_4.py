# -*- coding: utf-8 -*-
"""python lab 4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kLM0_hpOH9O9RY2Gd8X_hZDWQCtGRNHr
"""

#calc
ans = input("What is you calculations: ")
a, b, c = ans.split()


a = int(a)
c = int(c)

if b == ("+"):
  print(a + c)
elif b == ("-"):
  print(a - c)
elif b == ("*"):
  print(a * c)
elif b == ("/"):
  print(a / c)

"""A summer camp has a daily schedule. 

Between 8am-10am reading lessons

Between 10am-12pm math lessons

Between 12pm-1pm lunch time

Between 1pm-2pm music lessons



"""

# find the time and sets it into numbers i can use 
time = input("whats is the time in 24 hour format: ")
time = time.replace(":", " ") 
hour, minute = time.split()
hour = int(hour)
minute = int(minute)
deci_time = hour + (minute / 60)

if deci_time >= 8 and deci_time < 10: 
  print("reading lessons")
elif deci_time >= 10 and deci_time < 12:
  print("math lessons") 
elif deci_time >= 12 and deci_time < 13:
  print("Lunch time")
elif 13 <= deci_time <= 14:
  print("music lesson")
else:
  print("no lessons at this time")