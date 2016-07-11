#!/usr/bin/python
import bs4
import urllib

abc="https://www2.bmreports.com/bmrs/?q=remit"
print abc
page = urllib.urlopen(abc)
data = page.read()
soup = bs4.BeautifulSoup(data, 'html.parser')
table = soup.findAll('table', id='myTable1')
print type(table)
