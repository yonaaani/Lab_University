using P01_BillsPaymentSystem.Core.IO.Contracts;
using System;

namespace P01_BillsPaymentSystem.Core.IO
{
    public class ConsoleReader : IReader
    {
        public string ReadLine()
        {
            return Console.ReadLine();
        }
    }
}