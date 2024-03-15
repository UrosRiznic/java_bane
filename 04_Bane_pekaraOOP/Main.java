public class Main {
    public static void main(String[] args) {
        Pekara pekara = new Pekara();
        /* 
        Musterija musterija1 = new Musterija("Marko", PolovnaPorudzbina.HOCU_POLOVICNU_PORUDZBINU);
        Musterija musterija2 = new Musterija("Ivan", PolovnaPorudzbina.NECU_POLOVICNU_PORUDZBINU);
        Musterija musterija3 = new Musterija("Kalina", PolovnaPorudzbina.HOCU_POLOVICNU_PORUDZBINU);
        Musterija musterija4 = new Musterija("Shawn", PolovnaPorudzbina.NECU_POLOVICNU_PORUDZBINU);
        Musterija musterija5 = new Musterija("Marija", PolovnaPorudzbina.HOCU_POLOVICNU_PORUDZBINU);
        Musterija musterija6 = new Musterija("Mare", PolovnaPorudzbina.HOCU_POLOVICNU_PORUDZBINU);

        // Porudžbine
        pekara.izvrsiTransakciju(musterija1, "hleb", 6);
        System.out.println("--------------------------------");
        pekara.izvrsiTransakciju(musterija2, "krofne", 4);
        System.out.println("--------------------------------");
        pekara.izvrsiTransakciju(musterija3, "hleb", 8);
        System.out.println("--------------------------------");
        pekara.izvrsiTransakciju(musterija4, "kroasani", 5);
        System.out.println("--------------------------------");
        pekara.izvrsiTransakciju(musterija5, "kifle", 3);
        System.out.println("--------------------------------");
        pekara.izvrsiTransakciju(musterija6, "kifle", 7);
        System.out.println("--------------------------------");
        // Prikaz trenutno stanje peciva
        System.out.println("Trenutno stanje peciva:");
        for (Pecivo pecivo : pekara.getPeciva().values()) {
            System.out.println(pecivo.getNaziv() + ": " + pecivo.getKolicina());
        }
        */

        Musterija musterija7 = new Musterija("Marko", PolovnaPorudzbina.HOCU_POLOVICNU_PORUDZBINU);
        musterija7.dodajStavkuPorudzbine("hleb", 5);
        musterija7.dodajStavkuPorudzbine("krofne", 10);
        pekara.izvrsiTransakciju(musterija7);
        System.out.println("--------------------------------");

        Musterija musterija10 = new Musterija("Marko", PolovnaPorudzbina.HOCU_POLOVICNU_PORUDZBINU);
        
        musterija10.dodajStavkuPorudzbine("kifle", 3);
        pekara.izvrsiTransakciju(musterija10);
        System.out.println("----------------------------------");

        Musterija musterija8 = new Musterija("Ana", PolovnaPorudzbina.HOCU_POLOVICNU_PORUDZBINU);
        musterija8.dodajStavkuPorudzbine("hleb", 1);
        musterija8.dodajStavkuPorudzbine("kifle", 9);
        pekara.izvrsiTransakciju(musterija8);
        System.out.println("--------------------------------");

        Musterija musterija9 = new Musterija("Nemanja", PolovnaPorudzbina.NECU_POLOVICNU_PORUDZBINU);
        musterija9.dodajStavkuPorudzbine("kifle", 3);
        musterija9.dodajStavkuPorudzbine("kroasani", 7);
        pekara.izvrsiTransakciju(musterija9);
        System.out.println("--------------------------------");

    }
}


