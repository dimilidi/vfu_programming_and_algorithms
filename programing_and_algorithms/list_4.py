"""
4 зад. От първия ред на стандартния вход се въвежда цяло положително число n (n<=400), от втория ред на
стандартния вход се въвеждат n на брой числа. На първия ред на стандартния изход да се отпечата
последното въведено число, което е едноцифрено и неговия номер (номерата започват от 1) или NO, ако
няма въведено такова число.
"""
# Въвеждане на броя числа
n = int(input())

# Въвеждане на редицата от числа
numbers_str = input()

# Разделяне на числата и преобразуване в списък от цели числа
numbers = list(map(int, numbers_str.split()))
# numbers = [int(num) for num in numbers_str.split()]


# Инициализация на променливи за последното едноцифрено число и неговия номер
last_single_digit = None
number_index = None

# Търсене на последното едноцифрено число
for index, num in enumerate(reversed(numbers), start=1):
    if 0 < num < 10:
        last_single_digit = num
        number_index = n - index + 1
        break

# Извеждане на резултата
if last_single_digit is not None:
    print(f"{last_single_digit} {number_index}")
else:
    print("NO")
