#include <iostream>
#include <fstream>
#include <ios>
using namespace std;

int main(int argc, char* argv[])
{
    unsigned bin = 1;
    unsigned i;
    int j, k = 0;
    if (argc < 2)
        return 1;
    ifstream input(argv[1], ios::in | ios::binary);
    if (!input) return 0;
    while (!input.eof())
    {
        input.read((char*)&i, 3);
        for (j = 0; j < 24; j++)
        {
            if ((i & bin) > 0)
                ++k;
            bin = bin << 1;
        }
        bin = 1;
    }
    cout << k << endl;
    return 0;
}