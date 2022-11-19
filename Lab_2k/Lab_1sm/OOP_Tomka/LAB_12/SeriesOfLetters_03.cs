using System;
using System.Text.RegularExpressions;

namespace LAB_12
{
    internal class SeriesOfLetters_03
    {
        public static void Main()
        {
            var text = Console.ReadLine();
            var patten = new Regex(@"(.)\\1+");

            MatchCollection math = patten.Matches(text);

            foreach (Match item in math)
            {
                Console.WriteLine(patten.Replace(text, "$1"));
            }

        }
    }
}
