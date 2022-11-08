using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PetClinics_08
{
    public class Pet
    {
        public Pet(string name, int age, string kind)
        {
            this.Name = name;
            this.Age = age;
            this.Kind = kind;
        }

        public string Name { get; set; }
        public int Age { get; set; }
        public string Kind { get; set; }

        public override string ToString()
        {
            return $"{this.Name} {this.Age} {this.Kind}";
        }
    }

    public class Clinic
    {
        private string name;
        private Pet[] rooms;

        public Clinic(string name, int roomsCount)
        {
            this.Name = name;
            this.Rooms = new Pet[roomsCount];
        }
        public string Name
        {
            get
            {
                return name;
            }
            set
            {
                name = value;
            }
        }
        public Pet[] Rooms
        {
            get
            {
                return rooms;
            }
            private set
            {
                if (value.Length % 2 == 0)
                {
                    throw new InvalidOperationException("Invalid Operation!");
                }

                this.rooms = value;
            }
        }
    }
}
