def christmas_song():
    for i in range(1, 13, 1):
        print('on the ')
        match i:
            case 1:
                print('first')
            case 2:
                print('second')
            case 3:
                print('third')
            case 4:
                print('fourth')
            case 5:
                print('fifth')
            case 6:
                print('sixth')
            case 7:
                print('seventh')
            case 8:
                print('eighth')
            case 9:
                print('ninth')
            case 10:
                print('tenth')
            case 11:
                print('eleventh')
            case 12:
                print('twelfth')

        print('Day my true love gave to me')
        for s in range(1, 13, 1):
            match s:
                case 1:
                    print('A partridge in a pear tree ')
                case 2:
                    print('Turtle Doves')
                case 3:
                    print('French Hens')
                case 4:
                    print('Calling Birds')
                case 5:
                    print('Golden Rings')
                case 6:
                    print('Geese a laying')
                case 7:
                    print('Swans a swimming')
                case 8:
                    print('Maids a milking')
                case 9:
                    print('Ladies Dancing ')
                case 10:
                    print('Lords a leaping')
                case 11:
                    print('Pipers piping ')
                case 12:
                    print(' Drummers Drumming ')


def check_multiple(number1, number2):
    if number2 % number1 == 0:
        print('it is a multiple of the number ')
    else:
        print('it is not a multiple of the number ')


def temperature():
    kev = float(input("Enter celsius degree"))
    cel = float(input("Enter kelvin degree"))
    kelvin = cel + 273.15
    celsius = kev - 273.15
    print(f"Kelvin degree : {kelvin}")
    print(f"celsius degree : {celsius}")


def sum_of_digits():
    num = input("Enter four digit numbers :")
    num1 = int(num)
    count = 0
    total = 0
    while count <= num1:
        if len(num) == 4:
            rem = num1 % 10
            total += rem
            num1 //= 10
            count += 1
            print(f"The total of the {num} is : {total}")
        elif len(num) > 4:
            print("Length of number must be 4")
            break


if __name__ == '__main__':
    christmas_song()
    check_multiple(5, 12)
    temperature()
    sum_of_digits()
