using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DependencyInversion_03
{
    //Models
   public class Add : IStrategy
    {
        public int Calculate(int first, int second)
        {
            return first + second;
        }
    }

    public class Minus : IStrategy
    {
        public int Calculate(int first, int second)
        {
            return first - second;
        }
    }

    public class Dilite : IStrategy
    {
        public int Calculate(int first,int second)
        {
            return first / second;
        }
    }

    public class Mnozhenia : IStrategy
    {
        public int Calculate(int first, int second)
        {
            return first * second;
        }
    }
    // Contracts
    public interface IStrategy
    {
        int Calculate(int first, int second);
    }

    public class PrimitiveCalculator
    {
        private IStrategy strategy;

        public PrimitiveCalculator()
        {
            this.strategy = new Add();
        }

        public void ChangeStrategy(char @operator)
        {
            IStrategy currentStrategy = null;

            switch (@operator)
            {
                case '+':
                    currentStrategy = new Add();
                    break;

                case '-':
                    currentStrategy = new Minus();
                    break;

                case '*':
                    currentStrategy = new Mnozhenia();
                    break;

                case '/':
                    currentStrategy = new Dilite();
                    break;
            }

            this.strategy = currentStrategy;
        }

        public int PerformCalculation(int firstOperand, int secondOperand)
        {
            return strategy.Calculate(firstOperand, secondOperand);
        }

        // start
        public class StartUp
        {
            public static void Main()
            {
                PrimitiveCalculator calculator = new PrimitiveCalculator();

                while (true)
                {
                    var input = Console.ReadLine().Split();

                    switch (input[0])
                    {
                        case "mode":
                            char symbol = input[1][0];
                            calculator.ChangeStrategy(symbol);
                            break;

                        case "End":
                            return;

                        default:
                            int firstOperand = int.Parse(input[0]);
                            int secondOperand = int.Parse(input[1]);
                            Console.WriteLine(calculator
                                .PerformCalculation(firstOperand, secondOperand));
                            break;
                    }
                }
            }
        }
    }
}
