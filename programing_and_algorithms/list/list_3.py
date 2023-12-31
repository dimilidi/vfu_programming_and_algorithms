"""
От първия ред на стандартния вход се въвежда цяло положително число n (n<=300), от втория ред на
стандартния вход се въвеждат n на брой числа. На първия ред на стандартния изход да се отпечата
последното въведено число, което има цифра на единиците 5 или NO, ако няма въведено такова число.
"""
# Въвеждане на броя числа
n = int(input())

# Въвеждане на редицата от числа
numbers_str = input()

# Разделяне на числата и преобразуване в списък от цели числа
numbers = list(map(int, numbers_str.split()))

# Инициализация на променлива за последното число с цифра на единиците 5
last_ending_with_5 = None

# Търсене на последното число с цифра на единиците 5
for num in reversed(numbers):
    if num % 10 == 5:
        last_ending_with_5 = num
        break

# Извеждане на резултата
if last_ending_with_5 is not None:
    print(last_ending_with_5)
else:
    print("NO")
