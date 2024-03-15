import java.util.Scanner;

public class check {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        System.out.print("Unesi text: ");
        String unos = s.nextLine();

        if(unos.equals("UROS")){
            System.out.println("Uneo si UROS");
        }else{
            System.out.println("Nisi uneo UROS");
        }
    }
}
