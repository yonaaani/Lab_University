using System;
using System.Text.RegularExpressions;


namespace LAB_12
{
    internal class ReplaceATag_04
    {
        static void Main(string[] args)
        {
            string text = Console.ReadLine();
            while (text != "end")
            {
                string pattern = @"<a.*?href.*?=(.*)>(.*?)<\/a>";
                // для взяття двох груп
                // перша група використовується для доменного імені
                // наприклад: ttps://stackoverflow.com"

                // а другий, якщо ви хочете ввести текст
                // (або не ввести текст)
                // наприклад : This is some text

                string replace = @"[URL href=$1]$2[/URL]";
                // використала $ char і число (як заповнювачі)
                // наприклад: $1 означає взяти все, що знайдеться з групи 1
                //         і: $2 означає взяти все, що ви знайдеться з групи 2

                string replaced = Regex.Replace(text, pattern, replace);

                //  У певному вхідному рядку (тексті) замінює всі рядки
                //  які збігаються з указаним регулярним виразом (шаблоном/маскою).
                //  вказаний рядок заміни (replace)

                Console.WriteLine(replaced);

                text = Console.ReadLine();
            }


        }
    }
}
