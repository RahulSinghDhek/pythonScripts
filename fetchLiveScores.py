#!/usr/bin/python
from bs4 import BeautifulSoup
import pynotify
import requests

def sendAlert(title,message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return

url = "http://static.cricinfo.com/rss/livescores.xml"
res = requests.get(url)
soup = BeautifulSoup(res.text,'lxml')
scoreData = soup.find_all("description")
scoreCard = ""
for i in range(1,len(scoreData)):
    scoreCard=scoreCard + scoreData[i].text + "\n"

sendAlert("Live Scores",scoreCard)

