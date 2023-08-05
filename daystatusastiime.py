import time
timestamp = time.localtime()
timing = timestamp.tm_hour
print(timing)
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