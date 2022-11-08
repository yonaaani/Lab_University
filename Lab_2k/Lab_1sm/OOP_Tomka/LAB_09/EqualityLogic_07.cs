using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace EqualityLogic_07
{
    public class Person : IComparable<Person>
    {
        public string name;
        public int age;

        public Person(string name, int age)
        {
            this.Name = name;
            this.Age = age;
        }
        public string Name
        {
            get { return this.name; }
            private set { this.name = value; }
        }
        public int Age
        {
            get { return this.age; }
            private set { this.age = value; }
        }

        public int CompareTo(Person other) //Сравнивает данный экземпляр с заданным объектом или строкой
                                           //String и возвращает целое число, которое показывает, расположен ли данный экземпляр перед, после или на той же позиции
                                           //в порядке сортировки, что и заданный объект или строка String
        {
            int result = this.Name.CompareTo(other.Name);
            if (result == 0)
            {
                result = this.Age.CompareTo(other.Age);
            }
            return result;
        }

        public override bool Equals(object obj) //визначає, чи вказаний об'єкт дорівнює поточному об'єкту.
        {
            if(obj is Person)
                {
                Person person = obj as Person;

                if (this.Name == person.Name && this.Age == person.Age)
                {
                    return true;
                }
            }
            return false;
        }

        // Метод GetHashCode надає цей хеш-код для алгоритмів,
        // які потребують швидкої перевірки рівності об’єктів
        public override int GetHashCode()
        {
            return this.Name.GetHashCode() + this.Age.GetHashCode();
        }
    }

    public class StartProgram
    {
        public static void Main(string[] args)
        {
            HashSet<Person> people = new HashSet<Person>();
            SortedSet<Person> sortedpeople = new SortedSet<Person>();

            int numberOfLines = int.Parse(Console.ReadLine());

            for(int i = 0; i < numberOfLines; i++)
            {
                string[] elements = Console.ReadLine().Split(' ').ToArray();

                string name = elements[0];
                int age = int.Parse(elements[1]);

                Person person = new Person(name, age);

                people.Add(person);
                sortedpeople.Add(person);
            }

            Console.WriteLine(people.Count);
            Console.WriteLine(sortedpeople.Count);
        }
    }
}
