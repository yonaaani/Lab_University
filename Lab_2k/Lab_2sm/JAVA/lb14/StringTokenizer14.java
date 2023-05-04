import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.StringTokenizer;
import  java.io.File;

public class StringTokenizer14 {

    public static void main(String[] args) {

        try (BufferedReader br = new BufferedReader(new FileReader("src/input"))) {
            String line;
            while ((line = br.readLine()) != null) {
                System.out.println("Введений рядок: " + line);
                StringTokenizer st = new StringTokenizer(line);
                System.out.print("Рядок складається з: ");
                while (st.hasMoreTokens()) {
                    String token = st.nextToken();
                    try {
                        double num = Double.parseDouble(token);
                        System.out.printf("%s - це число = %.1f%n", token, num);
                    } catch (NumberFormatException e) {
                        System.out.print(token + " ");
                    }
                }
                System.out.println();
            }
        } catch (FileNotFoundException e) {
            System.out.println("Файл не знайдений");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
