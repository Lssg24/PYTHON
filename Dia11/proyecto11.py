import bs4
import requests

url_base = 'https://books.toscrape.com/catalogue/page-{}.html'
formato = 1
code = requests.get(url_base.format(formato))
titulos_rating_alto = []
while code.status_code != 404:
    code = requests.get(url_base.format(formato))
    sopa = bs4.BeautifulSoup(code.text, 'lxml')
    libros = sopa.select('.product_pod')
    for l in libros:
        if len(l.select('.star-rating.Four')) != 0 or len(l.select('.star-rating.Five')) != 0:
            titulo = l.select('a')[1]['title']
            titulos_rating_alto.append(titulo)
    formato += 1

for t in titulos_rating_alto:
    print(t)
