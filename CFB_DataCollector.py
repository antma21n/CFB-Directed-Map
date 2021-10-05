#to install a library enter following code below
#py -m pip install -U (NAME OF LIBRARY HERE)

import networkx as nx
import matplotlib.pyplot as plt

import requests
from bs4 import BeautifulSoup, SoupStrainer
from lxml import etree
import re
import json

#globals
teams = []
all_links = []
data = {}
completedata = []

page = requests.get("http://www.cfbstats.com/")
soup = BeautifulSoup(page.content, 'html.parser')
dom = etree.HTML(str(soup))
page_title = soup.title.text
print(page_title)

# Extract and store in top_items according to instructions on the left
links = soup.select('a')
for ahref in links:
    text = ahref.text
    text = text.strip() if text is not None else ''

    href = ahref.get('href')
    href = href.strip() if href is not None else ''
    all_links.append({"href": href, "text": text})
#print(all_links)
with open('links.json', 'w') as f:
    json.dump(all_links, f, indent=4)

for i in range(1,130):
	xpath = '/html/body/div/div[4]/div/ul/li[2]/ul/li[' + str(i) +']/a'
	team = dom.xpath(xpath)[0].text
	if len(team) < 12:
		teams.append(team)

#done manually rn
f = open('fixedlinks.json')
teams = json.load(f)

print(teams[0]['href'])

for i in range(1,len(teams)):
	team = teams[i]['text']
	link = teams[i]['href']

	webpage = "http://www.cfbstats.com" + link
	page = requests.get(webpage)
	soup = BeautifulSoup(page.content, 'html.parser')
	#print(soup)
	dom1 = etree.HTML(str(soup))
	page_title = soup.title.text
	print(page_title)

	opponents = soup.find_all("td", {"class": "opponent"})
	for j in range(0,len(opponents)):
		opponents[j] = opponents[j].text
		opponents[j] = ''.join([k for k in opponents[j] if not k.isdigit()])
		opponents[j] = opponents[j].replace("@","")
		opponents[j] = opponents[j].replace("+","")
		opponents[j] = opponents[j].replace(" ","")

	results = soup.find_all("td", {"class": "result"})
	for j in range(0,len(results)):
		results[j] = results[j].text
		if (results[j].find('W') != -1):
			results[j] = 'W'
		if (results[j].find('L') != -1):
			results[j] = 'L'

	data = {"team":team,
			"opponents":opponents,
			"results":results}
	completedata.append(data)

	#store opponents and results as a data frame
with open('completedata.json', 'w') as f:
    json.dump(completedata, f, indent=4)

