def multiplication_dict(n):
    d = dict()
    for x in range(1, n):
        d[x] = x * x
    print(d)


def add_set():
    count = 1
    set_number = set()

    while count <= 5:
        try:
            number = int(input("Enter a number: "))
            if 2 <= number <= 90:
                set_number.add(number)
                count += 1
        except ValueError:
            print("invalid type")
            break
    print(set_number)


def conversion():
    values = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred']
    key = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    dict_first = {values[i]: key[i] for i in range(len(values))}
    print(dict_first)


if __name__ == '__main__':
    # multiplication_dict(n=int(input("Enter a number: ")))
    # add_set()
    conversion()
