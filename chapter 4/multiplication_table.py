def multiplication(num):
    for i in range(1, 13, 1):
        multiply = i * num
        print(f'{num} * {i} = {multiply}')


def multiplication_loop(num1, num2):
    return num1 * num2


def addition(num1, num2):
    return num1 + num2


if __name__ == '__main__':
    total = 0
    while True:
        number1 = int(input("Enter first number: "))
        if number1 == -1:
            print("Total is:", total)
            break
        number2 = int(input("Enter second number: "))

        result = addition(number1, number2)
        total += result
        print(result)

    while True:
        total = 0
        number1 = int(input("Enter your first number: "))
        if number1 == -1:
            break
        number2 = int(input("Enter your second number: "))
        result = multiplication_loop(number1, number2)
        print(result)


