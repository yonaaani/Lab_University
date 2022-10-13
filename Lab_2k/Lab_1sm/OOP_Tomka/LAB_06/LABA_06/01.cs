using System;
using System.Collections.Generic;
using System.Text;

namespace Person_01
{
    public class Person
    {
        private int age;

        public Person(string name, int age)
        {
            this.Name = name;
            this.Age = age;
        }

        public string Name { get; set; }

        public virtual int Age 
        { 
            get
            {
                return this.age;
            }
            set
            {
                if(value<=0)
                {
                    throw new ArgumentOutOfRangeException("Age cannot be negative");
                }
                this.age = value;
            }
        }

        public override string ToString()
        {
            StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.Append($"Name: {this.Name},Age: {this.Age}");
            return stringBuilder.ToString();
        }
    }

    public class Child : Person
    {
        public Child(string name, int age) : base(name, age) { }

        public override int Age
        {
            get
            {
                return base.Age;
            }
            set
            {
                if(value>15)
                {
                    throw new ArgumentOutOfRangeException("Age cannot be grater than 15");
                }
                base.Age = value;
            }
        }
    }

    public class Start
    {
        public static void Main(string[] args)
        {
            string name = Console.ReadLine();
            int age = int.Parse(Console.ReadLine());
            Person person;
               
            if(age<=15)
            {
                person=new Child(name, age);
            }
            else
            {
                person = new Person(name, age);
            }

            Console.WriteLine(person);
        }
    }

}
