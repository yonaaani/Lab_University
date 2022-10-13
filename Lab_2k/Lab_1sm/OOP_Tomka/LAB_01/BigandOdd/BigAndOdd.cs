using System;

BigandOdd();

void BigandOdd()
{
    Console.Write("Vvedit n: ");
    int n = Convert.ToInt32(Console.ReadLine());

    bool result = true;
    bool nresult = false;
    if (n>20)
    {
        if (n % 10 == 1)
        {
            Console.WriteLine(result);
        }
        else
            Console.WriteLine(nresult);
    }

}
