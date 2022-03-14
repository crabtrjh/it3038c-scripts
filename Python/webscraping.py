# import module
import requests
from bs4 import BeautifulSoup
  
# link for extract html data
def getdata(url):
    r = requests.get(url)
    return r.text
  
htmldata = getdata("https://www.frontlinegaming.org/2022/03/07/tyranids-codex-announced-get-a-combat-patrol-box/")
soup = BeautifulSoup(htmldata, 'html.parser')
data = ''
for data in soup.find_all("p"):
    print(data.get_text())