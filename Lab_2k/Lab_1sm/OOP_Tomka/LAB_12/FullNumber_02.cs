using System;
using System.Text.RegularExpressions;

namespace LAB_12
{
    internal class FullNumber_02
    {
            public static void Main()
            {
                var text = Console.ReadLine();
                var patten = new Regex(@"(\\+359)(\\s+|-)(2)(\\2)([\\d]{3})(\\2)([\\d]{4}\\b)");

                MatchCollection math = patten.Matches(text);

                foreach (Match item in math)
                {
                    Console.Write("{0} ", string.Join(" ", item));
                }

            }

    }
}
