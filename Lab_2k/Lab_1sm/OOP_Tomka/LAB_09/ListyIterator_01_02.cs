using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ListyIterstor_01_02
{
    public class ListyIterator<T> : IEnumerable<T>
    {
        private List<T> elements;
        private int currentIndex;

        public ListyIterator(params T[] elements) //Використовуючи params ключове слово, ви можете вказати параметр методу , який приймає змінну кількість аргументів. Тип параметра має бути одновимірним масивом.
        {
            this.elements = elements.ToList();
            this.currentIndex = 0;
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

        public bool HasNext()
        {
            bool hasNext = this.currentIndex + 1 <= this.elements.Count - 1;
            if (!hasNext)
            {
                return false;
            }

            return true;
        }

        public bool Move()
        {
            if (!this.HasNext())
            {
                return false;
            }

            this.currentIndex++;

            return true;
        }

        public void Print()
        {
            bool areAny = this.elements.Any();
            if (!areAny)
            {
                throw new InvalidOperationException("Invalid Operation!");
            }

            Console.WriteLine(this.elements[this.currentIndex]);
        }
    }


        public class StartUp
        {
            public static void Main(string[] args)
            {
                string input = string.Empty;

                ListyIterator<string> listyIterator = null;

                while ((input = Console.ReadLine()) != "END")
                {
                    string[] elements = input.Split(" ", StringSplitOptions.RemoveEmptyEntries).ToArray();

                    string command = elements[0];

                    if (command == "Create")
                    {
                        string[] elementsToAdd = elements.Skip(1).ToArray();

                        listyIterator = new ListyIterator<string>(elementsToAdd);
                    }
                    else if (command == "Move")
                    {
                        bool result = listyIterator.Move();

                        Console.WriteLine(result);
                    }
                    else if (command == "Print")
                    {
                        try
                        {
                            listyIterator.Print();
                        }
                        catch (Exception ex)
                        {
                            Console.WriteLine(ex.Message);
                        }
                    }
                    else if (command == "HasNext")
                    {
                        bool result = listyIterator.HasNext();

                        Console.WriteLine(result);
                    }
                    else if (command == "PrintAll")
                    {
                        if (listyIterator.Any())
                        {
                            Console.WriteLine(string.Join(" ", listyIterator));
                        }
                    }
                }
            }
        }
}


