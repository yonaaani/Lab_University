using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Reflection;

namespace BlackBoxInteger_02
{
    public class BlackBoxInteger
    {
        private static int DefaultValue = 0;
        private int innerValue;

        private BlackBoxInteger(int innerValue)
        {
            this.innerValue = innerValue;
        }

        private BlackBoxInteger()
        {
            this.innerValue = DefaultValue;
        }

        //Methods:
        private void Add(int addend)
        {
            this.innerValue += addend;
        }

        private void Subtract(int subtrahend)
        {
            this.innerValue -= subtrahend;
        }

        private void Multiply(int multiplier)
        {
            this.innerValue *= multiplier;
        }

        private void Divide(int divider)
        {
            this.innerValue /= divider;
        }

        private void LeftShift(int shifter)
        {
            this.innerValue <<= shifter;
        }

        private void RightShift(int shifter)
        {
            this.innerValue >>= shifter;
        }
    }

    public class StartProgram
    {
        static void Main()
        {
            var input = "";
            var type = typeof(BlackBoxInteger);
            var blackboxObj = Activator.CreateInstance(type, true);
            var blackbox = (BlackBoxInteger)blackboxObj;

            while ((input = Console.ReadLine()) != "END")
            {
                var cmdArgs = input.Split('_');
                var operation = cmdArgs[0];
                var param = int.Parse(cmdArgs[1]);

                switch (operation)
                {
                    case "Add":
                        var addMethod = type.GetMethod("Add", BindingFlags.NonPublic | BindingFlags.Instance | BindingFlags.Static | BindingFlags.Public);
                        addMethod.Invoke(blackbox, new object[] { param });
                        break;

                    case "Subtract":
                        var subtractMethod = type.GetMethod("Subtract", BindingFlags.NonPublic | BindingFlags.Instance | BindingFlags.Static | BindingFlags.Public);
                        subtractMethod.Invoke(blackbox, new object[] { param });
                        break;

                    case "Multiply":
                        var multyplyMethod = type.GetMethod("Multiply", BindingFlags.NonPublic | BindingFlags.Instance | BindingFlags.Static | BindingFlags.Public);
                        multyplyMethod.Invoke(blackbox, new object[] { param });
                        break;

                    case "Divide":
                        var divideMethod = type.GetMethod("Divide", BindingFlags.NonPublic | BindingFlags.Instance | BindingFlags.Static | BindingFlags.Public);
                        divideMethod.Invoke(blackbox, new object[] { param });
                        break;

                    case "LeftShift":
                        var leftShiftMethod = type.GetMethod("LeftShift", BindingFlags.NonPublic | BindingFlags.Instance | BindingFlags.Static | BindingFlags.Public);
                        leftShiftMethod.Invoke(blackbox, new object[] { param });
                        break;

                    case "RightShift":
                        var righttShiftMethod = type.GetMethod("RightShift", BindingFlags.NonPublic | BindingFlags.Instance | BindingFlags.Static | BindingFlags.Public);
                        righttShiftMethod.Invoke(blackbox, new object[] { param });
                        break;

                    default:
                        break;
                }

                Console.WriteLine(type.GetField("innerValue", BindingFlags.NonPublic | BindingFlags.Instance | BindingFlags.Public | BindingFlags.Static).GetValue(blackbox));
            }
        }
    }
}
