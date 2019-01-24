import urllib.request
import sys
from urllib.parse import urlparse
from requests_html import HTMLSession
from collections import Counter

'''
url = 'http://web.cs.ucla.edu/classes/fall18/cs131/syllabus.html'

'''

url = "'" + sys.argv[1] + "'"

my_netloc = urlparse(url).netloc

def get_bytes():
  x = urllib.request.urlopen(url)
  byte_length = len(x.read())
  return(byte_length)

def get_links():
  session = HTMLSession()
  t = session.get(url)
  links = []

  for link in t.html.absolute_links:
    links.append(urlparse(link).netloc)

  print(links)
  unique = Counter(links)

  return (unique[my_netloc])

length = get_bytes()
counter = get_links()

print(length)
print(counter)
