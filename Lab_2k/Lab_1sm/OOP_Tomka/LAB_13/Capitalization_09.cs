using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LAB_13
{
    internal class Capitalization_09
    {
        public static void Main(string[] args)
        {
            string input = Console.ReadLine();
            string result = "";
            char[] textInput = input.ToCharArray();
            string capitalizing = textInput[0].ToString();
            string firstLennterCapital = capitalizing.ToUpper();

            result += firstLennterCapital;
            for(int i = 1; i < capitalizing.Length; i++)
            {
                if(input[i] == ' ')
                {
                    if(char.IsLower(input[i+1]))
                    {
                        i++;
                        result += ("" + char.ToUpper(input[i]));
                    }
                }
                else
                {
                    result += input[i];
                }
            }
            Console.WriteLine(result);
        }
    }
}
