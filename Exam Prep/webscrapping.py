import requests as rq
from bs4 import BeautifulSoup

url = "https://www.reddit.com/"
response = rq.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    para = soup.find_all("p")
    for p in para:
        print(p.text)

print(response)
