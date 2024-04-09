import requests 
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


HEADERS = {'User-Agent':UserAgent().random}
SEARCH = 'https://eu.hitmotop.com/search?q={}'
URL = 'https://eu.hitmotop.com/'


def search_in_hitmotop(search):
    new_data = []
    result = search
    url = SEARCH.format(result)

    try:
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.text, 'lxml')
        data1 = soup.find('div', class_='content-inner')
        data2 = data1.find('ul', class_='tracks__list')
        data3 = data2.find_all('div', class_='track__info')
        
        for result in data3:
     

            track_title = result.find('div', class_='track__title').text.strip()
            track_content = result.find('div', class_='track__desc').text.strip()
            track_download = result.find('a', class_='track__download-btn').get('href')
            new_data.append([str(track_title), str(track_content), str(track_download)])
            
        return new_data
    except:
        return "NOW internet!"

# def main():
#     while True:
#         print(search_in_hitmotop(input("Search musik:  ")))


# if __name__=='__main__':

#     main()