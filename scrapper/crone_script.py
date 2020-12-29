from database.database import DataBase
from scrapper.crawler import WebCrawler
from models import Currencies


def perform_scrapping():
    database = DataBase('db.json')
    my_crawler = WebCrawler()
    my_crawler.get_google_cookies()

    for cur in Currencies:
        my_crawler.get_exchange_rate(cur.title().lower())
        database.insert_data(my_crawler.data_dict)

    return database

if __name__ == "__main__":
    perform_scrapping()
