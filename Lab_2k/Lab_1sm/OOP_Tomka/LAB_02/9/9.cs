using System;
using System.Collections.Generic;
using System.Text;

namespace _09AlphabetLetterToDigit
{
    class Program
    {
        static void Main(string[] args)
        {
            // англійський алфавіт зразу ж у відповідних індексах
            char[] alphabet = new char[26] { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' };

            Console.WriteLine("\nEnter your words:");
            string input = Console.ReadLine();
            Console.Clear();
            Console.WriteLine($"\n\nYour number message is:\n\n");
            StringBuilder sb = new StringBuilder();

            // видалити будь-який тескт що не буде буквою
            foreach (char c in input)
            {
                if (char.IsLetter(c))
                {
                    sb.Append(c);
                }
            }

            string validatedInput = sb.ToString().ToUpper();
            List<int> output = new List<int>();

            // для кожної букви знайде і виведе відповідне число
            foreach (char c in validatedInput)
            {
                output.Add(Array.IndexOf(alphabet, c) + 1);
            }

            foreach (int digit in output)
            {
                Console.Write($"{digit} ");
            }
        }
    }
}