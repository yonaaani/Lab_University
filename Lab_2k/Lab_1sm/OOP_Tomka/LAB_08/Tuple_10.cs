using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Tuple_10
{
    class Tuple<T1, T2> // Це клас, який може зберігати кілька об’єктів, але давайте зосередьтеся на типі кортежу, який містить два об’єкти
    {
        public T1 Item1 { get; }
        public T2 Item2 { get; }

        public Tuple(T1 item1, T2 item2)
        {
            Item1 = item1;
            Item2 = item2;
        }

        public override string ToString()
        {
            return $"{Item1} -> {Item2}";
        }
    }

    class StartProgram
    {
        static void Main(string[] args)
        {
            var input = Console.ReadLine().Split();
            Tuple<string, string> tuple1 = new Tuple<string, string>(input[0] + " " + input[1], input[2]);
            Console.WriteLine(tuple1);

            input = Console.ReadLine().Split();
            Tuple<string, int> tuple2 = new Tuple<string, int>(input[0], Convert.ToInt32(input[1]));
            Console.WriteLine(tuple2);

            input = Console.ReadLine().Split();
            Tuple<int, double> tuple3 = new Tuple<int, double>(Convert.ToInt32(input[0]), Convert.ToDouble(input[1].Replace('.', ',')));
            Console.WriteLine(tuple3);
        }
    }
}
