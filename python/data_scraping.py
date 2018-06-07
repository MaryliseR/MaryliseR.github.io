# Importing the necessary packages
from bs4 import BeautifulSoup
from urllib import request

# Data to be scraped found at:
url = "https://github.com/humanitiesprogramming/scraping-corpus"

print(url)
print(url + "/subdomain")

# Scrape the url of the page
html = request.urlopen(url).read()
#print(html[0:2000])

# Turning the HTML code into something BeautifulSoup can work with -> turn the
# HTML into a BS object
soup = BeautifulSoup(html, 'lxml')

# To get the links
#print(soup.find_all('a')[0:10])

# To get the text
#print(soup.text[0:2000])
# Outputs all the HTML stripped out in a long string

# Here is a slightly prettier version that strips out all the '\n' characters
# (those are a just a way for Python to note that there should be a line break
# at that point in the string)
#print(soup.text.replace('\n', ' ')[0:1000])

# "first get me only the HTML for the links on this page. Then give me the text
# for just these smaller chunks.
# print(soup.find_all('a').text)
# gives an error message

# To see what's going on, the following line will tell us what kind of object we're looking at:
print(type(soup.find_all('a')).__name__)
# We're looking at a ResultSet. Not a BeautifulSoup object.
# a results set gives us a list of Tag objects, but those still respond to a lot of the same
# things as BeautifulSoup objects
print(type(soup.find_all('a')[0]).__name__)
print(soup.find_all('a')[0].text)

# How many links on this page?
print(len(soup.find_all('a')))
