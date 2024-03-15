import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class provera {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Unesi elemente niza odvojene razmakom: ");
        String[] inputArray = scanner.nextLine().split(" ");

        int[] array = new int[inputArray.length];
        for (int i = 0; i < inputArray.length; i++) {
            array[i] = Integer.parseInt(inputArray[i]);
        }

        for (String element : inputArray) {
            System.out.println(element);
        }

        System.out.println("---------------------------------------------");

        for (int element : array) {
            System.out.println(element);
        }
    }

    /*  [2,2,5,]
     *  [1, 10]
     *  [2, 2, 5 ,1 10]
     * 
     * 
     */

}
