using System;

Avarage();

void Avarage()
{ 
    Console.Write("Vvedit a: ");
    int a = Convert.ToInt32(Console.ReadLine());

    Console.Write("Vvedit b: ");
    int b = Convert.ToInt32(Console.ReadLine());

    Console.Write("Vvedit c: ");
    int c = Convert.ToInt32(Console.ReadLine());

    double avarage;
    avarage = (a + b + c) / 3;

    Console.WriteLine(a); Console.WriteLine();
    Console.WriteLine(b); Console.WriteLine();
    Console.WriteLine(c); Console.WriteLine();
    Console.WriteLine(avarage); Console.WriteLine();

}


