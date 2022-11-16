#include <iostream>
#include <cmath>
using namespace std;

// Перетворення до суми
float sum(float x, int k)
{
    int n = 0;
    float a = 1, sum, r;
    sum = 0;
    for (k = 0; k <= n; k++)
    {
        sum += a;
        r = (2*x*(k/2 + 35)+k);
        a = a * r;
    }
    return sum;
}
double t(double x)
{
    return sum(0, 10);
}

double foo(int n, int t = 100) {
    if (t > n) return 0;
    return (2*foo(n,t + 1)*((n/2)+35) + n);
}

int main()
{
    setlocale(LC_ALL, "Ukr");

    double n, T;
    cout << " n = "; cin >> n;
    T = 2 * t(n) * (n / 2 + 35) + n;
    cout << " Перетворення до суми: " << endl;
    cout << " T(n) = 2T(n/2 + 35) + n = " << T << endl;
    cout << foo(n);
    system("pause");
    return 0;
}