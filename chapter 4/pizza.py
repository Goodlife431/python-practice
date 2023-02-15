def snacks(offenders, balance, expected):

    amount = (expected - balance) // offenders
    print(f'how many people needed to pay the balance: {amount}')


if __name__ == '__main__':
    snacks(int(input("Enter offenders amount: ")), 4200, 17000)

