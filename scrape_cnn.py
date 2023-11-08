import requests
from bs4 import BeautifulSoup

def scrape_cnn(URL):
    try:
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        headline = soup.find(class_="headline__text inline-placeholder")
        content = soup.find(class_="article__content").findChildren(class_="paragraph inline-placeholder")
        
        print(headline.getText().strip())
        for child in content:
            print(child.text.strip())
    except:
        print("Something went wrong")
                
if __name__ == "__main__":
    url = input("Enter the URL of the CNN article: ")
    scrape_cnn(url)