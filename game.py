import random
print('Number Guessing Game by - punit42')
print()
name = input('Enter your name = ')
win = random.randint(1,100)
user = int(input('Guess the number between (1/100) = '))
guess = 1
while True:
    if win == user:
        print()
        print(f'Congratulation "{name}"')
        print(f'Hurrrrrraayyy youuuuu winnnn in "{guess}" attempts.')
        break
    else:
        if win > user:
            print('Your number is too low')
            user = int(input('Guess again = ')) 
            guess += 1
        else:
            print('Your number is too high')
            user = int(input('Guess again = '))
            guess += 1

print()
input('Press enter to exit')
exit()