# 1 зад. Дадена е квадратна матрица от реални числа с размерност (n х n), където 1n20. Да се състави програма, съдържаща подпрограми за: 
# а) запълване на матрицата с числа от клавиатурата;
# б)намиране на минималния от всички ненулеви елементи под главния диагонал включително; ако ненулеви елементи няма, за минимален елемент се приема 0;
# в)извеждане на елементите на матрицата под главния диагонал на екрана.
# Да се състави програма matrix1, която като използва описаните подпрограми, запълва матрицата с числа от клавиатурата, преобразува я като запълва контура на матрицата с намерения от т.б) елемент и извежда новополучената матрица на екрана.

def input_matrix(n):
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def find_min_below_main_diagonal(matrix):
    min_value = float('inf')
    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            if matrix[i][j] > 0 and matrix[i][j] < min_value:
                min_value = matrix[i][j]
    return min_value if min_value != float('inf') else 0

def fill_contour_with_min(matrix, min_value):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j or i + j == len(matrix) - 1:
                matrix[i][j] = min_value
    return matrix

def print_below_main_diagonal(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            print(matrix[i][j], end=" ")
        print()

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Main program
n = int(input("Enter the dimension of the matrix (n): "))
original_matrix = input_matrix(n)

min_value = find_min_below_main_diagonal(original_matrix)
result_matrix = fill_contour_with_min(original_matrix, min_value)

print("\nMatrix after transformation:")
print_matrix(result_matrix)

print("\nElements below the main diagonal:")
print_below_main_diagonal(result_matrix)

print(f"\nThe minimum positive value below the main diagonal is: {min_value}")

