from bs4 import BeautifulSoup

import get_site


def page_opinions(j, i, number_opinion):
    print(f'Мы на странице {str(j)} звезды {str(i)}')
    soup = get_site.get_site('/' + str(j) + '/?ratio='+str(i))
    rewiew_opinion = soup.find_all(class_='review-title')  # находим заголовки(тему)
    plus = soup.find_all(class_='review-plus')  # находим достоинство
    minus = soup.find_all(class_='review-minus')  # находим негатив
    opinion = soup.find_all(class_='review-teaser')  # находим отзыв
    print(str(len(rewiew_opinion))+str(len(plus))+str(len(minus))+str(len(opinion)))
    for h in range(20):
        text = rewiew_opinion[h].text+'\n\nДостоинства: '+plus[h].text+'\nНедостатки: '+minus[h].text+'\nОтзыв: '+opinion[h].text
        namefile = str(number_opinion).zfill(4)
        with open('dataset/' + str(i) + '/' + namefile + '.txt', 'w+', encoding="utf-8") as file:
            file.write(text)
        print(f'Звезда {str(i)} отзыв {namefile} создан')
        number_opinion+=1
    return number_opinion