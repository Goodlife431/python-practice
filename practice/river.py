"""river = 'Mississippi'
target = input("Enter a character: ")
for index in range(len(river)):
    if river[index] == target:
        print("Letter found at index",index)
        break
else:
    print('Letter', target, 'not found in', river)


def palindrome(s_word):
    if s_word == s_word[::-1]:
        print("is a palindrome word")
    else:
        print("is not a palindrome word")


if __name__ == '__main__':
    s = input("Enter a word: ")
    palindrome(s)"""


def palindrome(word_str):
    plain_word = word_str
    word_array = list(plain_word)
    word_array.reverse()
    target = "".join(word_array)
    return plain_word == target


if __name__ == '__main__':
    s = input("Enter a word: ")
    if palindrome(s):
        print("is a palindrome  ")
    else:
        print("it is not a palindrome ")

