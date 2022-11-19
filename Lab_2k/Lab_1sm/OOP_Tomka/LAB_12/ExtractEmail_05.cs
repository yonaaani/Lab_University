using System;
using System.Text.RegularExpressions;

namespace LAB_12
{
    internal class ExtractEmail_05
    {
        static void Main()
        {
            string input = Console.ReadLine();

            // тобто тут зможемо використовувати як і різні слова \w
            // так і нижній регістр _
            // так і крапку у назвах пошти
            string pattern = @"\b[\w_.]+@[._\w]+\.\w+\b";
            Regex regex = new Regex(pattern);
            MatchCollection mathes = regex.Matches(input);

            foreach(var match in mathes)
            {
                Console.WriteLine(match);
            }
        }
    }
}
