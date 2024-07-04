import time
timestamp = time.localtime()
timing = timestamp.tm_hour
date =(timestamp.tm_mday,timestamp.tm_mon,timestamp.tm_year)

print(timing)
print(date)

if timing < 12:
    print("good morining")
elif 15>timing>12:
    print("good afternoon")
elif 21>timing>15:
    print("good evening")
elif timing>21:
    print("good night")
else:
    print("somting id wrog")