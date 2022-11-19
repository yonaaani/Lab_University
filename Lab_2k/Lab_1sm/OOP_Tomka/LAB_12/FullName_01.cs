using System;
using System.Text.RegularExpressions;

namespace LAB_12
{
    class FullNmae_01
    {
        public static void Main()
        {
            var text = Console.ReadLine();
            var patten = new Regex(@"\b([A-Z][a-z]+) ([A-Z][a-z]+)\b");

            MatchCollection math = patten.Matches(text);

            foreach (Match item in math)
            {
                Console.Write("{0} ", string.Join(" ", item));
            }

        }
    }
}