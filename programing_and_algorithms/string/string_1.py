# Зад. 1 ДСНП, която прочита от клавиатура дума и извежда “Yes”, ако тя е палиндром и “No”, ако не е.

def is_palindrome(word):
    reversed_word = word[::-1]
    return word == reversed_word

word = input("Enter a word: ")

if is_palindrome(word):
    print('Yes')
else:
    print('No')
