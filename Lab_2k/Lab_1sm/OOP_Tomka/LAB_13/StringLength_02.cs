using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LAB_13
{
    internal class StringLength_02
    {
        static void Main()
        {
            string input = Console.ReadLine();
            string twentyCharacters = input.Length > 20 ? new string(input.Take(20).ToArray()) : input;
            Console.WriteLine(twentyCharacters.PadRight(20, '*'));
        }
    }
}
