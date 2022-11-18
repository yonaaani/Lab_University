using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace EventImplementation_01
{
    public class NameChangeEventArgs : EventArgs
    {
        public NameChangeEventArgs(string name)
        {
            this.Name = name;
        }
        public string Name { get; private set; }
    }

    public class Handler
    {
        public void OnDispatcherNameChange(object sender, NameChangeEventArgs args)
        {
            Console.WriteLine($"Dispatcher's name changed to {args.Name}.");
        }
    }

    public delegate void NameChangeEventHandler(Object sender, NameChangeEventArgs parametr);

    public class Dispather
    {
        private string name;

        public event NameChangeEventHandler NameChange;

        public string Name
        {
            get { return this.name; }
            set 
            { 
                this.name = value;
                this.OnNameChange(new NameChangeEventArgs(value));
            }
        }

        public void OnNameChange(NameChangeEventArgs parametr)
        {
            if(this.NameChange != null)
            {
                this.NameChange(this, parametr);
            }
        }

    }
    public class StartProgram
    {
        public static void Main()
        {
            Dispather dispather = new Dispather();
            Handler handler = new Handler();

            dispather.NameChange += handler.OnDispatcherNameChange;

            string input = Console.ReadLine();

            while (input != null)
            {
                dispather.Name = input;
                input = Console.ReadLine();
            }
        }
    }
}