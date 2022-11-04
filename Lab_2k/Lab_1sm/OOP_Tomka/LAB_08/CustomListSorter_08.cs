using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CustomListSorter_08
{
    class CustomList<T> where T : IComparable<T>
    {
        public List<T> Data;

        public CustomList()
        {
            Data = new List<T>();
        }

        public void Add(T element)
        {
            Data.Add(element);
        }

        public T Remove(int index)
        {
            T element = Data[index];
            Data.RemoveAt(index); //з нульового елемнта, який треба видалити

            return element;
        }

        public bool Contains(T element)
        {
            return Data.Contains(element);
        }

        public void Swap(int index1, int index2)
        {
            T temp = Data[index1];
            Data[index1] = Data[index2];
            Data[index2] = temp;
        }

        public int CountGreaterThan(T element)
        {
            return Data.Count(e => e.CompareTo(element) > 0);
        }

        public T Max()
        {
            return Data.Max();
        }

        public T Min()
        {
            return Data.Min();
        }

        public void Sort()
        {
            Data.Sort();
        }

        /* public string Print()
         {
             var result = new StringBuilder();

             foreach (var data in Data)
             {
                 result.Append(data + Environment.NewLine);
             }

             return result.ToString().TrimEnd();
         }
     }*/
    }
        public static class Sorter
        {
            public static void Sort<T>(List<T> List) where T : IComparable<T>
            {
                List.Sort();
            }
        }

        class StartProgram
        {
            static void Main(string[] args)
            {
                var list = new List<string>();

                string command;

                while ((command = Console.ReadLine()) != "End")
                {
                    string[] input = command.Split();

                    switch (input[0])
                    {
                        case "Add":
                            {
                                list.Add(input[1]);
                                break;
                            }
                        case "Remove":
                            {
                                list.Remove(input[1]);
                                break;
                            }
                        case "Contains":
                            {
                                Console.WriteLine(list.Contains(input[1]));
                                break;
                            }
                        case "Swap":
                            {
                                list.Swap(Convert.ToInt32(input[1]), Convert.ToInt32(input[2]));
                                break;
                            }
                        case "Greater":
                            {
                                Console.WriteLine(list.CountGreaterThan(input[1]));
                                break;
                            }
                        case "Max":
                            {
                                Console.WriteLine(list.Max());
                                break;
                            }
                        case "Min":
                            {
                                Console.WriteLine(list.Min());
                                break;
                            }
                        case "Sort":
                            Sorter.Sort(list);
                            break;
                        //case "Print":
                        //Console.WriteLine(list.Print());
                        //break;
                        default:
                            throw new ArgumentException();
                    }
                }
            }
        }

    
}



