from random import randint
def get_number():
    while True:
        Num = int(input("Please enter a number between 1-10:"))
        if 1<=Num<=10:
            return Num
        else:
            print('Number invalid, try again')

Num = get_number()
print("You chose", Num,"!")

Rando = randint(1,10)

if Num == Rando:
    print("You got the number!!")
else:
    print("Try again the number was", Rando)
