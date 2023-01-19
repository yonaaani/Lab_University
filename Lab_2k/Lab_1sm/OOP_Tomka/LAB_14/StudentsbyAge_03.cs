﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LAB_14
{
    internal class StudentsbyAge_03
    {
        public class Startup
        {
            public static void Main()
            {
                var inputLine = Console.ReadLine();
                var studentsGroup = new List<string[]>();
                while (!inputLine.Equals("END"))
                {
                    var studentNames = inputLine.Trim().Split();
                    studentsGroup.Add(studentNames);
                    inputLine = Console.ReadLine();
                }

                var result = studentsGroup
                    .Where(x => int.Parse(x[x.Length - 1]) >= 18 && int.Parse(x[x.Length - 1]) <= 24);

                foreach (var student in result)
                {
                    Console.WriteLine($"{student[0]} {student[1]} {student[2]}");
                }
            }
        }
    }
}
