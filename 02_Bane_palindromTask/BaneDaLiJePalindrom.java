import java.util.Scanner;

public class BaneDaLiJePalindrom {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("Provera da li je palindrom ('IZLAZ' za kraj programa): ");
            String unos = scanner.nextLine();

            if ("IZLAZ".equals(unos)) {
                System.out.print("Program zavrsen.");
                break;
            }

            if (imaViseRazmaka(unos)) {
                System.out.println("Uneta rec nije palindrom jer sadrži dva ili više razmaka.");
            } else {
                if (jePalindrom(ukloniBeline(unos))) {
                    System.out.println("Uneta rec je palindrom.");
                } else {
                    System.out.println("Uneta rec nije palindrom.");
                }
            }
        }
        scanner.close();
    }
    
    /* Metoda koja proverava da li u inputu ima 2 ili vise razmaka */
    private static boolean imaViseRazmaka(String str) {
        return str.matches(".*\\s{2,}.*");
    }

    /* Metoda koja proverava da li je rec palindrom */
    private static boolean jePalindrom(String str) {
        return str.equals(new StringBuilder(str).reverse().toString());
    }

    /* Metoda koja brise razmake */
    private static String ukloniBeline(String str) {
        return str.replaceAll("\\s", "");
    }
}
