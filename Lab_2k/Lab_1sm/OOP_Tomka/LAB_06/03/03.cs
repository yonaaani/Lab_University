using System;
using System.Collections.Generic;
using System.Text;

namespace Mankid_03
{
    public class Human
    {
        private string firstName;
        private string lastName;

        public Human(string firstName, string lastName)
        {
            this.FirstName = firstName;
            this.LastName = lastName;
        }

        public string FirstName
        {
            get
            {
                return firstName;
            }
            set
            {
                if (!char.IsUpper(value[0]))
                {
                    throw new ArgumentException("Expected upper case letter! Argument: firstName");
                }
                if (value.Length < 4)
                {
                    throw new ArgumentException("Expected length at least 4 symbols! Argument: firstName");
                }
                firstName = value;
            }
        }

        public string LastName
        {
            get
            {
                return lastName;
            }
            set
            {
                if (!char.IsUpper(value[0]))
                {
                    throw new ArgumentException("Expected upper case letter! Argument: lastName");
                }
                if (value.Length < 3)
                {
                    throw new ArgumentException("Expected length at least 3 symbols! Argument: lastName ");
                }
                lastName = value;
            }
        }
    }

    public class Student : Human
    {
        private string facultyNumber;

        public Student(string firstName, string lastName, string facultyNumber) : base(firstName, lastName)
        {
            this.FacultyNumber = facultyNumber;
        }

        public string FacultyNumber
        {
            get
            {
                return facultyNumber;
            }
            set
            {
                if (value.Length < 5 || value.Length > 10)
                {
                    throw new ArgumentException("Invalid faculty number!");
                }
                foreach (var c in value)
                {
                    if (!char.IsDigit(c))
                    {
                        throw new ArgumentException("Invalid faculty number!");
                    }
                }
                facultyNumber = value;
            }
        }

        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.AppendLine($"First Name: {FirstName}");
            sb.AppendLine($"Last Name: {LastName}");
            sb.AppendLine($"Faculty Number: {FacultyNumber}");

            return sb.ToString(); // повертає просто строку

        }
    }

    public class Worker : Human
    {
        private double weekSalary;
        private double workHoursPerDay;

        public Worker(string firstName, string lastName, double weekSalary, double workHoursPerDay) : base(firstName, lastName)
        {
            this.WeekSalary = weekSalary;
            this.WorkHoursPerDay = workHoursPerDay;
        }

        public double WeekSalary
        {
            get
            {
                return weekSalary;
            }
            set
            {
                if (value <= 10)
                {
                    throw new ArgumentException("Expected value mismatch! Argument: weekSalary");
                }
                weekSalary = value;
            }
        }

        private double WorkHoursPerDay
        {
            get
            {
                return workHoursPerDay;
            }
            set
            {
                if (value < 1 || value > 12)
                {
                    throw new ArgumentException("Expected value mismatch! Argument: workHoursPerDay");
                }
                workHoursPerDay = value;
            }
        }

        public override string ToString()
        {
            double totalAmount = WorkHoursPerDay * 5;
            double result = WeekSalary / totalAmount;
            var sb = new StringBuilder();
            sb.AppendLine($"Fisrt Name: {FirstName}");
            sb.AppendLine($"Last Name: {LastName}");
            sb.AppendLine($"Week Salary: {WeekSalary}");
            sb.AppendLine($"Hours Per Week: {workHoursPerDay:f2}");
            sb.AppendLine($"Salary Per Hour: {result:f2}");

            return sb.ToString();
        }
    }

    public class Start
    {
        static void Main(string[] args)
        {
            try
            {
                var studentInput = Console.ReadLine().Split().ToArray();
                string firstName = studentInput[0];
                string lastName = studentInput[1];
                string faculutyNumber = studentInput[2];

                Student student = new Student(firstName, lastName, faculutyNumber);

                var workerInput = Console.ReadLine().Split().ToArray();
                string firstName1 = workerInput[0];
                string lastName1 = workerInput[1];
                double salary = double.Parse(workerInput[2]);
                double workinghours = double.Parse(workerInput[3]);

                Worker worker = new Worker(firstName1, lastName1, salary, workinghours);

                Console.WriteLine(student);
                Console.WriteLine(worker);
            }
            catch (Exception e) //використовувати, лише якщо вам справді потрібно перевірити викликаний виняток 
            {
                Console.WriteLine(e.Message);
            }
        }
    }
}