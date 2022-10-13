using System;
using System.CodeDom;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassBox01_02
{
     class Box
    {
        private double length { get; set; }
        private double width { get; set; }
        private double height { get; set; }

        public Box(double length, double width, double height)
        {
            this.Length = length;
            this.Width = width;
            this.Height = height;
        }
        public double Length
        {
            get => this.length;
            private set
            {
                this.ThrowIfInvalidSide(value, nameof(this.Length));
                this.length = value;
            }
        }

        public double Width
        {
            get => this.width;
            private set
            {
                this.ThrowIfInvalidSide(value, nameof(this.Width));
                this.width = value;
            }
        }
        public double Height
        {
            get => this.height;
            private set
            {
                this.ThrowIfInvalidSide(value, nameof(this.Height));
                this.height = value;
            }
        }

        private void ThrowIfInvalidSide(double value, string propertyName)  //викинути, якщо б хоча б якийсь розмір заданий - невірний, тобто 0 або від'ємний
        {
            if (value <= 0)
            {
                throw new ArgumentException($"{propertyName} cannot be zero or negative.");  // throw - для створення вийнятку
            }
        }

        public double Volume()  // об'єм
        {
            return (this.Length * this.Width * this.Height);
        }

        public double SurfaceArea()  // Площа повної поверхні
        {
            return ((2 * this.Length * this.Width) + (2 * this.Length * this.Height) + (2 * this.Width * this.Height));
        }

        public double LateralSurfaceArea() // Площа бічної поверхні
        {
            return ((2 * this.Length * this.Height) + (2 * this.Width * this.Height));
        }
    }

    public class Start
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Put down length, wudth, height: ");
            var length = double.Parse(Console.ReadLine());
            var width = double.Parse(Console.ReadLine());
            var height = double.Parse(Console.ReadLine());

            try
            {
                Box box = new Box(length, width, height);
                Console.WriteLine($"Volume: { box.Volume():f2}");
                Console.WriteLine($"Surface Area: { box.SurfaceArea():f2}");
                Console.WriteLine($"Lateral Surface Area: { box.LateralSurfaceArea():f2}");
            }
            catch (ArgumentException x)
            {
                Console.WriteLine(x.Message);
            }
            Console.ReadLine();
            Console.WriteLine();
        }
    }
    
}

namespace AnimalFarm_03
{
    class Chiken
    {
        private string name;
        private int age;


        public Chiken(string name, int age)
        {
            this.Name = name;
            this.Age = age;
        }

        public string Name
        {
            get => name;
            set
            {
                if (NotNull(name))
                {
                    name = value;
                }
                else
                {
                    throw new System.ArgumentException("Name not valid");  // ім'я недійсне
                }
            }
        }

        public int Age
        {
            get => age;
            set
            {
                if (value < 0 || value > 15)
                {
                    throw new System.ArgumentException("Age can be between 0 and 15");  //в інеті пише що кури живуть в середньому 15 років?
                }
                this.age = value;
            }
        }

        private bool NotNull(string Validate) //перевірка
        {
            return string.IsNullOrEmpty(Validate) & string.IsNullOrWhiteSpace(Validate);
        }

        // 2 part

        private int CalculateProductPerDay(int chiken_age)
        {
            if (chiken_age < 1)
            {
                Console.WriteLine("Chiken doesn`t produce any ages at this age :( ");
                return 0;
            }
            else
            {
                if (chiken_age > 1 && chiken_age < 10)
                {
                    return 3;
                }
                else
                    return 1;
            }
        }

        public int ProductPerDay
        {
            get
            {
                return CalculateProductPerDay(age);
            }
        }

        class Start
        {
            static void Main(string[] args)
            {
                Console.WriteLine("Enter the chiken name and age:");

                var cmdArgs = Console.ReadLine().Split();
                Chiken chiken = new Chiken(cmdArgs[0], int.Parse(cmdArgs[1]));
                Console.WriteLine($"Chiken {chiken.Name} age of {chiken.Age} can produce {chiken.ProductPerDay} per day");
                Console.WriteLine();
            }
        }
    }
}

namespace Shopping_Spree_04
{
    public class Person
    {
        private string name;
        private decimal money;
        private readonly List<Product> products;
        public Person(string name, decimal money)
        {
            this.Name = name;
            this.Money = money;
            this.products = new List<Product>();
        }

        public IReadOnlyCollection<Product> ProductsCollection
            => this.products;

        public string Name
        {
            get
            {
                return name;
            }
            private set
            {
                if(string.IsNullOrWhiteSpace(value))
                {
                    throw new ArgumentException("Wrong name");
                }
                name = value;
            }
        }

        public decimal Money
        {
            get
            {
                return money;
            }
            private set
            {
                if(value<0)
                {
                    throw new ArgumentException("Money cannot be negative");
                }
                money = value;
            }
        }

        public bool AddProduct(Product product)
        {
            if(this.Money - product.Price < 0)
            {
                return false;
            }
            products.Add(product);
            this.Money -= product.Price;
            return true;
        }

    }

    public class Product
    {
        private string name;
        private decimal price;

        public Product(string name, decimal price)
        {
            this.Name=name;
            this.Price = price;
        }

        public string Name
        {
            get
            {
                return name;
            }
            private set
            {
                if(string.IsNullOrWhiteSpace(value))
                {
                    throw new ArgumentException("Wrong name");
                }
                name = value;
            }
        }

        public decimal Price
        {
            get 
            { 
                return price; 
            }
            private set
            {
                if(value<0)
                {
                    throw new ArgumentException("Money cannot be negative");
                }
                price = value;
            }
        }
    }

    public class Start
    {
        public static void Main(string[] args)
        {
            Dictionary<string, Person> personI = new Dictionary<string, Person>();
            Dictionary<string, Product> productI = new Dictionary<string, Product>();

            try
            {
                string[] people = Console.ReadLine().Split(new char[] { '=',';' }, StringSplitOptions.RemoveEmptyEntries);
                //Розділити рядок на максимальну кількість підрядків на основі масиву символів, переданого як параметр. Ви можете вказати, чи включати порожні елементи масиву в масив підрядків чи ні.
                //RemoveEmptyEntries - Исключить элементы массива, содержащие пустые строки, из результата.
               for(int i = 0; i < people.Length; i+=2)
                {
                    string name = people[i];
                    decimal money = decimal.Parse(people[i+1]);

                    Person person = new Person(name, money);
                    personI.Add(name, person);
                }

               string[] products = Console.ReadLine().Split(new char[] { '=', ';' }, StringSplitOptions.RemoveEmptyEntries);
                for (int i = 0; i < people.Length; i += 2)
                {
                    string name = products[i];
                    decimal price = decimal.Parse(products[i + 1]);

                   Product product = new Product(name, price);
                    productI.Add(name, product);
                }


                string command = Console.ReadLine();

                while(command != "END")
                {
                    string[] commandInfo = command.Split("", StringSplitOptions.RemoveEmptyEntries);

                    string personName = commandInfo[0];
                    string productName = commandInfo[1];

                    Person person = personI[personName];
                    Product product = productI[productName];

                    bool IsAdded = person.AddProduct(product);

                    if(!IsAdded)
                    {
                        Console.WriteLine($"{personName} can`t afford {productName}");
                    }
                    else
                    {
                        Console.WriteLine($"{personName} bought {productName}");
                    }
                    command = Console.ReadLine();
                }

                foreach(var (name,person ) in personI)
                {
                    string productInfo = person.ProductsCollection.Count > 0 ? string.Join(",", person.ProductsCollection.Select(x => x.Name))
                        : "Nothing bought";

                    Console.WriteLine($"{name}-{productInfo}");

                }
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }

        }
    }

}

namespace PizzaCalories_05
{
    public class Dough
    {
        private string flourType; // тип муки
        private string bakingTechnique; //техніка приготування
        private int weight; //вага

        public Dough(string flourType,string bakingTechnique,int weight)
        {
            this.FlourType = flourType;
            this.BakingTechnique = bakingTechnique;
            this.Weight = weight;
        }

        public string FlourType
        {
            get
            {
                return flourType;
            }
            private set
            {
                if(!Helper.Modifier.ContainsKey(value.ToLower()))
                {
                    throw new ArgumentException("Wrong type of dough");
                }
                flourType = value;
            }
        }
        public string BakingTechnique
        {
            get
            {
                return bakingTechnique;
            }
            private set
            {
                if (!Helper.Modifier.ContainsKey(value.ToLower()))
                {
                    throw new ArgumentException("Wrong type of dough");
                }
                bakingTechnique = value;
            }
        }
        public int Weight
        {
            get
            {
                return weight;
            }
            private set
            {
                if(value <1 || value > 200)
                {
                    throw new ArgumentException("Dough weight should be in the range [1..200]");
                }
                weight = value;
            }
        }


        // // Грами => Грами * 2 * модифікатори
        public double Calories
            => 2
            * this.Weight
            * Helper.Modifier[FlourType.ToLower()]
            * Helper.Modifier[BakingTechnique.ToLower()];
    }

    public static class Helper
    {
        public static Dictionary<string, double> Modifier
            => new Dictionary<string, double>
            {
                {"white", 1.5 },
                {"wholegrain", 1.0 },
                {"crispy",0.9 },
                {"chewy",1.1 },
                {"homemade",1.0 },
                {"meat",1.2 },
                {"veggies",0.8 },
                {"cheese",1.1 },
                {"sause",0.9 },
            };
            
    }

    public class Topping
    {
        private string toppingType;
        private int weight;
        
        public Topping(string toppingType, int weight)
        {
            this.ToppingType = toppingType;
            this.Weight = weight;
        }

        public string ToppingType
        {
            get
            {
                return toppingType;
            }
            private set
            {
                if (!Helper.Modifier.ContainsKey(value.ToLower()))
                {
                    throw new ArgumentException("Cannot place {value} on top of your pizza");
                }
                toppingType = value;
            }
        }
        public int Weight
        {
            get
            {
                return weight;
            }
            set
            {
                if(value<1 || value>50)
                {
                    throw new ArgumentException($"{ToppingType} weight should be in the range [1..50]");
                }
                weight = value;
            }
        }
        public double Calories
            => 2
            * Weight
            * Helper.Modifier[ToppingType.ToLower()];
    }

    public class Pizza
    {
        private string name;
        private List<Topping> toppings;
        
        public Pizza(string name, Dough dough)
        {
            this.Name = name;
            this.Dough = dough;
            toppings = new List<Topping>();
        }

        public string Name
        {
            get
            {
                return name;
            }
            set
            {
                if(string.IsNullOrWhiteSpace(value) || value.Length <1 || value.Length>15)
                {
                    throw new ArgumentException("Pizza name should be between 1 and 15 symbols");
                }
                name = value;
            }
        }

        public Dough Dough
        {
            get;
            private set;
        }

        public void AddTopping(Topping topping)
        {
            if(toppings.Count == 10)
            {
                throw new ArgumentException("Number of toppings should be in range [0..10]");
            }
            toppings.Add(topping);
        }

        public double Calories
            => this.Dough.Calories + toppings.Sum(x => x.Calories);
    }

    public class Start
    { 
     static void Main(string[] args)
        {
            string[] pizzaInfo = Console.ReadLine().Split(" ", StringSplitOptions.RemoveEmptyEntries);
            string name = pizzaInfo[1];

            string[] doughInfo = Console.ReadLine().Split();

            string flourType = doughInfo[1];
            string bakingTechnique = doughInfo[2];
            int weight = int.Parse(doughInfo[3]);

            try
            {
                Dough dough = new Dough(flourType, bakingTechnique, weight);

                Pizza pizza = new Pizza(name, dough);

                string input = Console.ReadLine();
                while (input != "END")
                {
                    string[] toppingInfo = input.Split(" ", StringSplitOptions.RemoveEmptyEntries);
                    string toppingType = toppingInfo[1];
                    int toppingWeight = int.Parse(toppingInfo[2]);

                    Topping topping = new Topping(toppingType, toppingWeight);

                    pizza.AddTopping(topping);

                    input = Console.ReadLine();
                }

                Console.WriteLine($"{pizza.Name} - {pizza.Calories:F2} Calories.");
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
    }

}