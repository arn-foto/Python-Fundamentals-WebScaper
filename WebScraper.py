#BeautifulSoup is a used to pull out data from HTML and XML files.
from bs4 import BeautifulSoup
#This import makes a get request to a web page.
import requests
# Creates a csv file with the information pulled from requests.
import csv

# open() is a built in function and has a few arguments that serve different purposes
# 'w' is used for writing but it creates the file first.
# In addition, we can specify if it gets handled in binary or text. "t" is text mode. 
# "b" is binary mode (e.g. images)
file = open('GatheredInfo.csv', 'w')

# The write() method writes a specified text to the file.
#"a": append - The text will be inserted at the current file stream position, default at the end of the file.
#"w": The file will be emptied before the text will be inserted at the current file stream position, default 0.
# In this case, we're saving it to our csv file with a function attached to it.
writer = csv.writer(file)

writer.writerow(['Name', 'Capital', 'Population', 'Area'])

# This is is where we are calling our import and sends a GET request to the specified url
target_page = requests.get("http://www.scrapethissite.com/pages/simple/")

# BeautifulSoup() is built into bs4 and takes 2 arguments, one for the target and the other for the format
soup = BeautifulSoup(target_page.text, 'html.parser')

# We are taking our assigned variables and going through the CSS file to grab from the tags we chose. 
name = soup.find_all('h3', attrs={"class":"country-name"})
capital = soup.find_all('span', attrs={"class":"country-capital"})
population = soup.find_all('span', attrs={"class":"country-population"})
area = soup.find_all('span', attrs={"class":"country-area"})

# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, 
# and then the second item in each passed iterator are paired together etc.
for name, capital, population, area in zip(name, capital, population, area):
    print(name.text + "-" + capital.text + "-" + population.text + "-" + area.text)
   
    writer.writerow([name.text, capital.text, population.text, area.text])
# close() does what you think it does.
file.close()