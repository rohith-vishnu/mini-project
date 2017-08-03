import urllib.request
from bs4 import BeautifulSoup
file=open("URLS.txt","r")

websites=file.readlines()
for website in websites
    page=urllib.request.urlopen(website)

#print(page.read())
soup=BeautifulSoup(page.read(),"html.parser")

for p in soup.find_all('p'):
    print (p.text)