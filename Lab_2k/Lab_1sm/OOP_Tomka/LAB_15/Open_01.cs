using System;
using System.Configuration;
using System.Data.SqlClient;

namespace Open_01
{
    internal class StartUp
    {
        static void Main(string[] args)
        {
            try
            {
                string connectionString = @"Data Source=DESKTOP-AOKJEDU\SQLEXPRESS;Initial Catalog=Laba15_OOP;Integrated Security=True";
                using (SqlConnection connection = new SqlConnection(connectionString))
                {
                    //1.2
                    Console.WriteLine("<-1.2->");
                    connection.Open();
                    Console.WriteLine("З'єднано!");

                    //1.3
                    Console.WriteLine("<-1.3->");
                    string sqlExpression = "SELECT * FROM [Points]";
                    SqlCommand command = new SqlCommand(sqlExpression, connection);
                    SqlDataReader reader = command.ExecuteReader();
                    if (reader.HasRows) // якщо є дані
                    {
                        // виводим назви стовпців
                        Console.WriteLine("{0}\t{1}\t{2}\t{3}\t{4}\t{5}", reader.GetName(0), reader.GetName(1), reader.GetName(2), reader.GetName(3), reader.GetName(4), reader.GetName(5));

                        while (reader.Read()) // строково зчитую всі дані
                        {
                            object id = reader.GetValue(0);
                            object name = reader.GetValue(1);
                            object group = reader.GetValue(2);
                            object ser = reader.GetValue(3);
                            object predmetmin = reader.GetValue(4);
                            object predmetmax = reader.GetValue(5);

                            Console.WriteLine("{0} \t{1} \t{2} \t{3} \t{4} \t{5}", id, name, group, ser, predmetmin, predmetmax);
                        }
                    }
                    reader.Close();


                    Console.WriteLine();
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    string sqlExpression1 = "SELECT [StudentName] FROM [Points]";
                    SqlCommand command1 = new SqlCommand(sqlExpression1, connection);
                    SqlDataReader reader1 = command1.ExecuteReader();
                    if(reader1.HasRows)
                    {
                        Console.WriteLine("{0}", reader1.GetName(0));

                        while (reader1.Read())
                        {
                            object name = reader1.GetValue(0);
                            Console.WriteLine("{0}", name);
                        }
                    }
                    reader1.Close();

                    Console.WriteLine();
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    string sqlExpression2 = "SELECT [AVGPoint] FROM [Points]";
                    SqlCommand command2 = new SqlCommand(sqlExpression2, connection);
                    SqlDataReader reader2 = command2.ExecuteReader();
                    if (reader2.HasRows)
                    {
                        Console.WriteLine("{0}", reader2.GetName(0));

                        while (reader2.Read())
                        {
                            object avg = reader2.GetValue(0);
                            Console.WriteLine("{0}", avg);
                        }
                    }
                    reader2.Close();

                    Console.WriteLine();
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    string sqlExpression3 = "SELECT [StudentName],[AVGPoint] FROM [Points] WHERE [AVGPoint]>50"; 
                    SqlCommand command3 = new SqlCommand(sqlExpression3, connection);
                    SqlDataReader reader3 = command3.ExecuteReader();
                    if (reader3.HasRows)
                    {
                        Console.WriteLine("{0}\t{1}", reader3.GetName(0), reader3.GetName(1));

                        while (reader3.Read())
                        {
                            object name = reader3.GetValue(0);
                            object avg = reader3.GetValue(1);
                            Console.WriteLine("{0}\t{1}", name, avg);
                        }
                    }
                    reader3.Close();


                    Console.WriteLine();
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    string sqlExpression33 = "SELECT [MINPoin] FROM [Points]";
                    SqlCommand command33 = new SqlCommand(sqlExpression33, connection);
                    SqlDataReader reader33 = command33.ExecuteReader();
                    if (reader33.HasRows)
                    {
                        Console.WriteLine("{0}", reader33.GetName(0));

                        while (reader33.Read())
                        {
                            object avg = reader33.GetValue(0);
                            Console.WriteLine("{0}", avg);
                        }
                    }
                    reader33.Close();


                    //1.4
                    Console.WriteLine("<-1.4->");
                    string sqlExpression4 = "SELECT COUNT(*) FROM [Points]";
                    SqlCommand command4 = new SqlCommand(sqlExpression4, connection);
                    object count = command4.ExecuteScalar();

                    Console.WriteLine();
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    command4.CommandText = "SELECT MIN([AVGPoint]) FROM [Points]";
                    object minPoint = command4.ExecuteScalar();
                    Console.WriteLine(" MinPoint: {0} ", minPoint);

                    Console.WriteLine();
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    command4.CommandText = "SELECT MAX([AVGPoint]) FROM [Points]";
                    object maxPoint = command4.ExecuteScalar();
                    Console.WriteLine(" MaxPoint: {0} ", maxPoint);

                    Console.WriteLine();
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    command4.CommandText = ("SELECT MIN([AVGPoint]) FROM [Points] WHERE [MINPoin]='Math'");
                    object minMath = command4.ExecuteScalar();
                    Console.WriteLine(" Minimal Point on Math: {0} ", minMath);

                    Console.WriteLine();
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    command4.CommandText = ("SELECT MAX([AVGPoint]) FROM [Points] WHERE [MINPoin]='Math'");
                    object maxMath = command4.ExecuteScalar();
                    Console.WriteLine(" Maximum Point on Math: {0} ", maxMath);

                    Console.WriteLine();
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    command4.CommandText = ("SELECT COUNT([GruopName]) FROM [Points]");  
                    object countGroup = command4.ExecuteScalar();
                    Console.WriteLine(" Count in all Groups: {0} ", countGroup);

                    Console.WriteLine();
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    string sqlExpression5 = "SELECT [GruopName], COUNT([StudentName]) AS CountOfStudents FROM [Points] GROUP BY [GruopName]";
                    SqlCommand command5 = new SqlCommand(sqlExpression5, connection);
                    SqlDataReader reader5 = command5.ExecuteReader();
                    if (reader5.HasRows)
                    {
                        Console.WriteLine("{0}\t{1}", reader5.GetName(0), reader5.GetName(1));

                        while (reader5.Read())
                        {
                            object name = reader5.GetValue(0);
                            object countt = reader5.GetValue(1);
                            Console.WriteLine("{0}\t{1}", name, countt);
                        }
                    }
                    reader5.Close();


                    Console.WriteLine();
                    connection.Close();
                    Console.WriteLine("Роз'єднано!");
                }
            }
            catch (SqlException ex)
            {
                Console.WriteLine(ex.Message);
            }

            Console.Read();
        }
    }
}
