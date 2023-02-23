import java.util.Scanner;
public class Lab3_2_Trukytnuk {
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter First int:");
        int first = scan.nextInt();
        System.out.print("Enter Second int:");
        int second = scan.nextInt();

        double rezult = calculate(first, second);
        System.out.println("result kyt c: " + rezult + "°");
    }

    public static double calculate(int x, int y) {
        double hyp = Math.hypot(x,y); //пошук гіпотенузи

        double rad1 = x/hyp;
        double rad2 = y/hyp;

        double kyt1 = Math.toDegrees(rad1);
        System.out.println("kyt a: " + kyt1 + "°");
        double kyt2 = Math.toDegrees(rad2);
        System.out.println("kyt b: " + kyt2 + "°");
        double result = 180 - kyt1 - kyt2;

        return result;
    }
}
