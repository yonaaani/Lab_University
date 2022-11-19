// метод Фібоначчі із затримуванням
#include <iostream>
#include <time.h>

using namespace std;

unsigned int lagA = 0, lagB = 0;

void main(void)
{
	int Count = 0;
	setlocale(LC_ALL, "ukr");
	cout << "Введіть a = ";
	cin >> lagA;
	cout << "Введіть b = ";
	cin >> lagB;
	cout << "Введіть кількість згенерованих значень : ";
	cin >> Count;

	//Для старту фібоначчієвого датчика потрібно max{a,b} випадкових чисел,
	//які можуть бути згенеровані простим (!!!) конгруентним датчиком (!!!).
	srand(time(NULL)); //І так ініціалізуємо конгруентний датчик
	int* Arr = new int[max(lagA, lagB)]; //Генеруєм масив
	for (int i = 0; i < max(lagA, lagB); i++)
		Arr[i] = rand(); //Заповнюємо його випадковими величинами, які згенерували конгруентним датчиком

		//Генеруємо випадкові величини
	for (int i = Count; i > 0; i--)
	{
		int Res; //Результат
		if (Arr[max(lagA, lagB) - lagA] >= Arr[max(lagA, lagB) - lagB])
		{
			Res = Arr[max(lagA, lagB) - lagA] - Arr[max(lagA, lagB) - lagB];
		}
		else Res = Arr[max(lagA, lagB) - lagB] - Arr[max(lagA, lagB) - lagA];

		for (int i = 0; i < max(lagA, lagB); i++)
			Arr[i] = rand(); //Генеруємо масив заново кожної ітерації

		cout << Res << endl; //Виведемо на екран

	}


}