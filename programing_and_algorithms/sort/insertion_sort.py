

def insertion_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(i + 1, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break

# Example usage:
array = [75, 34, 54, 56, 78, 1]
insertion_sort(array)

for element in array:
    print(element, end=' ')

