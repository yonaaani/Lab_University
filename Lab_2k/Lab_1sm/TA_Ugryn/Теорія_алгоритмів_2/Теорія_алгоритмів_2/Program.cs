using System;

/*
 * Алгоритм сортування вибором складається з наступних кроків:

-Спочатку визначаємо позицію мінімального елемента масиву;
-Робимо обмін мінімального елемента з елементом на початку масиву. Виходить, перший елемент масиву вже відсортований;
-Зменшуємо робочу область масиву, відкидаючи перший елемент, а для підмасиву який вийшов, повторюємо сортування.
*/

namespace Laba_03
{
    namespace Insertion_Sort
    {
        class Program
        {
            static void Main(string[] args)
            {
                Console.WriteLine("Масив: ");
                int[] Numbers = new int[] { 12, 8, 27, 2, 6, 19, 10, 13, 25, 45, 56, 54, 76, 75, 90, 45, 32, 65, 76, 65,85,98,23,24,53,32,23,45,46,54,96,32,12,34,23,12,16,22,23,43,54,65,76,87,98,50,30,20,12,13,14,15,25,45,56,67, 45, 56, 54, 76, 75, 90, 45, 32, 65, 76, 65, 85, 98, 12, 8, 27, 2, 6, 19, 10 };
                for (int i = 0; i < Numbers.Length; i++)
                {
                    Console.WriteLine(Numbers[i]);
                }

                for (int i = 0; i < Numbers.Length; i++)
                {
                    int temp = Numbers[i];
                    int j = i;

                    while (j > 0 && Numbers[j - 1] > temp)
                    {
                        Numbers[j] = Numbers[j - 1];
                        j--;
                    }
                    Numbers[j] = temp;
                }

                Console.WriteLine("Відсортований масив: ");
                for (int i = 0; i < Numbers.Length; i++)
                {
                    Console.WriteLine(Numbers[i] + " ") ;
                }
                Console.ReadLine();

            }


        }
    }
}


