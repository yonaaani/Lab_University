using P01_BillsPaymentSystem.Data.Models;
using P01_BillsPaymentSystem.Data.Models.Enums;

namespace P01_BillsPaymentSystem.Initial
{
    public class PaymentMethodInitializer
    {
        public static PaymentMethod[] GetPaymentMethods()
        {
            PaymentMethod[] paymentMethods = new PaymentMethod[]
            {
                new PaymentMethod(PaymentType.BankAccount, 1, 7),
                new PaymentMethod(PaymentType.BankAccount, 2, 6),
                new PaymentMethod(PaymentType.BankAccount, 3, 5),
                new PaymentMethod(PaymentType.BankAccount, 4, 4),
                new PaymentMethod(PaymentType.BankAccount, 5, 3),
                new PaymentMethod(PaymentType.BankAccount, 6, 2),
                new PaymentMethod(PaymentType.BankAccount, 7, 1)
            };

            return paymentMethods;
        }
    }
}