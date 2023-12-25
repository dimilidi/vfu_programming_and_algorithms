"""
2 зад. От първия ред на стандартния вход се въвежда цяло положително число n (n<=200), от втория ред на
стандартния вход се въвеждат n на брой числа. На първия ред на стандартния изход да се отпечата първото
въведено число, което е по-малко от 10 и неговия номер (номерата започват от 1) или NO, ако няма
въведено такова число
"""

# Въвеждане на брой числа
n = int(input())

# Въвежда цяло положително число 
numbers_str = input()

# Инициализация на променлива, която ще съдържа първото число < 10
first_less_than_10 = None

# Четене на числата и търсене на първото  10
numbers_list = numbers_str.split()
numbers_int = [int(num) for num in numbers_list]
index = 0


for num in numbers_int:
    index +=1
    if num < 10:
        first_less_than_10 = num
        break

# Извеждане на резултата
if first_less_than_10 is not None:
    print(f"{first_less_than_10} {index}")
else:
    print("NO")