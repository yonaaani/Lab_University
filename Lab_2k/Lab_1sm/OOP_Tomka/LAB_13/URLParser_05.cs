using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LAB_13
{
    internal class URLParser_05
    {
        static void Main()
        {
            string input = "http://server.example.org";
            string protocol = input.Substring(0, input.IndexOf(":"));
            string server = input.Substring(input.IndexOf("//") + 2, input.IndexOf("."));
            string domain = input.Substring(input.IndexOf(".") + 1);

            Console.WriteLine($"protocol: {protocol}, server: {server}, domain: {domain}");
        }
    }
}
