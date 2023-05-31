import json
import csv
import requests
from bs4 import BeautifulSoup

def median(pool):
    copy = sorted(pool)
    size = len(copy)
    if size % 2 == 1:
        return copy[int((size - 1) / 2)]
    else:
        return (copy[int(size/2 - 1)] + copy[int(size/2)]) / 2
class Stock():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def scrape(self):
        url='https://www.bbc.com/news'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find('body').find_all('h3')
        news_headlines = []
        for x in headlines:
            news_headlines.append(x.text.strip())
        return news_headlines


        # url = "https://www.google.com/finance/"
        # response = requests.get(url)
        # soup = BeautifulSoup(response.text, "html.parser")
        # headlines = soup.find('body').find_all('div', class_='Yfwt5')
        # for headline in headlines:
        #     print(headline.text.strip())

    def headlines_with_company(self, spy_input_file, news_headlines, spy_output_file):
        company_names = []

        # Read the input .csv file and extract company names
        with open(spy_input_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header row
            for row in reader:
                company_names.append(row[1])

        # Search for matching headlines
        matching_headlines = []
        for headline in news_headlines:
            for company_name in company_names:
                if company_name.lower() in headline.lower.split():
                    matching_headlines.append([company_name] + [headline])

        # Write the matching headlines to the output .csv file
        with open(spy_output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(matching_headlines)

if __name__ == '__main__':
    test = Stock("sam", 25)
    print(test.price)
    stock_list = []
    f = open("spy500.csv",'r')
    reader = csv.reader(f,delimiter=',')
    for line in reader:
        stock_list.append(line[0])
    print(stock_list[:10])
    news_headlines = test.scrape()
    print(news_headlines)
    test.headlines_with_company("spy500.csv", news_headlines, "headlines_with_company.csv")