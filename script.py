import requests
from bs4 import BeautifulSoup
import csv

webpage_response = requests.get('http://quotes.toscrape.com/tag/love/')

webpage = webpage_response.content

soup = BeautifulSoup(webpage, "html.parser")
quotes = soup.find_all("span", attrs={"class":"text"})
authors = soup.find_all("small", attrs={"class":"author"})

file = open("scraped_quotes.csv", "w")
writer = csv.writer(file)

writer.writerow(["QUOTES", "AUTHORS"])

for quote, author in zip(quotes, authors):
    writer.writerow([quote.text, author.text])
file.close()