import random
win=0
print("Welcome to my number guessing game. Please choose your difficulty level between easy, medium and difficult.You even have the choice for your own custom difficulty")
while True:
    diff=input()
    if diff=="easy":
        tries=7
        guess=random.randint(0,25)
        print("the range is between 0 and 25")
    elif diff=="med":
        tries=9
        guess=random.randint(0,100)
        print("the range is between 0 and 100")
    elif diff=="hard":
        tries=15
        guess=random.randint(0,1000)
        print("the range is between 0 and 1000")
    elif diff=="custom":
        tries=25
        low=input("enter lower range value")
        high=input("enter higher range value")
        print(f"the range is between {low} and {high}")
        low=int(low)
        high=int(high)
        guess=random.randint(low,high)
    while tries>0:
        userguess=int(input("-"))
        if diff=="easy":
            if userguess>25 or userguess<0:
                print("out of bounds bro")
                print(tries)
                continue
            elif userguess>guess:
                print("go lower")
                tries=tries-1
                print(tries)
                continue
            elif userguess<guess:
                print("go higher")
                tries=tries-1
                print(tries)
                continue
            elif userguess==guess:
                win=win+1
                print("Congratulations! You won")
                break
        elif diff=="med":
            if userguess>100 or userguess<0:
                print("out of bounds bro")
                print(tries)
                continue
            elif userguess>guess:
                print("go lower")
                tries=tries-1
                print(tries)
                continue
            elif userguess<guess:
                print("go higher")
                tries=tries-1
                print(tries)
                continue
            elif userguess==guess:
                win=win+1
                print("Congratulations! You won")
                break
        elif diff=="hard":
            if userguess>1000 or userguess<0:
                print("out of bounds bro")
                print(tries)
                continue
            elif userguess>guess:
                print("go lower")
                tries=tries-1
                print(tries)
                continue
            elif userguess<guess:
                print("go higher")
                tries=tries-1
                print(tries)
                continue
            elif userguess==guess:
                win=win+1
                print("Congratulations! You won")
                break
        elif diff=="custom":
            if userguess>high or userguess<low:
                print("out of bounds bro you legit chose it")
                print(tries)
                continue
            elif userguess>guess:
                print("go lower")
                tries=tries-1
                print(tries)
                continue
            elif userguess<guess:
                print("go higher")
                tries=tries-1
                print(tries)
                continue
            elif userguess==guess:
                win=win+1
                print("Congratulations! You won")
                break
    if win==0:
        print("You lost. Restart to try again.")
    else:
        print(f"you had {tries} tries left")