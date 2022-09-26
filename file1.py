import time
#print(dir(time))
def countdown(seconds):
    while seconds>0:
        mins= int(seconds/60)
        seconds=int(seconds%60)
        #timer=mins+":"+"seconds"
        timer = f'{mins}:{seconds}'
        print(timer)
        seconds-=1
    print("time up")
seconds=int(input("Enter the time in seconds"))
countdown(seconds)