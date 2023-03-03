import java.util.Scanner;
public class Lab4 {
    private double[] vector = null;
    public Lab4(double[] vector){
        this.vector = vector;
    }
    // Множення вектора на число
    public double mult(int n){
        double s = 0;
        for ( int i = 0; i < vector.length; i++ ){
            s += vector[i] * n;
        }
        return s;
    }
    public static double mult(Lab4 a, int b){
        return a.mult(b);
    }
    public static void main(String[] args){
        double[] a = {1, 2, 3, 4};
        double[] b = {1, 1, 1, 1};
        double[] c = {2, 2, 2, 2};
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter number:");
        int n = scan.nextInt();
        Lab4 v1 = new Lab4(a);
        Lab4 v2 = new Lab4(b);
        Lab4 v3 = new Lab4(c);
        System.out.println("v1*n=" + v1.mult(n));
        System.out.println("v2*n=" + Lab4.mult(v2,n));
        System.out.println("v3*n=" + v3.mult(n));
    }
}
