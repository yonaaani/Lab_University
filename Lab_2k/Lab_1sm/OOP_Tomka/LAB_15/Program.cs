using System;
using System.Configuration;
using System.Data.SqlClient;

namespace _2
{
    internal class StartUp
    {
        static void Main(string[] args)
        {
            string connectionString = @"Data Source=DESKTOP-AOKJEDU\SQLEXPRESS;Initial Catalog=Laba15_OOP;Integrated Security=True";

            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                connection.Open();
                SqlCommand command = new SqlCommand();
                command.CommandText = "SELECT * FROM [Оцінки студентів]";
                command.Connection = connection;
            }
        }
    }
}
