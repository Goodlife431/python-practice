if __name__ == '__main__':
    print("Start entering numbers")
    total = 0
    count = 0

    while True:
        number = int(input('Enter integers:'))
        total = total + number
        count = count + 1
        if number > total:
            break
        if number == total:
            break
        else:
            count = count + 1

