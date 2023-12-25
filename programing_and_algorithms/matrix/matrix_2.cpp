// 2 зад. Да се състави програма на C++, чрез която се извеждат елементите от масива с най-малката и най-голямата стойност.

#include <iostream>
#include <climits>

int main() {
    const int rows = 6;
    const int columns = 5;

    int array[rows][columns] = {
        {79, 72, 13, 14, 15},
        {21, 22, 53, 24, 75},
        {31, 57, 33, 34, 35},
        {41, 42, 43, 44, 45},
        {59, 52, 53, 54, 55},
        {61, 69, 63, 64, 65}
    };

    int min_value = INT_MAX;
    int max_value = INT_MIN;

    // Намиране на най-малката и най-голямата стойност
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < columns; ++j) {
            if (array[i][j] < min_value) {
                min_value = array[i][j];
            }
            if (array[i][j] > max_value) {
                max_value = array[i][j];
            }
        }
    }

    // Извеждане на резултата
    std::cout << "Най-малката стойност: " << min_value << std::endl;
    std::cout << "Най-голямата стойност: " << max_value << std::endl;

    return 0;
}
