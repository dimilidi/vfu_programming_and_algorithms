// 3 зад. Да се състави програма на C++, чрез която се отпечатват двойките индекси на всички елементи от масива, чиято стойност е по-малка от v.#include <iostream>

const int ROWS = 6;
const int COLS = 5;

void printIndices(int matrix[ROWS][COLS], int v) {
    for (int i = 0; i < ROWS; ++i) {
        for (int j = 0; j < COLS; ++j) {
            if (matrix[i][j] < v) {
                std::cout << "Element at index (" << i << ", " << j << ") has value " << matrix[i][j] << std::endl;
            }
        }
    }
}

int main() {
    int matrix[ROWS][COLS] = {
        {79, 72, 13, 14, 15},
        {21, 22, 53, 24, 75},
        {31, 57, 33, 34, 35},
        {41, 42, 43, 44, 45},
        {59, 52, 53, 54, 55},
        {61, 69, 63, 64, 65}
    };

    int v;
    std::cout << "Enter a value v: ";
    std::cin >> v;

    printIndices(matrix, v);

    return 0;
}
