import random

random_number = random.randint(1, 1000)
count = 1
while count != -1:
    guessing_number = int(input('Enter a number between 1 to 1000: '))
    if guessing_number == -99:
        break
    elif guessing_number > random_number:
        print(f'number too high {random_number}')
    elif guessing_number < random_number:
        print(f'number too low {random_number}')
    else:
        print('CONGRATULATION YOU GUESSED RIGHT')
        sentinel = int(input("Enter number 1 to try again: "))
        if sentinel != 1:
            break
        elif sentinel == -99:
            break
        if count < 10:
            print('you know the secret or you got lucky')
        elif count > 10:
            print('You should be able to do better!')
        elif count == 10:
            print('Aha!!!, you know the secret')
            count = count + 1
print(f'{count}')
