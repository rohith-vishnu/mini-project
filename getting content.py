import urllib.request
from bs4 import BeautifulSoup

page=urllib.request.urlopen('https://www.youtube.com/')

#print(page.read())
soup=BeautifulSoup(page.read(),"html.parser")

for p in soup.find_all('p'):
    print (p.text)