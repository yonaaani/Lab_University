using System;
using System.Collections.Generic;
using System.Linq;

namespace LAB_13
{
    public class ReverseString_01
    {
        static void Main()
        {
            string input = Console.ReadLine();
            string reverseinput = new string(input.Reverse().ToString());
            Console.WriteLine(reverseinput);
        }
    }
}