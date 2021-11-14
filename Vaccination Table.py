import urllib.request
from html_table_parser.parser import HTMLTableParser
from tabulate import tabulate
""" Opens a website and read its binary contents (HTTP Response Body) """
url = "https://www.bbc.com/news/world-56237778"
req = urllib.request.Request(url=url)
f = urllib.request.urlopen(req)
xhtml = f.read().decode('utf-8')
p = HTMLTableParser()
p.feed(xhtml)
s = (p.tables[0])
print(tabulate(s,headers='firstrow',tablefmt='fancy_grid'))
