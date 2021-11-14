# Import the required library
from lxml import html,etree
from tabulate import tabulate

# Provide the path of the html file
html_file = "/Users/mohamedthoufeeq/Desktop/UPWORK PROJECTS/Fixnter/HTML TABLE /List of best-selling books - Wikipedia.html"


# Open the html file and Parse it, 
# returning a single element/document.
with open(html_file,'r',encoding='utf-8') as inpt:
    html_doc = html.fromstring(inpt.read())
    
# Open a BestSellingBooksLists.xml file and write the 
# element/document to an encoded string 
# representation of its XML tree.
with open("BestSellingBooksLists.xml",'wb',) as outpt:
    outpt.write(etree.tostring(html_doc))
#Parse the contents of HTML and store it to table_tree variable                
table_tree = etree.parse("/Users/mohamedthoufeeq/Desktop/UPWORK PROJECTS/Fixnter/HTML TABLE /BestSellingBooksLists.xml")

#Extracting data from the table
Main_Heading = table_tree.xpath('//*[@class = "wikitable sortable"][1]//th')
Main_Heading_list =[]
for mh in Main_Heading:
     Main_Heading_list.append((mh.text).replace("\n"," "))

item = []

Book = table_tree.xpath('//*[@class = "wikitable sortable"][1]//i[1]/a[1]')
for bl in Book:
    item.append((bl.text).replace("\n"," "))
Author = table_tree.xpath('//*[@class = "wikitable sortable"][1]//td[2]/a[1]')
for auth in Author:
     item.append((auth.text).replace("\n"," "))
Language = table_tree.xpath('//*[@class = "wikitable sortable"][1]//td[3]')
for lan in Language:
     item.append((lan.text).replace("\n"," "))
Published = table_tree.xpath('//*[@class = "wikitable sortable"][1]//td[4]')
for pub in Published:
    item.append((pub.text).replace("\n"," "))
Sales = table_tree.xpath('//*[@class = "wikitable sortable"][1]//td[5]')
for sal in Sales:
    item.append((sal.text).replace("\n"," "))
genre = table_tree.xpath('//*[@class = "wikitable sortable"][1]//td[6]/a[1]')
for gen in genre:
    item.append((gen.text).replace("\n"," "))
          
n = 6
rows = [item [v:v+n] for v in range(0,len(item),n)]
rows.insert(0,Main_Heading_list)

#Drawing the table
print(tabulate(rows,headers = 'firstrow',tablefmt='fancy_grid'))
