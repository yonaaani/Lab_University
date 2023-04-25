import java.util.*;
import java.io.*;

public class InputTest {
    public static void main(String args[]) {
        String searchString = "";
        ArrayList<String> list = new ArrayList<>();
        BufferedReader fin = null;
        try {
            if (args.length < 1) {
                System.out.println("Нужен параметр вызова: рядок для поиска");
                searchString = new Scanner(System.in).nextLine();
            } else {
                searchString = args[0];
            }
            System.out.println("Введи строки (для завершения ввода введите пустую строку):");
            Scanner scanner = new Scanner(System.in);
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                if (line.isEmpty()) break;
                System.out.println("==Введена строка: " + line);
                list.add(line);
            }
            Collections.sort(list);
            System.out.println("Отсортированный список строк:");
            for (String str : list) {
                System.out.println(str);
            }
            System.out.println("Результат поиска для строки \"" + searchString + "\":");
            for (String str : list) {
                if (str.contains(searchString)) {
                    System.out.println(str);
                }
            }
        } catch (Exception e) {
            System.out.println("Ошибка: " + e);
        } finally {
            if (fin != null) {
                try {
                    fin.close(); // !!! Закрыть файл
                } catch (IOException ex) {
                    System.out.println("Ошибка закрытия файла: " + ex);
                }
            }
        }
    }
}
