from bs4 import BeautifulSoup
import requests
import csv

# Pretvaranje html stranice u tekstualni format
source = requests.get('http://coreyms.com').text        
# Prosledjivanje tog teksta u BS i parsiranje u format 'lxml'
soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

# Article je sekcija u HTML-u u kome se nalazi sadrzaj
# Prodje kroz taj svaki artikl i vadi podatke
for article in soup.find_all('article'):
    # 1. Naslov, koji je na putanji : article/h2/a
    headline = article.h2.a.text
    print(headline)
    # 2. Opis, koji je na putanji : article/div/p
    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        # 3. Video, koji je na putanji : article/iframe/src/4Element/0Element
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
