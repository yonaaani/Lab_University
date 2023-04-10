using JetBrains.Annotations;
using Microsoft.EntityFrameworkCore;
using StudentSystem.Data.Configurations;
using StudentSystem.Data.Models;
using System;
using System.Collections.Generic;
using System.Text;

namespace StudentSystem.Data
{
    public class StudentSystemContext : DbContext
    {

        public DbSet<Student> Students { get; set; }
        public DbSet<Course> Courses { get; set; }
        public DbSet<Resource> Resources { get; set; }
        public DbSet<Homework> HomeworkSubmissions { get; set; }
        public DbSet<StudentCourse> StudentCourses { get; set; }

        public StudentSystemContext()
        {
        }

        public StudentSystemContext(DbContextOptions options)
            : base(options)
        {
        }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            if (!optionsBuilder.IsConfigured)
            {
                optionsBuilder.UseSqlServer(Configure.ConnectionString);
            }
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.ApplyConfiguration(new StudentConfig());
            modelBuilder.ApplyConfiguration(new CourseConfig());
            modelBuilder.ApplyConfiguration(new ResourceConfig());
            modelBuilder.ApplyConfiguration(new HomeworkConfig());
            modelBuilder.ApplyConfiguration(new StudentCourseConfig());

            //seeding
            modelBuilder.Entity<Student>().HasData(
                new Student
                {
                    StudentId = 4,
                    Name = "Evlogi",
                    PhoneNumber = "38827834",
                    RegisteredOn = DateTime.Now,
                    Birthday = new DateTime(1985, 02, 12)
                }
                );

            modelBuilder.Entity<Student>().HasData(
                new Student
                {
                    StudentId = 1,
                    Name = "Ivaylo",
                    PhoneNumber = "38827834",
                    RegisteredOn = DateTime.Now,
                    Birthday = new DateTime(1989, 05, 01)
                }
                );

            modelBuilder.Entity<Student>().HasData(
                new Student
                {
                    StudentId = 2,
                    Name = "Doncho",
                    Birthday = new DateTime(1988, 11, 22),
                    PhoneNumber = "388000034",
                    RegisteredOn = DateTime.Now
                }
                );

            modelBuilder.Entity<Student>().HasData(
                new Student
                {
                    StudentId = 3,
                    Name = "Nikolay",
                    Birthday = new DateTime(1990, 01, 20),
                    PhoneNumber = "38834434",
                    RegisteredOn = DateTime.Now
                }
                );

            modelBuilder.Entity<Course>().HasData(
                new Course
                {
                    CourseId = 1,
                    Name = "sql server",
                    Description = "veey interesting",
                    StartDate = DateTime.Today,
                    EndDate = DateTime.Today,
                    Price = 567
                }
                );

            modelBuilder.Entity<Course>().HasData(
                new Course
                {
                    CourseId = 2,
                    Name = "c# code",
                    Description = "very interesting",
                    StartDate = DateTime.Today,
                    EndDate = DateTime.Today,
                    Price = 999
                }
                );

            modelBuilder.Entity<Homework>().HasData(
                new Homework
                {
                    HomeworkId = 1,
                    Content = "do jsjdsj",
                    ContentType = ContentType.zip,
                    SubmissionTime = new DateTime(2023, 11, 22)
                }
                );

            modelBuilder.Entity<Resource>().HasData(
                new Resource
                {
                    ResourceId = 1,
                    Name = "For sql",
                    Url = "/sdjsdjkdjksdsd",
                    ResourceType = ResourceType.other
                }
                ); 
        }

    }
}