using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassPerson
{
    public class Person
    {
        public Person()
        {
            Name = "No name";
            Age = 1;
        }
        public Person(int age) : this()
        {
            Age = age;
        }
        public Person(string name, int age) : this(age)
        {
            Name = name;
            Age = age;
        }

        public string Name { get; set; }
        public int Age { get; set; }
    }

    public class Family
    {
        public Family()
        {
            FamilyMembers = new List<Person>();
        }
        public List<Person> FamilyMembers { get; set; }
        public void AddMember(Person member)
        {
            FamilyMembers.Add(member);
        }
        public Person GetOldestMember()  //4
        {
            return FamilyMembers.OrderByDescending(x => x.Age).FirstOrDefault();  //Сортирует элементы последовательности в порядке возрастания с использованием указанного компаратора.
        }                                                                         // Возвращает первый элемент последовательности или значение по умолчанию, если ни одного элемента не найдено.
        public void GetMoreThenThirty()
        {
            foreach (var member in FamilyMembers.OrderBy(x => x.Name))  //Сортирует элементы последовательности в порядке возрастания ключа.
            {
                if (member.Age > 30)
                {
                    Console.WriteLine($"{member.Name} - {member.Age}");
                }
            }
        }

    }

    public static class DateModifier
    {
        public static void CalculateDates(DateTime startDate, DateTime endDate)
        {
            TimeSpan days = endDate - startDate;  // Представляет интервал времени.
            Console.WriteLine(Math.Abs(days.Days));
        }
    }

    public class Engine  // паливо
    {
        public Engine(string model, int power)
        {
            Model = model;
            Power = power;
        }
        public Engine(int speed, int power)
        {
            Speed = speed;
            Power = power;
        }

        public string Model { get; set; }
        public int Speed { get; set; }
        public int Power { get; set; }
        public int Displacement { get; set; }
        public string Efficiency { get; set; }
    }

    public class Tire // шини
    {
        public Tire(double pressure, int age)
        {
            Pressure = pressure;
            Age = age;
        }

        public double Pressure { get; set; }
        public int Age { get; set; }

    }
    public class Cargo // вантаж
    {
        public Cargo(double weight, string type)
        {
            Weight = weight;
            Type = type;
        }

        public string Type { get; set; }
        public double Weight { get; set; }
    }

    public class Car
    {
        public Car(string model)
        {
            Model = model;
        }
        public Car(string model, double fuelAmount, double fuelConsumptionPerKilometer)
        {
            Model = model;
            FuelAmount = fuelAmount;
            FuelConsumptionPerKilometer = fuelConsumptionPerKilometer;
        }
        public Car(string model, Tire[] tires, Cargo cargo, Engine engine) : this(model)
        {

            Tires = tires;
            Cargo = cargo;
            Engine = engine;
        }


        public string Model { get; set; }
        public double FuelAmount { get; set; }
        public double FuelConsumptionPerKilometer { get; set; }
        public double TravelledDistance { get; set; }
        public Tire[] Tires { get; set; }
        public Cargo Cargo { get; set; }
        public Engine Engine { get; set; }
        public int Weight { get; set; }
        public string Color { get; set; }

        public void Drive(double distance)
        {
            double consumption = distance * FuelConsumptionPerKilometer;
            if ((FuelAmount - consumption) >= 0)
            {
                FuelAmount -= consumption;
                TravelledDistance += distance;
            }
            else
            {
                Console.WriteLine("Not enough fuel for the drive");
            }
        }
    }
        public class Start
       {
        static void Main(string[] args)
        {
            Console.WriteLine("Put down number of family members:");
            int members = int.Parse(Console.ReadLine());               // Parse - переробляє строку в число
            Family family = new Family();
            for (int i = 0; i < members; i++)
            {
                string[] read = Console.ReadLine().Split();
                Person person = new Person(read[0], int.Parse(read[1]));
                family.AddMember(person);
            }
            Console.WriteLine("The oldest person:");
            Person oldest = family.GetOldestMember();
            Console.WriteLine($"{oldest.Name} {oldest.Age}");
            Console.WriteLine();

            Console.WriteLine("Get more then thirty:");
            family.GetMoreThenThirty(); // 4

            Console.WriteLine("Put down dates:");
            DateTime startdate = DateTime.Parse(Console.ReadLine());  // 5
            DateTime enddate = DateTime.Parse(Console.ReadLine());
            DateModifier.CalculateDates(startdate, enddate);

            Console.WriteLine("Put down cars:");
            int carsCount = int.Parse(Console.ReadLine()); //6-8 +-
            List<Car> cars = new List<Car>();
            for (int i = 0; i < carsCount; i++)
            {
               string[] carDetails = Console.ReadLine().Split();  // Возвращает строковый массив, содержащий подстроки данного экземпляра, разделенные элементами заданной строки или массива знаков Юникода.
                Car car = new Car(carDetails[0], double.Parse(carDetails[1]) , double.Parse(carDetails[2]));
               cars.Add(car);
            }
            string input;
            while((input = Console.ReadLine()) != "End")
            {
               string[] currentCar = input.Split();
               Car car = new Car(currentCar[1], 0,0);
               Car car1 = cars.FirstOrDefault(c => c.Model == car.Model);
               int distance = int.Parse(currentCar[2]);
               car1.Drive(distance);
            }
            foreach (var car in cars)
            {
               Console.WriteLine($"{car.Model} {car.FuelAmount:f2} {car.TravelledDistance}");  // f - формат c плавающей запятой
                                                                                               // 2 - кол - во знаков после запятой
            }
        }
    }
}