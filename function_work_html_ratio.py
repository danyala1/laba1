
import get_site
import page_opinions


def function_work_html_ratio(i):
    soup = get_site.get_site('/?ratio='+str(i))
    info_max_page = soup.find('a', class_='pager-item last tooltip-top', href=True)
    # находим кнопку посследней макс страницы
    info_max_page = info_max_page['href']
    slash = info_max_page.split('/')  # slash[3] - номер макс страницы, делим адресс строки на части
    print(f'Нашли макс количество страниц для звезды: {str(slash[3])}')
    number_opinion = 1
    for j in range(int(slash[3])):  # slash[3]
        number_opinion = page_opinions.page_opinions(j, i, number_opinion)