from new_name_function import get_formatted_name

print("Enter q at any time to quit. ")
while True:
    first = input("\nplease give me a first name-> ")
    if first == 'q':
        break
    last = input("\nplease give me last name-> ")
    if last == 'q':
        break
    middle = input("\nplease give me middle name-> ")
    if middle == 'q':
        break
    formatted_name = get_formatted_name(first, last, middle)
    print("\nNeatly formatted name-> " + formatted_name + '.')
