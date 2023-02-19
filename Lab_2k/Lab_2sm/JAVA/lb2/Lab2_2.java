import java.io.IOException;
import java.lang.*;
import java.io.*;
import java.util.Scanner; //як сканер, зчитує дані з джерела


public class Lab2_2 {
    public static void main(String[] args) throws IOException {
      System.out.println("Please, input angel:");
      // створюємо нове посилання a на класс BufferedReader
        BufferedReader a = new BufferedReader(new InputStreamReader(System.in));
      // привласнюю змінній angle значення a
      String angle = a.readLine();
      // перетворюю строковий тип в double
      double x = Double.parseDouble(angle);
      // перетворюю в радіани
      x = Math.toRadians(x);
      double cos = Math.cos(x);
      double sin = Math.sin(x);

      System.out.println("cos = " + cos);
      System.out.println("sin = " + sin);

    }
}
