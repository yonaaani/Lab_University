using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace KingsGambit_02_05
{
    public abstract class Person
    {
        public Person(string name)
        {
            this.Name = name;
        }

        public string Name { get; private set; }
    }

    public class Footman : Person, IDefender //лакей
    {
        public Footman(string name) : base(name) { }

        public void DefendTheKing()
        {
            Console.WriteLine($"Footman {this.Name} is panicking!");
        }
    }

    public delegate void KingIsAttackedEventHandler();

    public class King : Person, IAttackable
    {
          public King(string name) : base(name) { }
           
          public event KingIsAttackedEventHandler KingIsAttacked;

          public void RespondToAttack()
        {
            Console.WriteLine($"King {this.Name} is under attack!");
            this.KingIsAttacked?.Invoke();
        }
    }
    public class RoyalGuard : Person, IDefender
    {
        public RoyalGuard(string name) : base(name){ }

        public void DefendTheKing()
        {
            Console.WriteLine($"Royal Guard {this.Name} is defending!");
        }
    }

    // Contracts
    public interface IAttackable
    {
        void RespondToAttack();
    }
    public interface IDefender
    {
        void DefendTheKing();
    }

    public class StartUp
    {
        public static void Main()
        {
            string kingsName = Console.ReadLine();
            King king = new King(kingsName);

            var royalGuardsNames = Console.ReadLine().Split(" ");

            var footmenNames = Console.ReadLine().Split(" ");

            var defenders = new List<Person>();

            foreach (var name in royalGuardsNames)
            {
                RoyalGuard guard = new RoyalGuard(name);
                defenders.Add(guard);
                king.KingIsAttacked += guard.DefendTheKing;
            }

            foreach (var name in footmenNames)
            {
                Footman footman = new Footman(name);
                defenders.Add(footman);
                king.KingIsAttacked += footman.DefendTheKing;
            }

            while (true)
            {
                var input = Console.ReadLine().Split();
                var command = input[0];

                switch (command)
                {
                    case "Kill":
                        string name = input[1];
                        Person defender = defenders.First(s => s.Name == name);
                        defenders.Remove(defender);
                        king.KingIsAttacked -= ((IDefender)defender).DefendTheKing;
                        break;

                    case "Attack":
                        king.RespondToAttack();
                        break;

                    case "End":
                        return;
                }
            }
        }
    }
}

