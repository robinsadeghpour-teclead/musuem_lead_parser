import pandas as pd
import ContactInfoScraper
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from myproject.myproject.spiders.myspider import MySpider

# Read the CSV file into a DataFrame
df = pd.read_csv('museen.csv')
process = CrawlerProcess(get_project_settings())

# Iterate over each row in the DataFrame
for index, row in df.head(5).iterrows():
    museen = row['Museen']
    staedte = row['Staedte']
    webseiten = row['Webseiten']

    # Do something with the values
    result = process.crawl(MySpider, start_url=webseiten)
    print(result)

process.start()