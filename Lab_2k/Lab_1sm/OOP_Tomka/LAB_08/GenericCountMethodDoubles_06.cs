using System;
using System.Collections.Generic;
using System.Text;

namespace GenericCountMethodDoubles_06
{
    class Box<T> : IComparable<T> where T : IComparable<T>
    {
        private T Value
        {
            get; set;
        }

        public Box(T value)
        {
            Value = value;
        }

        public int CompareTo(T other)
        {
            return Value.CompareTo(other);
        }

        public override string ToString()
        {
            return $"{Value.GetType().FullName}:{Value}";
        }

    }

    class StartProgram
    {
        static void Main(string[] args)
        {
            List<Box<double>> boxes = new List<Box<double>>(); //double
            int count = Convert.ToInt32(Console.ReadLine());

            for (int i = 0; i < count; i++)
            {
                double value = Convert.ToInt32(Console.ReadLine());

                boxes.Add(new Box<double>(value));
            }


            double element = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine(Count(boxes, element));
        }

        static int Count<T>(IEnumerable<Box<T>> collection, T element) where T : IComparable<T>
        {
            int counter = 0;

            foreach (var item in collection)
            {
                if (item.CompareTo(element) > 0)
                {
                    counter++;
                }
            }

            return counter;
        }
    }
}
