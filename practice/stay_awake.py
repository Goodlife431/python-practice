"""import random

if __name__ == '__main__':
    number = random.randint(1, 20)
    count = 1
    print('WELCOME TO MY GUESSING APP')

while count <= 10:
    guessing_number = input('Enter a random number between 1 to 10: ')
    guessing_number = int(guessing_number)

    if guessing_number > number:
        print('input higher than the random number "try again"')

    elif guessing_number < number:
        print('input lesser than random number "try again"')

    else:
        print('perfect number')
        break
    count += 1

num1 = float(input("Enter first number: "))
num2 = int(input("Enter second number: "))
#add = num1 + num2
print(f 'answer is: {num2+num1}')

weight = int(input("enter weight: "))
unit = input("(k)g or (l)bs: ")
if unit.lower() == "k":
    converted = weight / 2.2046
    print(f 'converted to kilograms: {converted: .2f}')
else:
    converted = weight * 2.2046
    print(f 'converted to pounds (l)bs: {converted: .2f}')


b =["banana","apples","orange"]
temp = b[0]
b[0] = b[2]
b[2] = temp

print(b)
count = 0
for numbers in range(1,10):
    if numbers % 2 == 0:
        count += 1
        print(f'{numbers}')
print(f"{count} even number from 1 to 10")

count = 0
total = 0

numbers = int(input("Enter a number: "))
while count <= numbers:
    total += count
    count += 1
    average = total/count
print(f"total is: {total}")
print(f"average is: {average}")

my_str = 'This is a test'
string_elements = my_str.split()
print(string_elements)
reversed_elements = []
for elements in string_elements:
    reversed_elements.append(elements[::-1])
print(reversed_elements)
new_str = ''.join(reversed_elements)
print(new_str)


def sorting(word, word1_int):
    list_word = []
    for element in word1_int:
        list_word.append(int(element))
    return sorted(word) + sorted(list_word)


if __name__ == '__main__':
    word_list = input("Enter a String:  ")
    number = input("Enter a integer:   ")

    print(sorting(word_list, number))

result = 2
n = 5
result = result * n
n = n + 1
print(result)

fist_dict = {
    "key1": "jude hates python",
    "key2": {
        "name": "pargon",
        "age": "4 months",
        "loan amount": "4 million",
        "size": 38,
        "weight": 3.9,
    },
    "key3": "Soo",
    "key4": [50, 10, 5.9, "hate python"],
    "key5": "fantastic"
}
print(fist_dict["key2"]["size"])"""

word = ['ade', 'simi', 'smile', 'glory', 'henry']
save = [x for x in word[:2] if 'i' in x]
okay = [y for y in range(1, 9, 2)]
print(save)
print(okay)

multiplication_dict = {

}



