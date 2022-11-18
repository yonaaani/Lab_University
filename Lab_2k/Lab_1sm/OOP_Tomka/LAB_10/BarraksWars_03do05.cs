using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace BarraksWars_03do05
{
    public class Unit
    {
        private int health;
        private int attackDamage;

        protected Unit(int health, int attackDamage)
        {
            this.SetInitialHealth(health);
            this.AttackDamage = attackDamage;
        }

        public int Health
        {
            get
            {
                return this.health;
            }

            set
            {
                if (value < 0)
                {
                    this.health = 0;
                }
                else
                {
                    this.health = value;
                }
            }
        }

        private void SetInitialHealth(int health)
        {
            if (health <= 0)
            {
                throw new ArgumentException("Health should be positive.");
            }

            this.Health = health;
        }

        public int AttackDamage
        {
            get
            {
                return this.attackDamage;
            }

            private set
            {
                if (value <= 0)
                {
                    throw new ArgumentException("Attack damage should be positive.");
                }

                this.attackDamage = value;
            }
        }
    }

    // Ініціалізація персонажів
    public class Archer : Unit //лучник
    {
        private const int DefaultHealth = 25;
        private const int DefaultDamage = 7;

        public Archer() : base(DefaultHealth, DefaultDamage)
        {
        }
    }

    public class Gunner : Unit //із зброї стріляє
    {
        private const int DefaultHealth = 20;
        private const int DefaultDamage = 20;

        public Gunner()
            : base(DefaultHealth, DefaultDamage)
        {
        }
    }

    public class Horseman : Unit 
    {
        private const int DefaultHealth = 20;
        private const int DefaultDamage = 20;

        public Horseman()
            : base(DefaultHealth, DefaultDamage)
        {
        }
    }

    public class Pikeman : Unit //зі списом
    {
        private const int DefaultHealth = 30;
        private const int DefaultDamage = 15;

        public Pikeman()
            : base(DefaultHealth, DefaultDamage)
        {

        }
    }

    public class Swordsman : Unit
    {
        private const int DefaultHealth = 40;
        private const int DefaultDamage = 13;

        public Swordsman()
            : base(DefaultHealth, DefaultDamage)
        {

        }
    }

    // Ініціалізація команд
    public abstract class Command : IExecutable
    {
        private string[] data;

        public Command(string[] data)
        {
            this.Data = data;
        }

        protected string[] Data
        {
            get { return data; }
            set { data = value; }
        }

        public abstract string Execute();

    }

    [AttributeUsage(AttributeTargets.Field, AllowMultiple = true)]
    public class InjectAttribute : Attribute
    {
    }
    public class AddCommand : Command
    {
        [Inject]
        private IRepository repository;
        [Inject]
        private IUnitFactory unitFactory;

        public AddCommand(string[] data)
            : base(data)
        {
        }

        public override string Execute()
        {
            string unitType = this.Data[1];
            IUnit unitToAdd = this.unitFactory.CreateUnit(unitType);
            this.repository.AddUnit(unitToAdd);
            string output = unitType + " added!";
            return output;
        }
    }

    public class FightCommand : Command
    {
        public FightCommand(string[] data)
            : base(data)
        {
        }

        public override string Execute()
        {
            Environment.Exit(0);
            return string.Empty;
        }
    }

    public class ReportCommand : Command
    {
        [Inject]
        private IRepository repository;

        public ReportCommand(string[] data)
            : base(data)
        {
        }

        public override string Execute()
        {
            string output = this.repository.Statistics;
            return output;
        }
    }
    public class RetireCommand : Command
    {
        [Inject]
        private IRepository repository;

        public RetireCommand(string[] data)
            : base(data)
        {
        }

        public override string Execute()
        {
            var unitToRemove = this.Data[1];
            this.repository.RemoveUnit(unitToRemove);
            return $"{unitToRemove} retired!";
        }
    }
    // Інтерфейси

    public interface IAttacker
    {
        int AttackDamage { get; }
    }

    public interface IDestroyable
    {
        int Health { get; set; }
    }
    public interface IExecutable
    {
        string Execute();
    }
    public interface IRunnable
    {
        void Run();
    }

    public interface IUnit : IDestroyable, IAttacker
    {

    }

    public interface IUnitFactory
    {
        IUnit CreateUnit(string unitType);
    }

    public interface IRepository
    {
        void AddUnit(IUnit unit);
        string Statistics { get; }
        void RemoveUnit(string unitType);
    }
    public interface ICommandInterpreter
    {
        IExecutable InterpretCommand(string[] data, string commandName);
    }
}
