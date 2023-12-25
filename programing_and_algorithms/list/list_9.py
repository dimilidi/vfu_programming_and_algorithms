# 9 зад. От първия ред на стандартния вход се въвежда цяло положително число n (n<=250) и цяло
# положително едноцифрено число m, от втория ред на стандартния вход се въвеждат n на брой числа. На
# първия ред на стандартния изход да се отпечата дължината на най-дългата последователност от числа,
# чиято цифра на единиците е равна на m.

# Вход:
# От първия ред на стандартния вход:
n_list = list(int(num) for num in input().split())  
#  цяло положително число n
n = n_list[0]
#  цяло положително едноцифрено число m
m = n_list[1]

# от втория ред на стандартния вход се въвеждат n на брой числа
num_str = input() 
num_int_list = list(int(num) for num in num_str.split())  

# Създаване на списък с индексите на числата, чиято цифра на единиците е равна на m
indexes_of_nums_with_last_digit_m = []
for index, num in enumerate(num_int_list):
    last_digit = num % 10
    if last_digit == m:
        indexes_of_nums_with_last_digit_m.append(index)

# Процес на търсене на най-дългата последователност
counter = 1
max_counter = 1

for i in range(1, len(indexes_of_nums_with_last_digit_m)):
    # Инкрементиране на брояча с 1, ако индексите са последователни числа
    if indexes_of_nums_with_last_digit_m[i] == indexes_of_nums_with_last_digit_m[i - 1] + 1:
        counter += 1
        #  Съхраняване на най-дългата последователност в  max_counter
        if counter > max_counter:
            max_counter = counter
    # Нулиране на брояча при нарушаване на последователността
    else:
        counter = 1  

# Изход:
print(max_counter)  # Отпечатване на дължината на най-дългата последователност
