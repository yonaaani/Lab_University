using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Stack_03
{
   public class Stack<T> : IEnumerable<T>
    {
        private List<T> elements;

        public Stack()
        {
           this.elements = new List<T>();
        }

        public void Push(params T[] elements)
        {
            this.elements.AddRange(elements); //метод додає елементи в кінець
        }

        public void Pop(params T[] elements)
        {
            bool areAny = this.elements.Any();
            if (!areAny)
            {
                throw new Exception("No elements");
            }

            int lastIndex = this.elements.Count - 1;
            this.elements.RemoveAt(lastIndex);
        }

        public IEnumerator<T> GetEnumerator()
        {
            for (int i = 0; i < this.elements.Count; i++)
            {
                yield return this.elements[i];  // yield return - визначає елемент що повертається
                                                // yield break - вказує що послідовність більше не має елементів
            }
        }
        IEnumerator IEnumerable.GetEnumerator() => this.GetEnumerator();
    }

    public class StartProgram
    { 
      public static void Main(string[] args)
        {
            Stack<int> stack = new Stack<int>();

            string input = string.Empty; // порожній рядок

            while((input = Console.ReadLine()) != "END")
            {
                string[] elements = input.Split(" ",2).ToArray();
                string commands = elements[0];

                if(commands == "Push")
                {
                    int[] elementsToAdd = elements[1].Split(", ").Select(int.Parse).ToArray();
                    stack.Push(elementsToAdd);
                }
                else if(commands == "Pop")
                {
                    try
                    {
                        stack.Pop();
                    }
                    catch(Exception e)
                    {
                        Console.WriteLine(e.Message);
                    }
                   
                }

                for(int i = 0; i < 2; i++)
                {
                    foreach(int number in stack)
                    {
                        Console.WriteLine(number);
                    }
                }
            }
        }
    }
}
