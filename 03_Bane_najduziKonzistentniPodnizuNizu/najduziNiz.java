import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class najduziNiz {
    /*
     * 1 - Korisnik iz konzole unosi niz celih brojeva odvojeni razmakom
     *      - taj niz brojeva se privremeno cuva u kao String
     *      - zatim se radi pretvaranje elemenata tog niza iz String u int i cuva s u novi niz
     * 
     * 2 - Trazenje najduzeg neopadajuceg podniza
     *      2.1. Pravimo praznu listu koja ce sadrzati trenutni najduzi neopadajuci niz.
     *      2.2. Pravimo praznu listu koja ce sadrzati finalni najduzi neopadajuci niz.
     *      2.3. Prolazimo petljom kroz niz i proveravamo
     *           ako je trenutniNiz prazan ili 
     *           ako je trenutni element niza veci ili jednak poslednjem elementu u trenutniNiz, 
     *           dodaje se i-ti element u trenutniNiz.
     *          
     *           u suprotnom, Ako trenutni element nije veci ili jednak poslednjem elementu iz trenutniNiz, 
     *           stvara se nova lista trenutniNiz koja sadrzi samo trenutni element
     * 
     *           Na kraju ako je trenutniNiz duzi od najduziPodNiz, 
     *           azurira se najduziPodNiz tako da postane kopija trenutniNizs
     */

    public static void main(String[] args) {
        
        //1 0 2 5 4 5 6 7 7 2 4 5
        //int[] testNiz = new int[]{5, 8, 2, 3, 1, 10, 11, 12, 4, 5, 2};

        Scanner scanner = new Scanner(System.in);

        System.out.println("Unesi elemente niza odvojene razmakom: ");
        String[] uneseniNiz = scanner.nextLine().split(" ");

        int[] niz = new int[uneseniNiz.length];
        for (int i = 0; i < uneseniNiz.length; i++) {
            niz[i] = Integer.parseInt(uneseniNiz[i]);
        }

        List<Integer> najduziNeopadajuciPodNiz = pronadjiNajduziNeopadajuciPodNiz(niz);

        System.out.println("Najduzi neopadajuci podniz: " + najduziNeopadajuciPodNiz);
    }

    private static List<Integer> pronadjiNajduziNeopadajuciPodNiz(int[] niz) {

        List<Integer> trenutniNiz = new ArrayList<Integer>();
        List<Integer> najduziPodNiz = new ArrayList<Integer>();

        for (int i = 0; i < niz.length; i++) {
            if (trenutniNiz.isEmpty() || niz[i] >= trenutniNiz.get(trenutniNiz.size() - 1)) {
                trenutniNiz.add(niz[i]);
            } else {
                trenutniNiz = new ArrayList<Integer>(Arrays.asList(niz[i]));
            }

            if (trenutniNiz.size() > najduziPodNiz.size()) {
                najduziPodNiz = new ArrayList<Integer>(trenutniNiz);
            }
        }
        return najduziPodNiz;
    }
}
