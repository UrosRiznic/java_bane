import java.util.Random;

class Musterija {
    private String ime;
    private int povlastenaKartica;
    private PolovnaPorudzbina polovnaPorudzbina;
    private Porudzbina porudzbina;
    // porudzbina ide lista porudzbina

    public Musterija(String ime, PolovnaPorudzbina polovnaPorudzbina) {
        this.ime = ime;
        this.povlastenaKartica = new Random().nextInt(1000); // Random broj za karticu
        this.polovnaPorudzbina = polovnaPorudzbina;
        this.porudzbina = new Porudzbina();
    }

    public void dodajStavkuPorudzbine(String pecivo, int kolicina) {
        porudzbina.dodajStavku(pecivo, kolicina);
    }

    public Porudzbina getPorudzbina() {
        return porudzbina;
    }

    public String getIme() {
        return ime;
    }

    public int getPovlastenaKartica() {
        return povlastenaKartica;
    }

    public PolovnaPorudzbina getPolovnaPorudzbina() {
        return polovnaPorudzbina;
    }
}