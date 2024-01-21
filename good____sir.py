import time
t=int(time.strftime('%H'))
if(t<12):
    print("Good Morning\n")
elif(t>=12 and t <17):
    print("good afternoon\n")
elif(t>=17 and t<19):
    print("Good evening\n")
else:
    print("Good Night\n")