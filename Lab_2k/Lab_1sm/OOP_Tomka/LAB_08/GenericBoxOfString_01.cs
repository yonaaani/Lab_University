using System;
using System.Collections.Generic;
using System.Text;

namespace GenericBoxOfString_01
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
                string value = Console.ReadLine();
                Box<string> box = new Box<string>(value);

                Console.WriteLine(box);
            }
        }
    }
}
