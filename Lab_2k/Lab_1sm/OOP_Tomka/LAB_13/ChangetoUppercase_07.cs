using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LAB_13
{
    internal class ChangetoUppercase_07
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Text: ");
            string text = Console.ReadLine();

            char[] textNew = new char[text.Length];

            int i= 0, j = 0, k = 0;
            while(i < text.Length)
            {
                if (text.IndexOf("<upcase>",k) < 0)
                {
                    while(i<text.Length)
                    {
                        textNew[j++] = text[i++];
                    }
                }
                else
                {
                    while(i < text.IndexOf("<upcase>", k))
                    {
                        textNew[j++] = text[i++];
                    }
                    i += 8;
                    k = i;
                }
                if(text.IndexOf("<upcase>", k) < 0)
                {
                    while(i<text.Length)
                    {
                        textNew[j++]= Char.ToUpper(text[i++]);
                    }
                }
                else
                {
                    while (i < text.IndexOf("<upcase>", k))
                    {
                        textNew[j++] = Char.ToUpper(text[i++]);
                    }
                    i += 9;
                }

                foreach(char c in textNew)
                {
                    Console.WriteLine(c);
                }
                Console.WriteLine();
            }
        }
    }
}
