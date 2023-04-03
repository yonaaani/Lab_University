import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Student {
    private String name;
    private int course;

    public Student(String name, int course){
        this.setName(name);
        this.setCourse(course);
    }

    public Student(Student otherStudent) {
        this(otherStudent.name, otherStudent.course);
    }

    public void copyFrom(Student otherStudent){
        this.name = otherStudent.name;
        this.course = otherStudent.course;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getCourse(){
        return course;
    }

    public void setCourse(int course) {
        this.course = course;
    }

    public static void printList(List students, int course) {
        System.out.println("Список студентів, які навчаються на "+ course + " курсі:");
        for(Iterator i = students.iterator(); i.hasNext();){
            Student student = (Student) i.next();
            if(student.getCourse() == course) {
                System.out.println(student.getName());
            }
        }
    }

    public static void main(String[] args) {
        List<Student> myList = new ArrayList<Student>();
        myList.add(new Student("Вася",1));
        myList.add(new Student("Петро",1));
        myList.add(new Student("Таня",4));
        myList.add(new Student("Саша",3));

        Student x = new Student("Міша",2);
        Student y = new Student(x);
        myList.add(y);

        x.copyFrom(new Student("Вероніка",3));
        myList.add(x);

        printList(myList, 1);
        printList(myList, 2);
        printList(myList, 3);
        printList(myList, 4);
    }
}
