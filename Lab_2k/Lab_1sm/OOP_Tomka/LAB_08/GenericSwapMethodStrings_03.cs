using System;
using System.Collections.Generic;
using System.Text;

namespace GenericSwapMethodStrings_03
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
        static void Swap<T>(List<Box<T>> list, int ind1, int ind2)
        {
            Box<T> box = list[ind1];
            list[ind1] = list[ind2];
            list[ind2] = box;
        }

        static void Main(string[] args)
        {
            var boxes = new List<Box<string>>();

            int n = int.Parse(Console.ReadLine());
            for (int i = 0; i < n; i++)
            {
                string value = Console.ReadLine();
                boxes.Add(new Box<string>(value));
            }

            int[] r = Console.ReadLine().Split().Select(int.Parse).ToArray();
            Swap(boxes, r[0], r[1]);

            foreach(var box in boxes) //перебір масива(ліста)
            {
                Console.WriteLine(box);
            }
        }
    }
}
