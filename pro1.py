import random

print ("Guess my number")
cno=random.randint(1,100)

low=1
high=100

uwon=False
cwon=False

while not uwon and not cwon:

    ug=int(input("guess my number (1-100):  "))
    if ug==cno:
        print("your guess is correc! you won!")
        uwon=True
    elif ug<cno:
        print("higher!")
    else:
        print("lower!")

    if uwon:
        break

    cg = (low + high) // 2
    
    print(f"computer guess: {cg}")

    rep=input("is the no. is high, low, or correct? (h/l/c): ")

    if rep=='c':
        print("computer guess your no.!")
        cwon=True
    elif rep=='h':
        low=cg+1
    elif rep=='l':
        high=cg-1
