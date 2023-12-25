//  2 зад. На поредния световен конгрес на сумистите се събрали няколко тона спортисти.
//  Да се състави програма (C++), чрез която по въведено общо тегло на сумисти и тяхното средно тегло се изчислява възможния брой спортисти.
//  Програмата да дава възможност потребителят да тества различни входни данни. Броят на опитите се определя от потребителя.
// Общото тегло, в тонове, е естествено число от интервала [10..99]., а средното тегло, в килограми, е реално число от интервала [120.299].

#include <iostream>
#include <iomanip>

using namespace std;

// Функция за въвеждане на данните
void inputData(int &totalWeight, double &averageWeight) {
    cout << "Enter the total weight and average weight (separated by space): ";
    cin >> totalWeight >> averageWeight;
}

// Функция за изчисляване на възможния брой спортисти
int calculatePossibleAthletes(int totalWeight, double averageWeight) {
    double totalWeightKg = totalWeight * 1000;  // Преобразуване в килограми
    return static_cast<int>(totalWeightKg / averageWeight + 0.5);
}

// Главна функция
int main() {
    int totalWeight;
    double averageWeight;

    // Въвеждане на данните
    inputData(totalWeight, averageWeight);

    // Изчисляване на възможния брой спортисти
    int possibleAthletes = calculatePossibleAthletes(totalWeight, averageWeight);

    // Извеждане на резултата
    cout << "Possible number of athletes: " << possibleAthletes << "\n";

    return 0;
}
