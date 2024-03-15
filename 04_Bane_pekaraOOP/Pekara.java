import java.util.HashMap;
import java.util.Map;

class Pekara {
    private Map<String, Pecivo> peciva;

    public Pekara() {
        this.peciva = new HashMap<>();
        peciva.put("hleb", new Pecivo("hleb", 5));
        peciva.put("kifle", new Pecivo("kifle", 10));
        peciva.put("krofne", new Pecivo("krofne", 20));
        peciva.put("kroasani", new Pecivo("kroasani", 30));
    }

    public Map<String, Pecivo> getPeciva() {
        return peciva;
    }

    public boolean izvrsiTransakciju(Musterija musterija) {
        ispisiStanjeNamirnica();

        Map<String, Integer> narudzbina = musterija.getPorudzbina().getStavke();

        for (Map.Entry<String, Integer> stavka : narudzbina.entrySet()) {
            String pecivo = stavka.getKey();
            int kolicina = stavka.getValue();

            Pecivo odabranoPecivo = peciva.get(pecivo);
            if (odabranoPecivo != null){
                if (odabranoPecivo.getKolicina() >= kolicina) {
                    odabranoPecivo.smanjiKolicinu(kolicina);
                    System.out.println("Transakcija uspesna: " + musterija.getIme() +
                    " kupuje " + kolicina + " " + pecivo + " sa karticom " + musterija.getPovlastenaKartica());
                } else if (odabranoPecivo.getKolicina() < kolicina && musterija.getPolovnaPorudzbina() == PolovnaPorudzbina.NECU_POLOVICNU_PORUDZBINU) {
                    System.out.println("Transakcija neuspesna: " + musterija.getIme() +
                    " nije moguce kupiti " + kolicina + " " + pecivo);
                    ispisiStanjeNamirnica();
                    // isprazniti listu
                    return false;
                } else if(odabranoPecivo.getKolicina() < kolicina && odabranoPecivo.getKolicina() > 0 && musterija.getPolovnaPorudzbina() == PolovnaPorudzbina.HOCU_POLOVICNU_PORUDZBINU) {
                    int prodataKolicina = odabranoPecivo.getKolicina();
                    odabranoPecivo.smanjiKolicinu(prodataKolicina);
                    System.out.println("Transakcija uspesna (polovinu): " + musterija.getIme() +
                        " kupuje " + prodataKolicina + " " + pecivo + " sa karticom " + musterija.getPovlastenaKartica());
                    
                    //return true;
                }
            }else{
                System.out.println("Transakcija neuspesna: " + musterija.getIme() +
                " nije moguce kupiti " + kolicina + " " + pecivo);
                ispisiStanjeNamirnica();
                return false;
            }
        }
        // praznjeje liste 
        proveraObnova();
        ispisiStanjeNamirnica();
        return true;
    }
    
    // Metoda za ispisivanje stanja namirnica
    private void ispisiStanjeNamirnica() {
        System.out.println("Stanje namirnica:");
    
        for (Map.Entry<String, Pecivo> entry : peciva.entrySet()) {
            String tipPeciva = entry.getKey();
            int kolicina = entry.getValue().getKolicina();
            System.out.println(tipPeciva + ": " + kolicina);
        }
    
        System.out.println("---------------");
    }
    
    public void proveraObnova(){
        if ((peciva.get("krofne").getKolicina() == 0 && peciva.get("kroasani").getKolicina() == 0)) {                    
            peciva.get("krofne").obnoviKolicinu(20);
            peciva.get("kroasani").obnoviKolicinu(30);
            System.out.println("Obnovljene slatke namirnice.");
        }
        if ((peciva.get("hleb").getKolicina() == 0 && peciva.get("kifle").getKolicina() == 0)) {                    
            peciva.get("hleb").obnoviKolicinu(5);
            peciva.get("kifle").obnoviKolicinu(10);
            System.out.println("Obnovljene slane namirnice.");
        }
    }
}