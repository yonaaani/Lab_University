using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LAB_13
{
    internal class ExtractSentencesByKeyword_04
    {
        static void Main(string[] args)
        {
            string keyword = Console.ReadLine().ToLower();
            List<string> sentences = Console.ReadLine().Split(new char[] {'.','!','?'}).ToList();

            for(int i = 0; i < sentences.Count; i++)
            {
                string[] result = sentences[i].Split(new char[] { ',', ':', ';', '(', ')', '[', ']', '{', '}', '-', '\\', '/', '\"', '\'', ' ' });

                if(result.Contains(keyword))
                {
                    Console.WriteLine(sentences[i].Trim());
                }
            }

        }
    }
}
