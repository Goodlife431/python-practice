def largest_list():
    largest = []
    count = 0
    while count < 5:
        numbers = int(input('Enter a  five number: '))
        largest.append(numbers)
        count += 1
    temp = largest[0]
    for i in largest:
        if i > temp:
            temp = i
    print(temp)


def reverse_list():
    num = int(input("enter numbers: "))
    num_string = str(num)
    number_list = list(num_string)
    number_list.reverse()
    reversed_num = ''.join(number_list)

    print("Reversed Number is: " + reversed_num)


def check_element():
    check_list = []
    count = 0
    temp = 0
    while count != -1:
        temp = int(input("Enter a number: "))
        if temp == -1:
            break
        if temp > 0:
            check_list.append(temp)
        count += 1
    check = int(input("Enter the number you want to check: "))
    if check in check_list:
        print("element exist")
    else:
        print("element does not exist")


def odd_position():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(0, len(array), 2):
        print(array[i])


def even_position():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(1, len(array), 2):
        print(array[i])


def running_total():
    arr = []
    count = 0
    temp = 0
    total = 0
    while count != -1:
        temp = int(input("Enter a number: "))
        if temp == -1:
            break
        if temp > 0:
            arr.append(temp)
        count += 1
        total += temp
    print(total)


def palindrome():
    s_word = input("enter a word: ")
    if s_word == s_word[::-1]:
        print("is a palindrome word")
    else:
        print("is not a palindrome word")


def loops_sum():
    while True:
        arr_list = []
        count = 0
        temp = 0
        total = 0
        while count < 5:
            temp = int(input("Enter a number: "))
            arr_list.append(temp)
            count += 1
            if temp > 0:
                total += temp
        print(total)
        break
    total = 0
    for x in [1, 2, 3, 4, 5]:
        total = total + x
    print(total)


def concatenates():
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']

    for i in list1:
        list2.append(i)
    print(str(list2))


if __name__ == '__main__':
    # largest_list()
    # reverse_list()
    # check_element()
    # odd_position()
    # even_position()
    # running_total()
    # palindrome()
    #loops_sum()
    concatenates()
