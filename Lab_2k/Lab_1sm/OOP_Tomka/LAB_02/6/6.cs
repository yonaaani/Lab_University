using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _06maxSequenceOfEqualElements
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = Console.ReadLine()
                .Split(new char[] { ' ' }, StringSplitOptions.RemoveEmptyEntries)
                .Select(int.Parse).ToList();
            int start = 0;
            int bestStart = 0;
            int len = 0;
            int bestLen = 0;

            for (int i = 1; i < numbers.Count; i++)
            {
                if (numbers[start] == numbers[i])
                {
                    len++;
                    if (len > bestLen)
                    {
                        bestStart = start;
                        bestLen = len;
                    }
                }
                else
                {
                    start++;
                    i = start;
                    len = 0;
                }
            }
            for (int i = 0; i <= bestLen; i++)
            {
                Console.Write(numbers[bestStart + i] + " ");
            }
            Console.WriteLine();
        }
    }
}