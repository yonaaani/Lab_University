/* Решето Ератосфена  

Якщо потрібно знайти всі прості числа менші за певне число N, виписуються всі числа від 2 до N.

Перше просте число — два. Викреслимо всі числа більші двох, які діляться на два (4, 6, 8 …).
Наступне число, яке залишилося незакресленим (три), є простим.Викреслюємо всі числа більші трьох та кратні трьом (6, 9 …).
Наступне незакреслене число (п'ять) є простим. Викреслимо всі числа більші п'яти та кратні п'яти (10, 15, 20, 25 …).
Повторюємо операцію поки не буде досягнуто число N:
Наступне незакреслене число є простим. Викреслимо всі числа більші нього та кратні йому.
Числа, які залишилися незакресленими після цієї процедури — прості. */

using System;  
using System.Linq;  // LINQ (Language-Integrated Query) представляет простой и удобный язык запросов к источнику данных.
                    // В качестве источника данных может выступать объект, реализующий интерфейс IEnumerable (например,
                    // стандартные коллекции, массивы), набор данных DataSet, документ XML. Но вне зависимости
                    // от типа источника LINQ позволяет применить ко всем один и тот же подход для выборки данных.

public class _04PrimesSieve
{
    private static int Maximum, Count;
    private static bool[] Primes;

    private static void Main()
    {
        Console.Write("Please write down a number: ");

        Maximum = Convert.ToInt32(Console.ReadLine());

        Console.WriteLine();

        Primes = Enumerable.Repeat(true, Maximum).ToArray();

        for (int C = 2; C < Math.Sqrt(Maximum) + 1; C++)
        {
            for (int N = (int)Math.Pow(C, 2); N <= Maximum; N += C)
            {
                Primes[N - 1] = false;
            }
        }

        for (int C = 2; C <= Primes.Length; C++) // лише <, якщо ми не хочемо включати введене число
        {
            if (Primes[C - 1])
            {
                Count++;
                Console.Write($"{C} ");
            }
        }

        Console.WriteLine("\n");
        Console.WriteLine($"There are {Count} primes up to {Maximum}");   //Primes.Count(B => B == true)
        Console.ReadKey();
    }
}
