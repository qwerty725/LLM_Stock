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
        # Make a request to the Google Finance website
        # url='https://www.bbc.com/news'
        # response = requests.get(url)

        # soup = BeautifulSoup(response.text, 'html.parser')
        # headlines = soup.find('body').find_all('h3')
        # for x in headlines:
        #     print(x.text.strip())


        url = "https://finance.google.com/"
        response = requests.get(url)

        # Parse the HTML response
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all the headline elements that contain the word "hours ago"
       # headlines = soup.find('body')
        headlines = soup.find_all("div")
            
        # find_all("Yfwt5")
        # soup.find_all("Yfwt5")
                                 #  class_="story-title", text=lambda text: text.find("hours ago") != -1)
       # soup.find('body').find_all(

        # Print the headlines
        for headline in headlines:
            if "Yfwt5" in headline.class_:
                  print(headline.text.strip())
    
if __name__ == '__main__':
    test = Stock("sam", 25)
    print(test.price)
    stock_list = []
    f = open("spy500.csv",'r')
    reader = csv.reader(f,delimiter=',')
    for line in reader:
        stock_list.append(line[0])
    print(stock_list[:10])
    test.scrape()