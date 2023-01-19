using System;
using System.Configuration;
using System.Data.SqlClient;
using Dapper;
using System.Text;
using System.Linq;
using System.Collections.Generic;
using System.Threading.Tasks;
using System.Data;



namespace PromotionalProducts_01
{
    public class Buyers
    {
        public int BuyerID { get; set; }
        public string BuyerName { get; set; }
        public DateTime dateTime { get; set; }
        public string BuyerEmail { get; set; }
        public string BuyerCountry { get; set; }
        public string BuyerCity { get; set; }
        public int IDRozdil { get; set; }

        public override string ToString()
        {
            return $"{BuyerID} {BuyerName} {dateTime} {BuyerEmail} {BuyerCountry} {BuyerCity}";
        }
    }

    public class Rozdili
    {
        public int RozdilaID { get; set; }
        public int BuyerID { get; set; }
        public string RozdilaName { get; set; }

        public override string ToString()
        {
            return $"{RozdilaID} {BuyerID} {RozdilaName}";
        }
    }

    public class SellerProducts
    {
        public int SellerProductsID { get; set; }
        public int RozdilaID { get; set; }
        public int BuyerID { get; set; }
        public string SellerProductsName { get; set; }
        public DateTime SellerProductsDateStart { get; set; }
        public DateTime SellerProductsDateEnd { get; set; }
    }
    internal class StartUp
    {
        // private static readonly string connectionString = @"Data Source=DESKTOP-AOKJEDU\SQLEXPRESS;Initial Catalog=Laba16_OOP;Integrated Security=True";

        static void Main(string[] args)
        {
            try
            {
                string connectionString = @"Data Source=DESKTOP-AOKJEDU\SQLEXPRESS;Initial Catalog=Laba16_OOP;Integrated Security=True";
                using (var connection = new SqlConnection(connectionString))
                {
                    //1.2
                    Console.WriteLine("<-1.2->");
                    connection.Open();
                    Console.WriteLine("З'єднано!");

                    //1.3
                    Console.WriteLine("<-1.3->");
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    var sql1 = connection.Query<Buyers>("SELECT * FROM [Buyer]").ToList();
                    sql1.ForEach(sql => Console.WriteLine(sql));

                    Console.WriteLine();
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    var sql2 = connection.Query<Buyers>("SELECT [EmailBuyer] FROM [Buyer]").ToList();
                    sql2.ForEach(sql => Console.WriteLine(sql));

                    Console.WriteLine();
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    var sql3 = connection.Query<Rozdili>("SELECT [NameRozdila] FROM [ListRozdiliv]").ToList();
                    sql3.ForEach(sql => Console.WriteLine(sql));

                    Console.WriteLine();
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    var sql4 = connection.Query<SellerProducts>("SELECT [NameSellerProduct] FROM [SellerProduct]").ToList();
                    sql4.ForEach(sql => Console.WriteLine(sql));

                    Console.WriteLine();
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    var sql5 = connection.Query<Buyers>("SELECT [CityBuyer] FROM [Buyer]").ToList();
                    sql5.ForEach(sql => Console.WriteLine(sql));

                    Console.WriteLine();
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    var sql6 = connection.Query<Buyers>("SELECT [CountryBuyer] FROM [Buyer]").ToList();
                    sql6.ForEach(sql => Console.WriteLine(sql));

                    //1.4
                    Console.WriteLine("<-1.4->");
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    var sql11 = connection.QueryFirst<Buyers>("SELECT [NameBuyer] FROM [Buyer] WHERE [CityBuyer]=@city", new { city = "Lviv" });
                    Console.WriteLine(sql11);

                    Console.WriteLine();
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    var sql22 = connection.QueryFirst<Buyers>("SELECT [NameBuyer] FROM [Buyer] WHERE [CountryBuyer]=@country", new { country = "Austria" });
                    Console.WriteLine(sql22);

                    Console.WriteLine();
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    var sql33 = connection.QueryFirst<SellerProducts>("SELECT [NameSellerProduct] FROM [SellerProduct] WHERE [IDBuyer]=@id", new { id = 1 });
                    Console.WriteLine(sql33);

                    Console.WriteLine("<-2.1->");
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    IEnumerable<Buyers> proc1 = null;
                    proc1 = connection.Query<Buyers>("[dbo].[Proc_1]", commandType: CommandType.StoredProcedure);

                    Console.WriteLine();
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    IEnumerable<Buyers> proc2 = null;
                    proc2 = connection.Query<Buyers>("[dbo].[Proc_2]", commandType: CommandType.StoredProcedure);

                    Console.WriteLine();
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    IEnumerable<Buyers> proc3 = null;
                    proc3 = connection.Query<Buyers>("[dbo].[Proc_3]", commandType: CommandType.StoredProcedure);

                    Console.WriteLine();
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    IEnumerable<Buyers> proc4 = null;
                    proc4 = connection.Query<Buyers>("[dbo].[Proc_4]", commandType: CommandType.StoredProcedure);

                    Console.WriteLine();
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    IEnumerable<Buyers> proc5 = null;
                    proc5 = connection.Query<Buyers>("[dbo].[Proc_5]", commandType: CommandType.StoredProcedure);

                    Console.WriteLine();
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    IEnumerable<Buyers> proc7 = null;
                    proc7 = connection.Query<Buyers>("[dbo].[Proc_7]", commandType: CommandType.StoredProcedure);

                    Console.WriteLine();
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    IEnumerable<Buyers> proc8 = null;
                    proc8 = connection.Query<Buyers>("[dbo].[Proc_8]", commandType: CommandType.StoredProcedure);

                    Console.WriteLine();
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    IEnumerable<Buyers> proc9 = null;
                    proc9 = connection.Query<Buyers>("[dbo].[Proc_9]", commandType: CommandType.StoredProcedure);

                    Console.WriteLine();
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    IEnumerable<Buyers> proc10 = null;
                    proc10 = connection.Query<Buyers>("[dbo].[Proc_10]", commandType: CommandType.StoredProcedure);

                    Console.WriteLine();
                    Console.WriteLine("------------------------------------------------------------------------------------------");
                    IEnumerable<Buyers> proc11 = null;
                    proc11 = connection.Query<Buyers>("[dbo].[Proc_11]", commandType: CommandType.StoredProcedure);

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


       
        //public interface IBuyers
        //{
        //    List<Buyers> GetBuyers();
        //}

        // public class BuyersRepository : IBuyers
        //{
        //    string connectionString = null;
        //   public BuyersRepository(string conn)
        //   {
        //      connectionString = conn;
        //  }
        //  public List<Buyers> GetBuyers()
        //  {
        //     using (IDbConnection db = new SqlConnection(connectionString))
        //    {
        //        return db.Query<Buyers>("SELECT * FROM [Покупець]").ToList();
        //    }
        // }
        // }

        //public IEnumerable<Buyers> GetBuyers()
        //{
        //    var buyersall = typeof(Buyers).GetProperties().Select(prop => prop.Name);
        //
        //   var firstQuery = new StringBuilder("SELECT ")
        //        .AppendJoin(", ", buyersall)
        //         .Append($" FROM [dbo].[{nameof(Покупець)}]")
        //         .ToString();
        //}
    }
}