using StudentSystem.Data.Models;
using StudentSystem.Data;
using System;
using System.Data.Entity.Migrations;
using System.Data.Entity;
using System.Linq;
using System.Data;


namespace StudentSystem.Data.Migrations
{
     internal sealed class Configuration : DbMigrationsConfiguration<StudentSystemContext>
    {
        public Configuration()
        {
            this.AutomaticMigrationsEnabled = true;
            this.AutomaticMigrationDataLossAllowed = false;
            ContextKey = "StudentSystem.Data.StudentSystemContext";
        }

        protected override void Seed(StudentSystemContext context)
        {
            this.SeedCourses(context);
            this.SeedStudents(context);
        }

        private void SeedStudents(StudentSystemContext context)
        {
            if (context.Students.Any())
            {
                return;
            }

            context.Students.Add(new Student
            {
                Name = "Evlogi",
                Birthday = new DateTime(1985, 02, 12),
                RegisteredOn = DateTime.Now
            });

            context.Students.Add(new Student
            {
                Name = "Ivaylo",
                Birthday = new DateTime(1989, 05, 01),
                RegisteredOn = DateTime.Now
            });

            context.Students.Add(new Student
            {
                Name = "Doncho",
                Birthday = new DateTime(1988, 11, 22),
                RegisteredOn = DateTime.Now
            });

            context.Students.Add(new Student
            {
                Name = "Nikolay",
                Birthday = new DateTime(1990, 01, 20),
                RegisteredOn = DateTime.Now
            });
        }

        private void SeedCourses(StudentSystemContext context)
        {
            if (context.Courses.Any())
            {
                return;
            }

            context.Courses.Add(new Course
            {
                Name = "Seeded course",
                Description = "Initial course for testing"
            });
        }

        private void SeedHomeworks(StudentSystemContext context)
        {
            if (context.HomeworkSubmissions.Any())
            {
                return;
            }

            context.HomeworkSubmissions.Add(new Homework
            {
                Content = "Entity-Framework.rar",
                SubmissionTime = DateTime.Now
            });

            context.HomeworkSubmissions.Add(new Homework
            {
                Content = "Entity-Framework-Code-First.rar",
                SubmissionTime = DateTime.Now
            });
        }
    }
}