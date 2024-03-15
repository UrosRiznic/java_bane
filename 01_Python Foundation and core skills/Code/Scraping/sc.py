from bs4 import BeautifulSoup
import requests

# 1. Ucitavanje HTML-a
#   - Mozemo da ucitamo HTML kao link
#   - Mozemo da ucitamo HTML kao FILE.hmtl 

# Ovo je primer ucitavanja sa fajla
# - Prvo kazemo koji fajl otvaramo
# - Zatim taj fajl prosledimo BeautifulSoap-u i kazemo u kom formatu zelimo da ga parsiramo (u ovom slucaju kao lxml)
# - Sada se u promenljivoj 'soup' nalazi ceo nas dokument i mozemo ga seci na komadice i pristupati svakom elementu
with open(r'C:\Users\U6071367\OneDrive - Clarivate Analytics\Desktop\Programiranje\Python\Revizija\Scraping\simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')            

# Pristup divu koji ima klasu 'footer'
# Dakle ovde trazimo div, a ujedno i div koji ima klasu footer
# kod class stoji donja crta zato sto je class rezervisana rec u Pythonu, pa mora da se stoji _
match_1 = soup.find('div', class_='footer')
#print(match_1)

for article in soup.find_all('div', class_='article'):  
    headline = article.h2.a.text
    #print(headline)

    summary = article.p.text
    #print(summary)
    #print("-------------")

# ---------------------------------------------------------------------------------------





