# 1 зад. Да се напише програма, коятo реализира следните действия:
# -	Въвежда едно цяло число n от клавиатурата и въвeжда в масив n на брой елементи.
# -	Въвежда цяло число m от клавиатурата и въвежда в масив m на брой елементи;
# -	Отпечатва YES ако броят на едноцифрените елементи в двата масива е равен и NO в противен случай;
# -	Сортира елементите на първият масив във възходящ ред, а на втория – в низходящ ред;
# -	Отпечатва сортираните масиви;

def input_array():
    elements = input("Enter elements separated by spaces: ")
    array = list(map(int, elements.split()))
    return array

def input_n_and_array():
    n = int(input("Enter the number of elements (n): "))
    print(f"Enter {n} elements separated by spaces:")
    array = input_array()
    return array

def is_one_digit_elements_count_equal(array1, array2):
    count_digits_array1 = sum(1 for element in array1 if 0 <= element <= 9)
    count_digits_array2 = sum(1 for element in array2 if 0 <= element <= 9)

    if count_digits_array1 == count_digits_array2:
        print("YES")
    else:
        print("NO")

def sort_arrays(array1, array2):
    array1.sort()
    array2.sort(reverse=True)

def print_arrays(array):
    print(" ".join(map(str, array)))

# Въвеждане на масивите
print("For array1:")
array1 = input_n_and_array()

print("For array2:")
array2 = input_n_and_array()

# Отпечатване на резултата
is_one_digit_elements_count_equal(array1, array2)

# Сортиране на масивите
sort_arrays(array1, array2)

# Отпечатване на сортираните масиви
print("Sorted array1:")
print_arrays(array1)

print("Sorted array2:")
print_arrays(array2)
