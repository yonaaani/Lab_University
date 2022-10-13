using System;
using System.Collections.Generic;
using System.Text;

namespace Animal_06
{
    class Animal
    {
        private string name;
        private string typeOfAnimal;
        private int age;
        private string gender;

        public Animal(string name, int age, string gender)
        {
            this.Name = name;
            this.Age = age;
            this.Gender = gender;
        }
        public Animal(string name, string typeOfAnimal, int age, string gender) : this(name,age,gender)
        {
            this.TypeOfAnimal = typeOfAnimal;
        }

        public string Name
        {
            get
            {
                return name;
            }
            set
            {
                if(string.IsNullOrEmpty(value) || string.IsNullOrWhiteSpace(value))
                {
                    throw new ArgumentException("Invalid name");
                }
                name = value;
            }
        }

        public int Age
        {
            get
            {
                return age;
            }
            set
            {
                if(value < 0)
                {
                    throw new ArgumentException("Invalid age");
                }
                age = value;
            }
        }

        public string Gender
        {
            get
            {
                return gender;
            }
            set
            {
                if (string.IsNullOrEmpty(value) || string.IsNullOrWhiteSpace(value))
                {
                    throw new ArgumentException("Invalid name");
                }
                gender = value;
            }
        }

        public string TypeOfAnimal
        {
            get
            {
                return typeOfAnimal;
            }
            set
            {
                if (string.IsNullOrEmpty(value) || string.IsNullOrWhiteSpace(value))
                {
                    throw new ArgumentException("Invalid name");
                }
                typeOfAnimal = value;
            }
        }

        public virtual string ProduceSound()
        {
            return "";
        }

        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.AppendLine(this.GetType().Name);
            sb.AppendLine($"{this.name}, { this.age}, {this.gender}");
            sb.AppendLine(this.ProduceSound());

            return sb.ToString();
        }
    }

    class Cat : Animal
    {
        public Cat(string name, int age, string gender) : base(name, age, gender)
        {

        }

        public override string ProduceSound()
        {
            return "Meow meow";
        }
    }
    class Tomcat : Cat
    {
        public Tomcat(string name, int age, string gender = "Male") : base(name, age, gender)
        {
            base.Gender = "Male";
        }

        public override string ProduceSound()
        {
            return "MEOW";
        }
    }
    class Kitten : Cat
    {
        public Kitten(string name, int age, string gender = "Male") : base(name, age, gender)
        {
            base.Gender = "Female";
        }

        public override string ProduceSound()
        {
            return "Meow";
        }
    }

    class Dog : Animal
    {
        public Dog(string name, int age, string gender) : base(name, age, gender)
        {

        }

        public override string ProduceSound()
        {
            return "Woof!";
        }
    }
    class Frog : Animal
    {
        public Frog(string name, int age, string gender) : base(name, age, gender)
        {

        }

        public override string ProduceSound()
        {
            return "Ribbit";
        }
    }

    class Start
    { 
    static void Main(string[] args)
        {
            while(true)
            {
                string inp = Console.ReadLine();
                if(inp == "Beast!")
                {
                    break;
                }

                try 
                { 
                var tokens = Console.ReadLine().Split();
                    var animal = CreatingAnimal(inp, tokens);
                    Console.WriteLine(animal);

                }
                catch (Exception e)
                {
                    Console.WriteLine(e.Message);
                }
            }
        }
                private static object CreatingAnimal(string input, string[] tokens)
                {

                    string name = tokens[0];
                    int age = int.Parse(tokens[1]);
                    string gender = tokens[2];

                    switch (input)
                    {
                        case "Cat":
                            return new Cat(name, age, gender);
                        case "Dog":
                            return new Dog(name, age, gender);
                        case "Frog":
                            return new Frog(name, age, gender);
                        case "Tomcat":
                            return new Tomcat(name, age, gender);
                        case "Kitten":
                            return new Kitten(name, age, gender);
                        default:
                            throw new ArgumentException("Invalid input!");
                    }

                }
        
    }
}
    
    
    

