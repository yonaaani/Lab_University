using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Froggy_04
{
    public class Lake : IEnumerable<int>
    {
        private List<int> stones;

        public Lake(params int[] stones)
        {
            this.stones = stones.ToList();
        }

        public IEnumerator<int> GetEnumerator()
        {
            for (int i = 0; i < this.stones.Count; i+=2)
            {
                yield return this.stones[i]; 
            }

            int startIndexToReturn = this.stones.Count % 2 == 0
                ? startIndexToReturn = this.stones.Count - 1
                : startIndexToReturn = this.stones.Count - 2;

            for (int i = startIndexToReturn; i >= 0; i -= 2)
            {
                yield return this.stones[i];
            }
        }
        IEnumerator IEnumerable.GetEnumerator() => this.GetEnumerator();
    }

    public class StartPtogram
    {
        public static void Main(string[] args)
        {
            int[] numbers = Console.ReadLine().Split(", ").Select(int.Parse).ToArray();

            Lake lake = new Lake(numbers);

            if(lake.Any())
            {
                Console.WriteLine(string.Join(", ", lake));
            }
        }
    }
}
