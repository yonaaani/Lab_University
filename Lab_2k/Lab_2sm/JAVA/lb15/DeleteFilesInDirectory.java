import java.io.File;
import java.util.Scanner;

public class DeleteFilesInDirectory {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the directory path: ");
        String directoryPath = scanner.nextLine();

        File directory = new File(directoryPath);

        if (!directory.isDirectory()) {
            System.out.println("The specified directory does not exist.");
            return;
        }

        File[] files = directory.listFiles();

        if (files == null || files.length == 0) {
            System.out.println("The specified directory is empty.");
            return;
        }

        System.out.println("The following files will be deleted: ");

        for (File file : files) {
            System.out.println(file.getName());
        }

        System.out.print("Are you sure you want to delete these files? (Y/N): ");
        String confirmation = scanner.nextLine().trim().toLowerCase();

        if (confirmation.equals("y")) {
            for (File file : files) {
                file.delete();
            }

            System.out.println("Files deleted successfully.");
        } else {
            System.out.println("Operation cancelled by the user.");
        }
    }
}
