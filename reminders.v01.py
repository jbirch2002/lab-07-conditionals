
current_hour = float(input("Enter the current hour in military time (0-23): "))

if 0 <= current_hour < 5:
    print("It’s early. You should be sleeping!")
elif 5 <= current_hour < 7:
    print("Wake up, brew that coffee, get that mile run in, and get that breakfast…")
elif 7 <= current_hour < 9:
    print("Time to go to work.")
elif 9 <= current_hour < 12:
    print("You should be working!")
elif 12 <= current_hour < 13:
    print("Take your lunch break!")
elif 13 <= current_hour < 17:
    print("Do you feel that afternoon lull?")
elif 17 <= current_hour < 19:
     print("Time to hit the gym…")
elif 19 <= current_hour < 21:
    print("Gotta eat that dinner.")
elif 21 <= current_hour <= 23:
    print("Get that SLEEP. And rePEAT!")
else:
     print("You didn’t type an acceptable value! (0-23)")
