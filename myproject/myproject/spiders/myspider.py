import scrapy
from bs4 import BeautifulSoup
from ..items import MyItem
from urllib.parse import urljoin
import re

class MySpider(scrapy.Spider):
    name = "myspider"
    validate_phone_number_pattern = "^\\+?[1-9][0-9]{7,14}$"

    def __init__(self, start_url=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.start_urls = [start_url]
        self.base_url = start_url

        print(f"kwargs {kwargs}")
        self.museum = kwargs["museum"]
        self.city = kwargs["city"]

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract emails and phone numbers
        emails = set()
        phones = set()

        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if 'mailto:' in href:
                emails.add(href.split('mailto:')[1])

        for text in soup.stripped_strings:
            if '@' in text and '.' in text:
                emails.add(text)


            if re.match(self.validate_phone_number_pattern, text):
                phones.add(text)

        item = MyItem()
        item['emails'] = list(emails)
        item['phones'] = list(phones)
        item['url'] = response.url
        item['museum'] = self.museum
        item['city'] = self.city

        yield item

        # Follow links to subpages that start with the base URL
        for link in response.css('a::attr(href)').getall():
            full_url = urljoin(response.url, link)
            if full_url.startswith(self.base_url) and ("kontakt" in full_url or "impressum" in full_url):
                yield response.follow(link, self.parse)