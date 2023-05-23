using P01_BillsPaymentSystem.Core.IO.Contracts;
using System;

namespace P01_BillsPaymentSystem.Core.IO
{
    public class ConsoleWriter : IWriter
    {
        public void WriteLine(string text)
        {
            Console.WriteLine(text);
        }
    }
}