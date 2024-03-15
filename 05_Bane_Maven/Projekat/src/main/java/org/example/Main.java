package org.example;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class Main {
    private static final Logger logger = LogManager.getLogger(Main.class);

    public static void main(String[] args) {
        try {
            System.setProperty("log4j.configurationFile", "log4j2.xml");

            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));


            // Validacija za unos imena (samo slova)
            String ime;
            do {
                logger.info("Unesite svoje ime (samo slova): ");
                ime = reader.readLine();
            } while (!ime.matches("[a-zA-Z]+"));

            // Validacija za unos broja kartice (samo brojevi)
            String brojKartice;
            do {
                logger.info("Unesite broj kartice (samo brojevi): ");
                brojKartice = reader.readLine();
            } while (!brojKartice.matches("[0-9]*"));

            // Provera postojanja naloga
            String imeBrojNaloga = ime + brojKartice;
            Path nalogaPath = Paths.get(imeBrojNaloga + ".txt");

            if (Files.exists(nalogaPath)) {
                // Pitanje za overwrite
                logger.info("Nalog sa unetim imenom i brojem kartice već postoji. Da li želite da ga overwrite-ujete? (Da/Ne): ");
                String odgovorOverwrite = reader.readLine().toLowerCase();

                if (!odgovorOverwrite.equals("da") && !odgovorOverwrite.equals("yes")) {
                    logger.info("Sledeci put unesite novo ime i broj kartice.");
                    return;  // Izlaz iz programa
                }
            }

            BufferedReader pitanjaReader = new BufferedReader(new FileReader("src/main/resources/pitanja.txt"));
            BufferedReader odgovoriReader = new BufferedReader(new FileReader("src/main/resources/odgovori.txt"));
            BufferedWriter logWriter = new BufferedWriter(new FileWriter("logs/logovi.txt", true));
            BufferedWriter userFileWriter = new BufferedWriter(new FileWriter(imeBrojNaloga + ".txt"));

            String linijaPitanja;
            String linijaOdgovora;
            int brojPitanja = 1;
            int brojPoena = 0;

            while ((linijaPitanja = pitanjaReader.readLine()) != null) {
                System.out.println("\nPitanje " + brojPitanja + ":");

                logger.info(linijaPitanja);
                System.out.print("Unesite odgovor na ovo pitanje: ");
                String odgovorKorisnika = reader.readLine();

                // Provera tačnosti odgovora
                linijaOdgovora = odgovoriReader.readLine();
                if (linijaOdgovora != null && linijaOdgovora.equals(odgovorKorisnika)) {
                    brojPoena++;
                }

                // Logovanje u fajl 'logovi.txt'
                logWriter.write("Pitanje " + brojPitanja + ": " + linijaPitanja + "\n");
                logWriter.write("Odgovor korisnika: " + odgovorKorisnika + "\n");
                logWriter.write("Tačan odgovor: " + linijaOdgovora + "\n");
                logWriter.write("-----------------------------------\n");

                // Pisanje u fajl 'ImeKorisnikaBrojKartice.txt'
                userFileWriter.write("Pitanje " + brojPitanja + ": " + linijaPitanja + "\n");
                userFileWriter.write("Odgovor korisnika: " + odgovorKorisnika + "\n");
                userFileWriter.write("-----------------------------------\n");

                brojPitanja++;
            }

            // Dodajemo informaciju o broju tačnih odgovora u fajl korisnika
            userFileWriter.write("Korisnik je imao '" + brojPoena + "' tačnih odgovora.\n");

            reader.close();
            pitanjaReader.close();
            odgovoriReader.close();
            logWriter.close();
            userFileWriter.close();

            logger.info("Test je zavrsen. Ostvarili ste " + brojPoena + " poena.");
        } catch (FileNotFoundException e){
            // exception, loguj los unos
        } catch (IOException e) {
            logger.error("Greska prilikom izvrsavanja programa", e);
        } catch (Exception e) {
            logger.error("Nepredviđena greška", e);
        }
    }
}
