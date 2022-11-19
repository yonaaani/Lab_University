using System;
using System.Text.RegularExpressions;

namespace LAB_12
{
    internal class ValidUsernames_07
    {
        static void Main()
        {
            string text = Console.ReadLine();

            string pattern = @"(?<=[\\\/)( ])(?<username>[A-Za-z]\w{2,25})";
            Regex regex = new Regex(pattern);
            MatchCollection matches = regex.Matches(text);

            int sum = 0;
            int bestSum = 0;
            int bestMathes = 0;

            for(int i = 0; i < matches.Count; i++)
            {
                sum = matches[i].Length + matches[i+1].Length;
                if(sum > bestSum)
                {
                    bestSum = sum;
                    bestMathes = i;
                }
            }

            Console.WriteLine("{0}\n{1}", matches[bestMathes], matches[bestMathes + 1]);
        }

    }
}
