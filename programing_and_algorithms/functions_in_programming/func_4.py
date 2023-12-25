# 4 зад. Да се състави програма, чрез която в двумерен масив, с брой колони А и брой редове B, се въвеждат псевдослучайни естествени числа от интервала [0..100]. А и В се въвеждат от клавиатурата. 
# Програмата да въведе в два други едномерни масива, поотделно само четните и нечетни въведени числа.
# Чрез функция да се изведе броя на четните и нечетни числа.

import random

def generate_matrix(rows, columns):
    matrix = []
    for _ in range(rows):
        row = [random.randint(0, 100) for _ in range(columns)]
        matrix.append(row)
    return matrix

def separate_even_odd_numbers(matrix):
    even_numbers = []
    odd_numbers = []

    for row in matrix:
        for number in row:
            if number % 2 == 0:
                even_numbers.append(number)
            else:
                odd_numbers.append(number)

    return even_numbers, odd_numbers

def format_numbers_output(numbers, is_even=True):
    numbers_str = '; '.join(map(str, numbers))
    return f"{len(numbers)} {'четни' if is_even else 'нечетни'} числа: {numbers_str};"

def print_matrix(matrix):
    for row in matrix:
        print('; '.join(map(str, row)), end=';\n')

def print_counts(even_count, odd_count):
    print(format_numbers_output(even_count))
    print(format_numbers_output(odd_count, False))

def main():
    rows = int(input("Въведете брой редове: "))
    columns = int(input("Въведете брой колони: "))

    matrix = generate_matrix(rows, columns)

    print("Генерирана матрица:")
    print_matrix(matrix)

    even_numbers, odd_numbers = separate_even_odd_numbers(matrix)

    print_counts(even_numbers, odd_numbers)

main()

