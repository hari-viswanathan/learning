import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.rottentomatoes.com/top/bestofrt/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}

def fetch_movie_details(movie_url):
    movie_f = requests.get(movie_url, headers = headers)
    movie_soup = BeautifulSoup(movie_f.content, 'lxml')
    movie_content = movie_soup.find('div', {
      'class': 'movie_synopsis clamp clamp-6 js-clamp'
    })
    print("Scraped {}".format(movie_url))
    return (movie_url, movie_content.string.strip())

if __name__ == '__main__':

    f = requests.get(url, headers = headers)
    movie_urls = []
    soup = BeautifulSoup(f.content, 'lxml')
    movies = soup.find('table', {'class': 'table'}).find_all('a')
    for anchor in movies:
        movie_urls.append('https://www.rottentomatoes.com' + anchor['href'])


    import time
    from concurrent.futures import ThreadPoolExecutor
    from multiprocessing import Pool
    start = time.time()
    with Pool(10) as executor:
        results = executor.map(fetch_movie_details, movie_urls[:30])

    print(results)
    for name, content in results:
        print(name, content)
    end = time.time()
    print("Time takes: {}s".format(end-start))
