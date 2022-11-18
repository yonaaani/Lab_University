using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WorkForce_04
{
    // classes employee
    class StandartEmployee : Employee
    {
        private const int WorkHoursPerWeek = 40;

        public StandartEmployee(string name) : base(name,WorkHoursPerWeek) { }
    }

    class PartTimeEmployee : Employee
    {
        private const int WorkHoursPerWeek = 20;

        public PartTimeEmployee(string name) : base(name, WorkHoursPerWeek) { }
    }

    public abstract class Employee
    {
        public Employee(string name, int workHoursPerWeek)
        {
            this.Name = name;
            this.WorkHoursPerWeek = workHoursPerWeek;
        }
        public string Name { get; private set; }
        public int WorkHoursPerWeek { get; private set; }
    }

    public delegate void JobFinishedHandler(Job job);

    public class Job
    {
        private string name;
        private int hoursOfWorkRequired;
        private Employee employee;

        public Job(string name, int hoursOfWorkRequired, Employee employee)
        {
            this.name = name;
            this.hoursOfWorkRequired = hoursOfWorkRequired;
            this.employee = employee;
        }

        public event JobFinishedHandler JobFinished;

        public void Update()
        {
            this.hoursOfWorkRequired -= this.employee.WorkHoursPerWeek;

            if(this.hoursOfWorkRequired <= 0)
            {
                Console.WriteLine($"Job {this.name} done!");
                this.JobFinished.Invoke(this);
            }
        }

        public override string ToString()
        {
            return $"Job: {this.name} Hours Remaining: {this.hoursOfWorkRequired}";
        }
    }
}
