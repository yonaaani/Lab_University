import java.awt.*;
import java.awt.Insets;
import javax.swing.*;
import javax.swing.border.EmptyBorder;
public class MyLayoutDemo {
    public static void main(String[] args){
        JFrame jf = new JFrame();
        jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //Створюю
        Container boxGlobal = jf.getContentPane();
        Box boxLogin = Box.createHorizontalBox();
        Box boxPassword = Box.createHorizontalBox();
        Box boxButton = Box.createHorizontalBox();

        boxGlobal.setLayout(new BoxLayout(boxGlobal, BoxLayout.Y_AXIS));


        JLabel jLogin = new JLabel("Логін:");
        JLabel jPassword = new JLabel("Пароль:");
        //JTextField це легкий компонент, який дозволяє редагувати один рядок тексту, тобто до 15 символів
        JTextField jFLogin = new JTextField(15);
        JTextField jFPassword = new JTextField(15);
        JButton buttonOk = new JButton("ОК");
        JButton buttonCancel = new JButton("Відміна");


        jFLogin.setMargin(new Insets(0,10,0,10));
        jFPassword.setMargin(new Insets(0,10,0,10));

        jLogin.setPreferredSize(jPassword.getPreferredSize());

        //Додаю
        boxLogin.add(jLogin);
        //щоб створити невидимий компонент між двома штучками
        boxLogin.add(Box.createHorizontalStrut(6));
        boxLogin.add(jFLogin);

        boxPassword.add(jPassword);
        boxPassword.add(Box.createHorizontalStrut(6));
        boxPassword.add(jFPassword);

        boxButton.add(Box.createHorizontalGlue());
        boxButton.add(buttonOk);
        boxButton.add(Box.createHorizontalStrut(12));
        boxButton.add(buttonCancel);

        boxGlobal.setBounds(12,12,12,12);

        boxLogin.setBorder(new EmptyBorder(12,12,0,12));
        boxPassword.setBorder(new EmptyBorder(0,12,0,12));
        boxButton.setBorder(new EmptyBorder(0,12,12,12));

        boxGlobal.add(boxLogin);
        boxGlobal.add(Box.createVerticalStrut(12));
        boxGlobal.add(boxPassword);
        boxGlobal.add(Box.createVerticalStrut(17));
        boxGlobal.add(boxButton);

        jf.pack();
        //зміна вікна заборонено
        jf.setResizable(false);
        jf.setVisible(true);
    }
}
