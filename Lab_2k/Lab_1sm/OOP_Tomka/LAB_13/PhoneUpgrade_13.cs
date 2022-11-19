using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LAB_13
{
    internal class PhoneUpgrade_13
    {
        static void Main()
        {
            var phonebook = new Dictionary<string, string>();

            var input = Console.ReadLine().Split(' ').ToList();

            while (input[0] != "END")
            {
                // Здається так... вивід всього
                if(input[0] == "ListAll")
                {
                    foreach(var value in phonebook)
                    {
                        Console.WriteLine(value);
                    }
                }
                // Додати ім'я та номер телефону
                if (input[0] == "A")
                {
                    if (!phonebook.ContainsKey(input[1]))
                    {
                        phonebook.Add(input[1], input[2]);
                    }
                    else
                    {
                        phonebook[input[1]] = input[2];
                    }
                }
                // Вивести ім'я та номер телефону або, якщо такого імені немає...
                if (input[0] == "S")
                {
                    if (phonebook.ContainsKey(input[1]))
                    {
                        Console.WriteLine($"{input[1]} -> {phonebook[input[1]]}");
                    }
                    else
                    {
                        Console.WriteLine($"Contact {input[1]} does not exist.");
                    }
                }
                //Продовжується зчитування всіх команд на консолі, включаючи останній рядок.
                input = Console.ReadLine().Split(' ').ToList();
            }
        }
    }
}
