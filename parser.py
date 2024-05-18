from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from random import randint
from app.handlers import image
def parser():
    url = 'https://ru.freepik.com/free-photos-vectors/motivation/' + str(randint(1, 100)) + '#uuid=6e83ad0c-97a3-4a90-86b8-38f657612b69'
    profile = UserAgent()
    page = requests.get(url, headers={'User-Agent': profile.random})
    soup = BeautifulSoup(page.content, 'html.parser')
    img = soup.findAll('a', class_ = 'showcase__link js-detail-data-link')
    for pic in img:
        url = pic.find("img").get("data-src")
        image(url)