"""
5 зад. От първия ред на стандартния вход се въвежда цяло положително число n (n<=350), от втория ред на
стандартния вход се въвеждат n на брой числа. На първия ред на стандартния изход да се отпечата броя на
въведените двуцифрени числа, разположени между първото число, което е по-голямо от 100 и последното
число, което е по-малко от 10 или NO, ако няма въведени числа, по-големи от 100 или числа, по-малки от
10
"""

# Въвеждане на брой числа
n = int(input())

# Въвеждане на числата
numbers_str = input()
numbers_list = [int(num) for num in numbers_str.split()]

# Инициализация на променливи за първото число > 100 и последното число < 10
first_over_100 = None
index_first_over_100 = None
last_under_10 = None
index_first_under_10 = None

# Итериране през числата
for index, num in enumerate(numbers_list):
    # Намиране на първото число > 100
    if num > 100:
        first_over_100 = num
        index_first_over_100 = index
        break

# Търсене на последното число < 10
for index, num in reversed(list(enumerate(numbers_list))):
    # Намиране на последното число < 10
    if num < 10:
        last_under_10 = num
        index_first_under_10 = index
        break

# Проверка за наличие на поне едно число > 100 и едно число < 10
if first_over_100 is not None and last_under_10 is not None:
    # Използване на range за създаване на списък с индекси
    indices = list(range(index_first_over_100 + 1, index_first_under_10))

    # Филтриране на двуцифрените числа и добавяне към нов списък
    two_digit_numbers = []
    for i in indices:
        num = numbers_list[i]
        if 10 < num < 100:
            two_digit_numbers.append(num)

    # Отпечатване на броя на двуцифрените числа
    print(len(two_digit_numbers))
    # Отпечатване на двуцифрените числа
    print(two_digit_numbers)
else:
    print("NO")


