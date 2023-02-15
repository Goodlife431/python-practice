# arr = [1, 2, 3, 4, 5, 6, 8, 9, 10]
#
#
# def missing_value(let):
#     for i in range(1, 11):
#         if i not in let:
#             return i
#
#
# print(missing_value(arr))


# import itertools
#
# integer_array = [2, 7, 11, 15]
# target = 9
# for i in itertools.combinations(integer_array, 2):
#     if sum(i) == target:
#         print([integer_array.index(number) for number in i])

# numbers = [2, 3, 1]
# target = 9
# for x in numbers:
#     for y in numbers:
#         if x + y == target:
#             print(numbers.index(x))
#

# arr = [1, 2, 2, 3, 6]
# arr2 = [21, 40, 19, 12, 3]
#
# result1 = set(arr)
# result2 = set(arr2)
#
# if result1 ==

# def sum_diagonal():
#     n = 3
#     a = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
#     sum_first_diagonal = sum(a[i][i] for i in range(n))
#     sum_second_diagonal = sum(a[n - i - 1][n - i - 1] for i in range(n))
#     print(str(sum_first_diagonal) + " " + str(sum_first_diagonal))
#

# arr1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
#
# def sum_diagonal(arr):
#     total = 0
#     for i in range(len(arr)):
#         total += arr[i][i]
#
#     return total
#
#
# print(sum_diagonal(arr1))

# numbers = [7, 9, 2, 5]
#
#
# def the_two_largest_umber(number):
#     first = number[0]
#     temp = number[0]
#     number[0] = number[1]
#     number[1] = temp
#     return temp, first

num_list = [1, 2, 3, 4, 5]

print(f'Current Numbers List {num_list}')

num = int(input("Please enter a number to add to list:\n"))

index = int(input(f'Please enter the index between 0 and {len(num_list) - 1} to add the number:\n'))

num_list.insert(index, num)

print(f'Updated Numbers List {num_list}')

