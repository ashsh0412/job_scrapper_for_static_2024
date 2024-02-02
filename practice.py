import requests
from bs4 import BeautifulSoup

keywords = ["flutter", "python", "golang"]

def job_scrapper(keyword):

    jobs = []

    url = f"https://remoteok.com/remote-{keyword}-jobs"

    response = requests.get(url, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",})

    soup = BeautifulSoup(response.content, "html.parser")

    sections = soup.find_all("td", class_="company position company_and_position")

    for section in sections:
        title = section.find("h2").text
        company = section.find("h3").text
        location = str(section.select_one("div"))[22:-6]

        job = {
            "title" : title,
            "company" : company,
            "location" : location,
        }
        
        jobs.append(job)
    print(jobs)

for keyword in keywords:
    job_scrapper(keyword)

    
    
