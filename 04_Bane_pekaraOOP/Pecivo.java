class Pecivo {
    private String naziv;
    private int kolicina;

    public Pecivo(String naziv, int pocetnaKolicina) {
        this.naziv = naziv;
        this.kolicina = pocetnaKolicina;
    }

    public String getNaziv() {
        return naziv;
    }

    public int getKolicina() {
        return kolicina;
    }

    public void smanjiKolicinu(int kolicina) {
        this.kolicina -= kolicina;
    }

    public void obnoviKolicinu(int pocetnaKolicina) {
        this.kolicina = pocetnaKolicina;
    }
}