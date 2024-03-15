class Porudzbina {
    private String naziv;
    private int kolicina;

    public Porudzbina(String naziv, int kolicina) {
        this.naziv = naziv;
        this.kolicina = kolicina;
    }

    public String getNaziv() {
        return naziv;
    }

    public int getKolicina() {
        return kolicina;
    }
}