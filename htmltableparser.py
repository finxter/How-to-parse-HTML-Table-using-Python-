#Import the necessary variables
import urllib.request
from html_table_parser.parser import HTMLTableParser
from tabulate import tabulate

#Opens a website,read its HTML Contents and store the contents to variable xhtml
url = "https://en.wikipedia.org/wiki/List_of_best-selling_books#More_than_100_million_copies"
req = urllib.request.Request(url=url)
f = urllib.request.urlopen(req)
xhtml = f.read().decode('utf-8')

#Define the object HTMLTableParser() and store  into variable p
p = HTMLTableParser()

#Feed the HTML contents to HTMLTableParser object 
p.feed(xhtml)

# Draw the Table
s = (p.tables[1])
print(tabulate(s,headers='firstrow', tablefmt='fancy_grid'))
