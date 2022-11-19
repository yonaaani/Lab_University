using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LAB_13
{
    internal class ReversetheWordsinaSentence_06
    {
        static void Main(string[] args)
        {
            Console.WriteLine("input = ");
            string str = Console.ReadLine();
            string strrev = "";
            char[] punctuation = new char[] { ' ', ',', '.', ':', '\'', '?', '!', '@', '#', '\"' };


            char[] inputAsChars = str.ToCharArray();


            string temp = "";
            foreach (char c in inputAsChars)
            {
                if (punctuation.Contains(c))
                {

                    char[] tx = temp.ToCharArray();
                    Array.Reverse(tx);
                    temp = new string(tx);
                    strrev += temp + c;
                    temp = "";
                }
                else
                    temp += c;
            }

            Console.WriteLine("Output= {0}", strrev);
        }
    }
}
