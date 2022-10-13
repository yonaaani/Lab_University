using System;
using System.Collections.Generic;
using System.Text;

namespace MordorsCruelPlan_05
{
        class Food
        {
            public string name;
            public int happinesPoint;

            public Food(string name)
            {
                this.name = name;
            }
        }

        class Cram : Food
        {
            public Cram(string name) : base(name)
            {
                base.happinesPoint = 2;
            }
        }

        class Lembas : Food
        {
            public Lembas(string name) : base(name)
            {
                base.happinesPoint = 3;
            }
        }
        class Apple : Food
        {
            public Apple(string name) : base(name)
            {
                base.happinesPoint = 1;
            }
        }
        class Melon : Food
        {
            public Melon(string name) : base(name)
            {
                base.happinesPoint = 1;
            }
        }
        class HoneyCake : Food
        {
            public HoneyCake(string name) : base(name)
            {
                base.happinesPoint = 5;
            }
        }
        class Mushrooms : Food
        {
            public Mushrooms(string name) : base(name)
            {
                base.happinesPoint = -10;
            }
        }
        class EverythingElse : Food
        {
            public EverythingElse(string name) : base(name)
            {
                base.happinesPoint = -1;
            }
        }



    class MoodFactory 
    {
        static void Main(string[] args)
        {
            int happines = 0;
            string[] food = Console.ReadLine().Split(' ', StringSplitOptions.RemoveEmptyEntries).ToArray();

            for (int i = 0; i < food.Length; i++)
            {
                switch(food[i].ToLower())
                {
                    case "apple":
                        {
                            Apple apple = new Apple(food[i]);
                            happines += apple.happinesPoint;
                            break;
                        }
                    case "cram":
                        {
                            Cram cram = new Cram(food[i]);
                            happines += cram.happinesPoint;
                            break;
                        }
                    case "lembas":
                        {
                            Lembas lembas = new Lembas(food[i]);
                            happines += lembas.happinesPoint;
                            break;
                        }
                    case "melon":
                        {
                            Melon melon = new Melon(food[i]);
                            happines += melon.happinesPoint;
                            break;
                        }
                    case "honeycake":
                        {
                            HoneyCake honeyCake = new HoneyCake(food[i]);
                            happines += honeyCake.happinesPoint;
                            break;
                        }
                    case "mushrooms":
                        {
                            Mushrooms mushrooms = new Mushrooms(food[i]);
                            happines += mushrooms.happinesPoint;
                            break;
                        }
                    default:
                        {
                            EverythingElse everythingElse = new EverythingElse(food[i]);
                            happines += everythingElse.happinesPoint;
                            break;
                        }
                }

                Console.WriteLine(happines);
                    if(happines < -5)
                    {
                        Console.WriteLine("Angry");
                    }
                    if(happines >= -5 && happines<=0)
                    {
                        Console.WriteLine("Sad");
                    }
                    if(happines >= 1 && happines <= 15)
                    {
                        Console.WriteLine("Happy");
                    }
                    if(happines>15)
                    {
                    Console.WriteLine("JavaScript");
                    }
            }
        }
    }
   
}
