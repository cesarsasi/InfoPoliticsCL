from scrapers.utils import get_session
from bs4 import BeautifulSoup

# Listas de noticias con distintos tags
list_urls = [
    'https://www.ciperchile.cl/tag/corrupcion/page/{}'
]
# .format reemplaza {}


def ciper():
    session = get_session()
    news_urls = []
    for list_url in list_urls:
        page = 1
        while True:
            page_url = list_url.format(page)
            response = session.get(page_url)

            if response.status_code == 404:
                break

            text = response.text

            soup = BeautifulSoup(text, 'html.parser')

            news_list = soup.find('section', 'bg-gray').findAll('article')
            for new in news_list:
                new_url = new.find('a').get('href')
                news_urls.append(new_url)

            page += 1

    for new_url in news_urls:
        response = session.get(new_url)
        text = response.text
        soup = BeautifulSoup(text, 'html.parser')
        scrape_new(soup)


# Como guardar la información (archivos para solr)
def scrape_new(soup):
    print('Aqui se scrapea la noticia')


# David: Mi recomendacion, Archivo JSON
"""
{
    title: Titulo de la noticia
    date: Es importante
    excerpt: Bajada de la noticia
    body: Cuerpo de la noticia
}
Buscar como guardar el archivo en otra carpeta fuera de ScraperInfoPoliticsCL
"""