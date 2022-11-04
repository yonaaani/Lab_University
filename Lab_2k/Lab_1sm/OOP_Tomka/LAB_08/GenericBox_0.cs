using System;
using System.Collections.Generic;
using System.Text;

namespace GenericBox_0
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

    public class SrartProgram
    {
        static void Main(string[] args)
        {
            var box1 = new Box<int>(123123);
            var box2 = new Box<string>("life in a box");

            Console.WriteLine(box1);
            Console.WriteLine(box2);
        }
    }
}

