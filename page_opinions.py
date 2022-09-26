import requests
import info
from bs4 import BeautifulSoup
import time


def page_opinions(j, i, number_opinion,):
    print("Мы на странице " + str(j) + ' звезды ' + str(i))
    time.sleep(5)
    html_text = requests.get(info.base_URL + '/' + str(j) + '/?ratio=' + str(i),
                             headers={"User-Agent": info.user_agent}).text
    soup = bs4(html_text, 'lxml')
    review_title = soup.find_all('a', class_='review-title')
    review_plus = soup.find_all('a', class_='review-plus')
    review_minus = soup.find_all('a', class_='review-minus')
    review_teaser = soup.find_all(class_='review_teaser', itempop='description')
    for h in range(len(review_title)):
        text = ''
        text = review_title[h].text + '\nДостоинства:\n' + plus[h].text + '\n' + 'Недостатки:\n' + minus[
            h].text + '\n' + '\nОтзыв:\n' + review_teaser[h].text
        if number_opinion >= 3:  # 1
            namefile = '0' + str(number_opinion)
        elif number_opinion >= 2:
            namefile = '00' + str(number_opinion)
        elif number_opinion >= 1:
            namefile = '000' + str(number_opinion)
        else:
            namefile = "0000" + str(number_opinion)
        with open('dataset/' + str(i) + '/' + namefile + '.txt', 'w+') as file:
            file.write(text)
        print('Звезда ' + str(i) + ' отзыв ' + namefile + ' создан')
        number_opinion += 1
