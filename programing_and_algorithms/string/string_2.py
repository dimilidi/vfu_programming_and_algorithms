# Зад. 2 ДСНП ana.cpp, която прочита от клавиатура два символни низа и отпечатва “Yes”, ако първия е анаграма (състоят се от едни и същи символи и брой) на втория и “No” в противен случай.

first_str = input('Enter your fitst word: ')
second_str = input('Enter your second word: ')

def is_anagram(str_1, str_2):
    # Проверявам дали дължината на двата низа е еднаква
    if len(str_1) != len(str_2):
        return False
  
   # Сортирам знаците в двата низа и ги сравнявам
    sorted_str_1 = sorted(str_1)
    sorted_str_2 = sorted(str_2)

    return sorted_str_1 == sorted_str_2

# Отпечатване на резултат
if is_anagram(first_str, second_str):
    print('Yes')
else:
    print('No')
                  


   
