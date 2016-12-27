
from bs4 import BeautifulSoup
import pynotify
import requests

url = "http://www.sonyliv.com/details/episodes/5082122953001/Ep.33--The-Kapil-Sharma-Show---Rustom-in-Kapil's-Mohalla"
res = requests.get(url)
soup = BeautifulSoup(res.text,'lxml')
print res.text

