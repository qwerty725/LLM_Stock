import json
import csv
import requests
from bs4 import BeautifulSoup
import openai
import os


class Headlines_for_chatGPT():

    def scrape(self): #self refers to Stock object
        url='https://www.bbc.com/news/technology'
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
            # next(reader)  # Skip header row
            for row in reader:
                company_names.append(row[1])

        # Search for matching headlines
        matching_headlines = []
        for headline in news_headlines:
            for company_name in company_names:
                if company_name.lower() in headline.lower().split():
                    matching_headlines.append([company_name] + [headline])

        # Write the matching headlines to the output .csv file
        with open(spy_output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(matching_headlines)
        return matching_headlines

def chatGPT_output(matching_headlines):
    openai.api_key = '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'
    reply_list = []
    messages = [ {"role": "system", "content":
        "Forget all your previous instructions. Pretend you are a financial expert. You are a financial expert with stock recommendation experience."} ]
    for each in matching_headlines:
        company_name = each[0]
        current_headline = each[1]
        message = "Answer “YES” if good news, “NO” if bad news, or “UNKNOWN” if uncertain in the first line. "\
            "Then elaborate with one short and concise sentence on the next line. "\
            f"Is this headline good or bad for the stock price of {company_name} in the term term? Headline: {current_headline}"

        # if message:
        messages.append(
            {"role": "user", "content": message},
        )
        # openai.api_key = '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'
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages #3.5
        )
        reply = chat.choices[0].message.content
        reply_list.append(reply)
        print(f"ChatGPT: {reply_list}")
    
    return reply_list
        # messages.append({"role": "assistant", "content": reply})

if __name__ == '__main__':
    chatGPT_obj = Headlines_for_chatGPT()
    stock_list = []
    f = open("spy500.csv",'r')
    reader = csv.reader(f,delimiter=',')
    for line in reader:
        stock_list.append(line[0])
    print(stock_list[:10])
    news_headlines = chatGPT_obj.scrape()
    print(news_headlines)
    matching_headlines = chatGPT_obj.headlines_with_company("spy500.csv", news_headlines, "headlines_with_company.csv")
    reply_lists = chatGPT_output(matching_headlines)
    print(reply_lists)


