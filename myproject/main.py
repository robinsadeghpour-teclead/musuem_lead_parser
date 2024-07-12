import pandas as pd
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from myproject.spiders.myspider import MySpider  # Adjust the import to your project's structure

# Read the CSV file into a DataFrame
df = pd.read_csv('../museen.csv')

class ItemCollectorPipeline:
    def open_spider(self, spider):
        self.items = []

    def close_spider(self, spider):

        for item in self.items:
            print(item)

    def process_item(self, item, spider):
        self.items.append(item)
        return item

process = CrawlerProcess(settings={
    'ITEM_PIPELINES': {'__main__.ItemCollectorPipeline': 1},
})

# Iterate over each row in the DataFrame
for index, row in df.head(1).iterrows():
    museen = row['Museen']
    staedte = row['Staedte']
    webseiten = row['Webseiten']

    # Do something with the values
    result = process.crawl(MySpider, start_url=f'https://{webseiten}', museum=museen, city=staedte)

process.start()