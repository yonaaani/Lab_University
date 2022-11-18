using System; //00
using System.Globalization; //01 Содержит классы, определяющие сведения, относящиеся к культуре, такие как язык, название страны, используемые календари, шаблоны форматирования дат, денежных сумм и чисел, а также порядок сортировки строк
using System.IO; // 02 Содержит типы, позволяющие осуществлять чтение и запись в файлы и потоки данных, а также типы для базовой поддержки файлов и папок.
using System.Numerics; // 03 Содержит числовые типы, дополняющие числовые типы — примитивы, такие как Byte, Double и Int32
using System.Text; // 04 Содержит классы, которые представляют кодировки ASCII и Юникода
using System.Threading; //05 Thread - Создает и контролирует поток, задает приоритет и возвращает статус.
using System.Collections.Generic;
using System.Reflection;

namespace HarvestingFields_01
{
    class HarvestingFields
    {
        private int testInt;
        public double testDouble;
        protected string testString;
        private long testLong;
        protected double aDouble;
        public string aString;
        private Calendar aCalendar; //01
        public StringBuilder aBuilder; //04
        private char testChar;
        public short testShort;
        protected byte testByte;
        public byte aByte;
        protected StringBuilder aBuffer; //04
        private BigInteger testBigInt; //03
        protected BigInteger testBigNumber; //03
        protected float testFloat;
        public float aFloat;
        private Thread aThread; //05
        public Thread testThread; //05
        private object aPredicate;
        protected object testPredicate;
        public object anObject;
        private object hiddenObject;
        protected object fatherMotherObject;
        private string anotherString;
        protected string moarString;
        public int anotherIntBitesTheDust; 
        private Exception internalException; //00
        protected Exception inheritableException; //00
        public Exception justException; //00
        public Stream aStream; //02
        protected Stream moarStreamz; //02
        private Stream secretStream; //02
    }

    public class ProgramStart
    {
        public static void Main()
        {
            var input = "";
            var type = typeof(HarvestingFields);
            var fields = type.GetFields(BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static | BindingFlags.Instance);
            while ((input = Console.ReadLine()) != "HARVEST")
            {
                List<FieldInfo> fieldsFromQuery = null;
                switch (input)
                {
                    case "private":
                        fieldsFromQuery = fields.Where(f => f.IsPrivate).ToList();
                        break;

                    case "protected":
                        fieldsFromQuery = fields.Where(f => f.IsFamily).ToList();
                        break;

                    case "public":
                        fieldsFromQuery = fields.Where(f => f.IsPublic).ToList();
                        break;

                    case "all":
                        fieldsFromQuery = fields.ToList();
                        break;
                }

                string[] result = fieldsFromQuery.Select(f => $"{f.Attributes.ToString().ToLower()} {f.FieldType.Name} {f.Name}").ToArray();

                Console.WriteLine(string.Join(Environment.NewLine, result).Replace("family", "protected"));
            }
        }
    }
}