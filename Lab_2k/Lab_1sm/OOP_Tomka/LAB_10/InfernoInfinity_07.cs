using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace InfernoInfinity_07
{
    // Камінчики
    public class Gem
    {
        private int strength;
        private int agility;
        private int vitality;
        private GemClarity clarity;

        protected Gem(string clarity, int str, int agi, int vit)
        {
            this.strength = str;
            this.agility = agi;
            this.vitality = vit;
            this.clarity = (GemClarity)Enum.Parse(typeof(GemClarity), clarity);
        }

        public Gem()
        {
            this.strength = 0; 
            this.agility = 0;
            this.vitality = 0;
            this.clarity = GemClarity.Empty;
        }

        public int Strength => this.strength + (int)clarity;

        public int Vitality => this.vitality + (int)clarity;

        public int Agility => this.agility + (int)clarity;
    }
    public class Amethyst : Gem
    {
        private const int BaseStrength = 2;
        private const int BaseAgility = 8;
        private const int BaseVitality = 4;

        public Amethyst(string clarity) : base(clarity, BaseStrength, BaseAgility, BaseVitality)
        {
        }
    }
    public class Emerald : Gem
    {
        private const int BaseStrength = 1;
        private const int BaseAgility = 4;
        private const int BaseVitality = 9;

        public Emerald(string clarity) : base(clarity, BaseStrength, BaseAgility, BaseVitality)
        {
        }
    }
    public class Ruby : Gem
    {
        private const int BaseStrength = 7;
        private const int BaseAgility = 2;
        private const int BaseVitality = 5;

        public Ruby(string clarity) : base(clarity, BaseStrength, BaseAgility, BaseVitality)
        {
        }
    }

    public abstract class Weapon
    {
        private int minDamage;
        private int maxDamage;
        private Gem[] gems;
        private WeaponRarity rarity;
        private string name;

        protected Weapon(string name, string rarity, int minDmg, int maxDmg, int amountOfSockets)
        {
            this.name = name;
            this.minDamage = minDmg;
            this.maxDamage = maxDmg;
            this.gems = new Gem[amountOfSockets];
            for (int i = 0; i < gems.Length; i++)
            {
                gems[i] = new Gem();
            }
            this.rarity = (WeaponRarity)Enum.Parse(typeof(WeaponRarity), rarity);
        }

        public int Strength => this.gems.Sum(g => g.Strength);
        public int Agility => this.gems.Sum(g => g.Agility);
        public int Vitality => this.gems.Sum(g => g.Vitality);

        public void AddGem(int index, Gem gem)
        {
            if (index >= 0 && index < this.gems.Length)
            {
                this.gems[index] = gem;
            }
        }

        public void RemoveGem(int index)
        {
            if (index >= 0 && index < this.gems.Length)
            {
                this.gems[index] = new Gem();
            }
        }

        public int GetMinDamage()
        {
            var totalMinDamage = 0;

            totalMinDamage = this.minDamage * (int)this.rarity;
            totalMinDamage += 2 * this.Strength;
            totalMinDamage += this.Agility;

            return totalMinDamage;
        }

        public int GetMaxDamage()
        {
            var totalMaxDamage = 0;

            totalMaxDamage = this.maxDamage * (int)this.rarity;
            totalMaxDamage += 3 * this.Strength;
            totalMaxDamage += 4 * this.Agility;

            return totalMaxDamage;
        }

        public override string ToString()
        {
            //"{weapon's name}: {min damage}-{max damage} Damage, +{points} Strength, +{points} Agility, +{points} Vitality"
            return $"{this.name}: {this.GetMinDamage()}-{this.GetMaxDamage()} Damage, +{this.Strength} Strength, +{this.Agility} Agility, +{this.Vitality} Vitality";
        }
    }

    public enum GemClarity
    {
        Empty = 0,
        Chipped = 1,
        Regular = 2,
        Perfect = 5,
        Flawless = 10
    }
    public enum WeaponRarity
    {
        Common = 1,
        Uncommon = 2,
        Rare = 3,
        Epic = 5
    }
}
