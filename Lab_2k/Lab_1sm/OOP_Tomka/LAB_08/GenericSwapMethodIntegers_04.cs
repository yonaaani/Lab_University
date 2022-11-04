using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GenericSwapMethodIntegers_04
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
            var boxes = new List<Box<int>>();

            int n = Convert.ToInt32(Console.ReadLine());
            for (int i = 0; i < n; i++)
            {
                int value = Convert.ToInt32(Console.ReadLine());
                boxes.Add(new Box<int>(value));
            }

            int[] r = Console.ReadLine().Split().Select(int.Parse).ToArray();
            Swap(boxes, r[0], r[1]);

            foreach (var box in boxes) //перебір масива(ліста)
            {
                Console.WriteLine(box);
            }
        }
    }
}
