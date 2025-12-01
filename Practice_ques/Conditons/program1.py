#----program to greet based on time using time module
import time
timestamp =time.strftime("%H:%M:%S")
numeric = int(timestamp.replace(":",""))
print(numeric)
print(type(numeric))
time = int(input("Enter your time "))
if numeric>=8 and numeric<12:
    print("good morning")
elif numeric>=12 and numeric<1:
    print("good afternoon")
elif numeric>=17 and numeric<20:
    print("good evening")
else:
    print("good night")