using System;

class _01GFG
{
    static void printLCSubStr(String X, String Y, int m, int n)
    {
        int[,] LCSuff = new int[m + 1, n + 1];
        int len = 0;
        int row = 0, col = 0;

        for (int i = 0; i <= m; i++)
        {
            for (int j = 0; j <= n; j++)
            {
                if (i == 0 || j == 0)
                    LCSuff[i, j] = 0;

                else if (X[i - 1] == Y[j - 1])
                {
                    LCSuff[i, j] = LCSuff[i - 1, j - 1] + 1;
                    if (len < LCSuff[i, j])
                    {
                        len = LCSuff[i, j];
                        row = i;
                        col = j;
                    }
                }
                else
                    LCSuff[i, j] = 0;
            }
        }

        if (len == 0)
        {
            Console.Write("No Common Substring");
            return;
        }

        String resultStr = "";

        while (LCSuff[row, col] != 0)
        {
            resultStr = X[row - 1] + resultStr; 
            --len;

            row--;
            col--;
        }

        Console.WriteLine(resultStr);
    }


    public static void Main()
    {
        String X = "OldSite:GeeksforGeeks.org";
        String Y = "NewSite:GeeksQuiz.com";

        int m = X.Length;
        int n = Y.Length;

        printLCSubStr(X, Y, m, n);
    }
}
