using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ComparingObjects_05
{
    public class Person : IComparable<Person>
    {
        private string name;
        private int age;
        private string town;

        public Person(string name, int age, string town)
        {
            this.Name = name;
            this.Age = age;
            this.Town = town;
        }

        public string Name
        {
            get
            {
                return this.name;
            }
            private set 
            { 
                this.name = value; 
            }
        }

        public int Age
        {
            get
            {
                return this.age;
            }
            private set
            {
                this.age = value;
            }
        }

        public string Town
        {
            get
            {
                return this.town;
            }
            private set
            {
                this.town = value;
            }
        }

        public int CompareTo(Person other)
        {
            int result = this.Name.CompareTo(other.Name);

            if (result == 0)
            {
                result = this.Age.CompareTo(other.Age);

                if (result == 0)
                {
                    result = this.Town.CompareTo(other.Town);
                }
            }

            return result;
        }
    }

    public class StartUp
    {
        public static void Main(string[] args)
        {
            List<Person> people = new List<Person>();

            string input = string.Empty;

            while ((input = Console.ReadLine()) != "END")
            {
                string[] elements = input.Split(" ").ToArray();

                string name = elements[0];
                int age = int.Parse(elements[1]);
                string town = elements[2];

                Person person = new Person(name, age, town);
                people.Add(person);
            }

            int numberTargetPerson = int.Parse(Console.ReadLine());

            Person targetPerson = people[numberTargetPerson - 1];

            int counterEqualPeople = 0;
            int counterNotEqualPeople = 0;

            foreach (Person person in people)
            {
                bool areEqual = person.CompareTo(targetPerson) == 0;
                if (areEqual)
                {
                    counterEqualPeople++;
                }
                else
                {
                    counterNotEqualPeople++;
                }
            }

            bool areFound = counterEqualPeople > 1;
            if (areFound)
            {
                Console.WriteLine($"{counterEqualPeople} {counterNotEqualPeople} {people.Count}");
            }
            else
            {
                Console.WriteLine("No matches");
            }
        }
    }
}
