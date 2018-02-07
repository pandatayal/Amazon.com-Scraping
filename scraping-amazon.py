from bs4 import BeautifulSoup
from selenium import webdriver
import csv

writer = csv.writer(open('amazon_python_books.csv', 'wb'))
writer.writerow(['Book Title', 'Book Link', 'ISBN', 'Description'])

class Book():
    """docstring for Book"""
    def __init__(self):
        self.title = ""
        self.link = ""
        self.isbn = ""
        self.desc = ""

def get_book_list():
    driver = webdriver.Chrome('/Users/panda/Downloads/chromedriver')

    url = 'https://www.amazon.com/s/ref=nb_sb_noss/133-6150266-8278807?url=search-alias%3Daps&field-keywords=python+programming'

    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')

    ul = soup.find('ul', {'id':'s-results-list-atf'})

    book_list = []

    for li in ul.find_all('li', class_ = 's-result-item'):
        all_a = li.find_all('a', class_ ='a-link-normal')

        book = Book()
        book.title = all_a[1].text
        book.link = all_a[1]['href']
        print book.link
        book_list.append(book)

    driver.quit()
    return book_list

def get_book_info(book_list):
    driver = webdriver.Chrome('/Users/panda/Downloads/chromedriver')

    for b in book_list[2:]:
        url = b.link
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'lxml')

        table = soup.find('table', {'id':'productDetailsTable'})

        all_li = table.find_all('li')

        isbn = all_li[3].text.strip('ISBN-10: ')
        b.isbn = isbn


        #driver.switch_to_frame( driver.find_element_by_tag_name('iframe'))

        #soup = BeautifulSoup(driver.page_source,'lxml')

        #description = soup.find('div').text
        #b.desc = description
        writer.writerow([b.title.encode('utf-8'),
                         b.link.encode('utf-8'),
                         b.isbn.encode('utf-8')])
                         #b.desc.encode('utf-8')])

    driver.quit()
#    return book_list

booklist = get_book_list()
get_book_info(booklist)

#for book in books:
#    writer.writerow([book.title.encode('utf-8'),
    #                book.link.encode('utf-8')])

#get_book_list()
#for book in books:
#    print book.title
##    print book.isbn
#    print book.desc
