import math

if __name__ == '__main__':
    count = 0
    numbers = []

    while count != -1:
        temp = int(input("Enter a number: "))
        if temp == -1:
            break
        if 0 < temp < 100:
            numbers.append(temp)
        count += 1
    maximum = max(numbers)
    minimum = min(numbers)
    print(maximum)
    print(minimum)


