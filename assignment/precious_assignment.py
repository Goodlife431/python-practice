import math


class PreciousAssignment:
    @staticmethod
    def grade_score(grade):
        if grade >= 90:
            print(f'Congratulations! Your grade of {grade} earns you an A in this course')

    @staticmethod
    def eggs_per_box(eggs):
        num_of_boxes = eggs / 6
        eggs_reminder = eggs % 6
        new_box = 6 - eggs_reminder

        if eggs_reminder == 0:
            print(f'{num_of_boxes} needed to fill the to store the eggs')
        elif eggs_reminder != 0:
            print(f'{eggs_reminder}: reminder of  the eggs ')
            print(f'{new_box}: additional eggs needed to fill the box')

    @staticmethod
    def bacteria():
        hours = 0
        print(f" hours\t\t\tNumber of bacteria")
        while hours < 20:
            b = 200 * (2 * hours)
            print(f"{hours}          {b}")
            hours += 5

    @staticmethod
    def hour_wage_calculator(good, bad, amount):
        good_reviews_wage = amount * (1 + 3 / 100) ** good
        print(f'After {good} years of employee good reviews, earning is {good_reviews_wage: .2f} ')

        bad_reviews_wage = amount * (1 - 3 / 100) ** bad
        print(f'After {bad} years of employee bad reviews, earning is:{bad_reviews_wage : .2f}')

    @staticmethod
    def heart_rate_calculator():
        age = int(input('Enter users age: '))
        maximum_heart_rate = 220 - age
        range_target_heart_rate = 50 * maximum_heart_rate / 100
        print(
            f'user maximum heart rate is: {maximum_heart_rate}, and range target heart rate is: {range_target_heart_rate} ')

    @staticmethod
    def palindrome(num):
        temp = num
        summation = 0
        while num != 0:
            rem = num % 10
            summation = (summation * 10) + rem
            num //= 10
        if summation == temp:
            print('It is a palindrome number')
        else:
            print('It is not a palindrome number')

    @staticmethod
    def extract(number):
        while number != 0:
            rem = number % 10
            number //= 10
            print(rem, end=' ')
        print()

    @staticmethod
    def bacteria_henry(b):
        print(f'Hours\t\tNumber Of Bacteria')
        for hours in range(0, 20, 5):
            b = 200 * math.pow(2, hours)
            print(f'{hours}\t\t\t {b}')


if __name__ == '__main__':
    PreciousAssignment.grade_score(92)
    PreciousAssignment.eggs_per_box(30)
    PreciousAssignment.bacteria()
    PreciousAssignment.hour_wage_calculator(5, 2, 10)
    PreciousAssignment.heart_rate_calculator()
    PreciousAssignment.palindrome(545)
    PreciousAssignment.extract(7536)
    PreciousAssignment.bacteria_henry(200)
