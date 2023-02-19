import java.lang.*;

class lab2_1_Cosinus {
    public static void main(String[] args)
    {
        double x = 30.0;
        double y = 30.0;

        // Конвертувати в радіани
        x = Math.toRadians(x);
        y = Math.toRadians(y);

        // Синус + косинус
        x = Math.cos(x);
        y = Math.sin(y);

        System.out.println("cos 30° = " + x);
        System.out.println("sin 30° = " + y);

    }
}