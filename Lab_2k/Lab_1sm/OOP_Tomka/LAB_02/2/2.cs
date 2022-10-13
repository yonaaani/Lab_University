using System;

public class _02RotateRight
{
    public static void Main()
    {
        int[] arr = new int[] { 1, 2, 3, 4, 5 };
        int n = 1;

        Console.WriteLine("Original array: ");
        for (int i = 0; i < arr.Length; i++)
        {
            Console.Write(arr[i] + " ");
        }

        for (int i = 0; i < n; i++)
        {
            int j, last;
            last = arr[arr.Length - 1];

            for (j = arr.Length - 1; j > 0; j--)
            {
                arr[j] = arr[j - 1];
            }
            arr[0] = last;
        }

        Console.WriteLine();


        Console.WriteLine("Array after rotation 1: ");
        for (int i = 0; i < arr.Length; i++)
        {
            Console.Write(arr[i] + " ");
        }

        //.....................

        for (int i = 0; i < n + 1; i++)
        {
            int j, last;
            last = arr[arr.Length - 1];

            for (j = arr.Length - 1; j > 0; j--)
            {
                arr[j] = arr[j - 1];
            }
            arr[0] = last;
        }
        Console.WriteLine();

        Console.WriteLine("Array after rotation 2: ");
        for (int i = 0; i < arr.Length; i++)
        {
            Console.Write(arr[i] + " ");
        }

        //.....................

        for (int i = 0; i < n + 2; i++)
        {
            int j, last;
            last = arr[arr.Length - 1];

            for (j = arr.Length - 1; j > 0; j--)
            {
                arr[j] = arr[j - 1];
            }
            arr[0] = last;
        }
        Console.WriteLine();

        Console.WriteLine("Array after rotation 3: ");
        for (int i = 0; i < arr.Length; i++)
        {
            Console.Write(arr[i] + " ");
        }

        Console.WriteLine();
        int[] sumResult = new int[arr.Length];

    }
}
