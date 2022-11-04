using System;
using System.Collections.Generic;
using System.Text;

namespace GenericBoxOfInteger_02
{
    public class Box<T>
    {
        private T value;

        public Box(T value)
        {
            this.value = value;
        }

        public override string ToString()
        {
            return $"{this.value.GetType().FullName}:{this.value}";
        }

    }

    public class StartProgram
    {
        static void Main(string[] args)
        {
            int count = int.Parse(Console.ReadLine());
            for (int i = 0; i < count; i++)
            {
                int value = int.Parse(Console.ReadLine());
                var box = new Box<int>(value);

                Console.WriteLine(box);
            }
        }
    }
}
