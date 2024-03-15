from bs4 import BeautifulSoup
import requests
import time

def find_job():
    html_text = requests.get('https://www.helloworld.rs/oglasi-za-posao/programiranje/beograd?tag=69&senioritet%5B0%5D=1&senioritet%5B1%5D=2').text
    soup = BeautifulSoup(html_text, 'lxml')

    for index, job in  enumerate(soup.find_all('div', class_='flex flex-col gap-4 flex-1 px-4 md:pl-4 mb-4 w-full')):
        job_title = job.find('a', class_='hover:opacity-50 font-bold text-lg').text
        company_name = job.find('h4', class_='font-semibold opacity-75').text
        job_skill = job.find('div', class_='flex items-center gap-2 flex-wrap').text
        job_link = job.div.h3.a['href']

        with open(f'jobs/{index}.txt', 'w') as f:
            f.write(f"Job Title: {job_title.strip()}")
            f.write(f"Company Name: {company_name.strip()}")
            f.write(f"Skills required: {job_skill.strip()}")
            f.write(f"LINK: https://www.helloworld.rs/{job_link}")
        print(f"File Saved {index}")

if __name__ == '__main__':
    while True:
        find_job()
        minutes = 10
        time.sleep(minutes*60) 