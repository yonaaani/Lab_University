using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LAB_13
{
    internal class Palindromes_08
    {
        static void Main(string[] args)
        {
            string[] input = Console.ReadLine().Split(new char[] { ' ', ',', '.', '?', '!' });
            List<string> palindromes = StringPalindromes(input);
            palindromes = palindromes.Distinct().ToList();
            palindromes.Sort();
            Console.WriteLine(string.Join(",", palindromes));
        }

        private static List<string> StringPalindromes(string[] input)
        {
            List<string> result = new List<string>();
            foreach (string word in input)
            {
                if (word.Equals(new string(word.ToCharArray().Reverse().ToArray())))
                {
                    result.Add(word);
                }
            }

            return result;
        }
    }
}
