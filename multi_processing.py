from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup

base_url = 'http://quotes.toscrape.com/page/'

all_urls = list()

def generate_urls():
	for i in range(1,4):
		all_urls.append(base_url + str(i))
    
def scrape(url):
	res = requests.get(url)
	print(res.status_code, res.url)
	return url

if __name__ == '__main__':
	generate_urls()
	print(all_urls)

	p = Pool(3)
	results = p.map(scrape, all_urls)
	p.terminate()
	p.join()
	print(results)
