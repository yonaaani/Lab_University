#include <iostream>  
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int dis(int x, int y)
{
    if (x + y == 0)
        return 0;
    else
        return 1;
}

int kon(int x, int y)
{
    if (x * y == 1)
        return 1;
    else
        return 0;
}

int otr(int x)
{
    return !x;
}

int function(int x, int y, char* formula, int counter)
{
    switch (formula[counter])
    {
    case '^': return kon(x, y);
    case 'v': return dis(x, y);
    }
}

void BIN(int a) {

    char binary[5];

    for (int i = 3; i >= 0; i--) 
    {
        if (a % 2 == 0) { binary[i] = '0'; }
        else { binary[i] = '1'; }
        a = a / 2;
    }

    for (int i = 0; i < 5; i++) 
    {           
        cout << binary[i] << "   ";
    }
    cout << endl;
}


int main()
{
    long t11 = clock();
    // Variant 1-------------------
    cout << "1 Variant" << endl;
    cout << "A   B   C   D   f" << endl;
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)
            for (int k = 0; k < 2; k++)
                for (int l = 0; l < 2; l++)
                cout << i << "   " << j << "   " << k << "   " << l << "   " << (i && (!j && !k)) << endl;
    long t22 = clock();
    cout << (t22 - t11)/(double(CLOCKS_PER_SEC)) << endl;

    long t1 = clock();
    // Variant 2-------------------
    cout << "2 Variant" << endl;
    string number_2, temp, number_16;
    int k, c = 0, numeral;
    string  table[] = { "","1","2","3","4","5","6","7","8",
                      "9","A","B","C","D","E","F" };

    cin >> number_2;
    k = number_2.length();
    //----------------
    if (k % 4 != 0)
        while (k % 4 != 0)
        {
            temp = number_2;
            number_2 = '0';
            number_2 += temp;
            k = number_2.length();
        }
    temp = "";
    //--------------------
    for (k = 0; k < number_2.length(); k++)
    {
        temp += number_2[k];
        c++;
        if (c == 4)
        {
            numeral = 8 * (temp[0] - '0') + 4 * (temp[1] - '0') +
                2 * (temp[2] - '0') + (temp[3] - '0');
            number_16 = table[numeral];
            cout << number_16;
            temp = "";
            c = 0;
        }
    }
    cout << endl;
    //--------------------------
    long t2 = clock();
    cout << (t2 - t1)/(double(CLOCKS_PER_SEC)) << endl;
    system("pause");
    return 0;
}

/*Висновок:
            в 1 Варіанті треба довше замучитись з кодом, але виконуватись буде в рази швидше
            в 2 Варіанті потрібно буде розв'язати письмово і ввести готовий код в двійковій системі числення
            тому я схиляюсь до 1, оскільки то точно буде швидше
  */