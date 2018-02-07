from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

writer = csv.writer(open('amazon_sellers.csv', 'wb'))
writer.writerow(['Book'])


book_list = []
driver = webdriver.PhantomJS(executable_path = r'/Users/panda/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')

for page in range(1,6):

	url = 'https://www.amazon.com/best-sellers-books-Amazon/zgbs/books#{0}'.format(page)

	print url

	driver.get(url)

	time.sleep(3)

	soup = BeautifulSoup(driver.page_source, 'lxml')

	print len(soup.find_all('div',class_ = 'zg_itemImmersion'))

	for div in soup.find_all('div',class_ = 'zg_itemImmersion'):
		# print div.find('div', class_ = 'zg_title').text
		book_list.append(div.find('div', class_ = 'p13n-sc-truncated').text)

for book in book_list:
	writer.writerow([book.encode('utf-8')])
