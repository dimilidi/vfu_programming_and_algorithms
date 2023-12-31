# 8 зад. От първия ред на стандартния вход се въвежда цяло положително число n (n<=100), от втория ред на
# стандартния вход се въвеждат n на брой числа. На първия ред на стандартния изход да се отпечата
# дължината на най-дългата последователност от едноцифрени числа.

# Вход:
# Въвеждане на брой числа
n = int(input())  
# Въвеждане на числата като стринг
num_str = input()  
# Преобразуване на стринга в списък от цели числа
num_int_list = list(int(num) for num in num_str.split())  
# Брояч за текущата последователност
counter = 1  
# Максимална дължина на последователността
max_counter = 1 

# Списък за индексите на едноцифрените числа
one_digit_num_list = []  

# Попълване на списъка с индексите на едноцифрените числа
for index, one_digit_num in enumerate(num_int_list):
    if 0 < one_digit_num < 10:
        one_digit_num_list.append(index)

# Прохождане през списъка с индексите и проверка за последователност от едноцифрени числа
for i in range(1, len(one_digit_num_list)):
    if one_digit_num_list[i] == one_digit_num_list[i - 1] + 1:
        counter += 1
        if counter > max_counter:
            max_counter = counter
    else:
        counter = 1  # Нулиране на брояча при нарушаване на последователността


# Изход:
# Отпечатване на дължината на най-дългата последователност от едноцифрени числа
print(max_counter)  
