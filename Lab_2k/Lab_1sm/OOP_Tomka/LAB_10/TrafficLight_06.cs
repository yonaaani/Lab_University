using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TrafficLight_06
{
    public enum LightColors
    {
        Red, Green, Yellow
    }
    public class TrafficLight
    {
        public LightColors LightColor { get; set; }

        public TrafficLight(string lightColorString)
        {
            var lightColor = (LightColors)Enum.Parse(typeof(LightColors), lightColorString);
            this.LightColor = lightColor;
        }

        public void ChangeColor()
        {
            var intColor = (int)this.LightColor;
            intColor = (intColor + 1) % 3;
            this.LightColor = (LightColors)Enum.Parse(typeof(LightColors), intColor.ToString());
        }

        public override string ToString()
        {
            return $"{this.LightColor.ToString()}";
        }
    }

    public class StartProgram
    {
        static void Main(string[] args)
        {
            var initialColors = Console.ReadLine().Split().ToList();
            var trafficLights = initialColors.Select(t => new TrafficLight(t)).ToList();
            var amountOfChanges = int.Parse(Console.ReadLine());

            for (int i = 0; i < amountOfChanges; i++)
            {
                foreach (var light in trafficLights)
                {
                    light.ChangeColor();
                }

                Console.WriteLine(string.Join(" ", trafficLights));
            }
        }
    }
}
