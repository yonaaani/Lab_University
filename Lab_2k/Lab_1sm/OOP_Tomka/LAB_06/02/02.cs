using System;
using System.Collections.Generic;
using System.Text;

namespace BookShop_02
{
    public class Book
    {
        private string title;
        private string author;
        private decimal price;

        public Book(string author, string title, decimal price)
        {
            this.Title = title;
            this.Author = author;
            this.Price = price;
        }

        public string Title
        {
            get
            {
                return title;
            }
            set
            {
                if (string.IsNullOrEmpty(value) || value.Length < 3)
                {
                    throw new ArgumentException("Title not valid");
                }
                title = value;
            }
        }

        private string Author
        {
            get
            {
                return author;
            }
            set
            {
                var name = value.Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
                if (name.Length > 1 && char.IsDigit(name[1][0]))
                {
                    throw new ArgumentException("Author not valid");
                }
                author = value;
            }
        }

        public virtual decimal Price
        {
            get
            {
                return price;
            }
            set
            {
                if (value <= 3)
                {
                    throw new ArgumentException("Price not valid");
                }
                price = value;
            }
        }

        public override string ToString()
        {
            var resultBuilder = new StringBuilder();
            resultBuilder.AppendLine($"Type: {this.GetType().Name}")
                .AppendLine($"Title: {this.Title}")
                .AppendLine($"Author: {this.Author}")
                .AppendLine($"Price: {this.Price:f2}");

            string result = resultBuilder.ToString().TrimEnd();
            return result;
        }
    }

    public class GoldenEditionBook : Book
    {
        public GoldenEditionBook(string author, string title, decimal price) : base(author, title, price)
        { }

        public override decimal Price
        {
            get
            {
                return base.Price * 1.3M;
            }
        }

    }
    public class Start
    {
        public static void Main()
        {
            try
            {
                string author = Console.ReadLine();
                string title = Console.ReadLine();
                decimal price = decimal.Parse(Console.ReadLine());

                Book book = new Book(author, title, price);
                GoldenEditionBook goldenEditionBook = new GoldenEditionBook(author, title, price);

                Console.WriteLine(book);
                Console.WriteLine(goldenEditionBook);
            }
            catch (ArgumentException ae)
            {
                Console.WriteLine(ae.Message);
            }
        }
    }

}