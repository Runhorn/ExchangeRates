from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from datetime import datetime
import re


class WebCrawler:
    def __init__(self):
        self.options = Options()
        self.options.add_argument("--headless")
        self.options.add_argument("--lang=en")
        self.driver = webdriver.Firefox(options=self.options)
        self.driver.implicitly_wait(1)
        self.data_dict = {
            'exchange_rate': 0.0,
            'date': '',
            'hour': '',
            'currency': ''
        }

    def get_google_cookies(self):
        self.driver.get(
            'https://consent.google.com?hl=pl&origin=https://www.google.com&continue=https://www.google.com/search?q%3DPLN%2BTO%2BUSD&if=1&m=0&pc=s&wp=-1&gl=PL')
        self.driver.find_element_by_id('introAgreeButton').click()

    @staticmethod
    def process_text_data(page_text):
        exchange_rate = float(page_text.splitlines()[1][:-6].replace(',', '.'))
        date = re.split("UTC", page_text.splitlines()[2])[0][:-1] + ':00'
        regex = re.compile(r"(\d+) ([a-z]+), (\d{2}:\d{2}:\d{2})")
        m = regex.match(date)
        month_dict = {
            'sty': '1',
            'lut': '2',
            'mar': '3',
            'kwi': '4',
            'maj': '5',
            'cze': '6',
            'lip': '7',
            'sie': '8',
            'wrz': '9',
            'paz': '10',
            'lis': '11',
            'gru': '12'
        }
        date = m.group(1) + '-' + month_dict[m.group(2)] + '-' + str(datetime.today().year)
        hour = m.group(3)
        return exchange_rate, date, hour

    def get_exchange_rate(self, currency):
        self.driver.get('https://google.com/search?q=' + currency)
        page_text = self.driver.find_element_by_id('knowledge-currency__updatable-data-column').text
        exchange_rate, date, hour = self.process_text_data(page_text)
        self.data_dict['date'] = date
        self.data_dict['hour'] = hour
        self.data_dict['exchange_rate'] = exchange_rate
        self.data_dict['currency'] = currency
