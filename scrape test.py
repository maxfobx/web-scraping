from bs4 import BeautifulSoup  #pip3 install beautifulsoup4
import requests     #pip3 install requests

while True: # For keeping the whole program in continous loop
    l=input('Enter the word you want to find idioms of:\n')
    URL = ('https://idioms.thefreedictionary.com/'+l)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='w1')
    word_mean = results.find_all('div', class_='ds-single')

    for meaning in word_mean:
        # Each meaning is a new BeautifulSoup object.
        print(meaning.text.strip())
        print('\n')
