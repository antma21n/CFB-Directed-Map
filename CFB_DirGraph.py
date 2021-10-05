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
newjson = []
gameResults = []


f = open('completedata.json')
completedata = json.load(f)
#len(completedata)

for i in range(0,8):
	temp = completedata[i]
	team = completedata[i]["team"]
	opponents = completedata[i]["opponents"]
	results = completedata[i]["results"]
	
	for j in range(0,len(opponents)):
		opponent = opponents[j]
		result = results[j]
		if (result.find('W') != -1):
			gameResults.append((team, opponent))
		if (result.find('L') != -1):
			gameResults.append((opponent, team))
	


	#print(team)
	#print(opponents)
	#print(results)
#print(gameResults)

G = nx.DiGraph()
G.add_edges_from( gameResults )


#really gross right now needs to be fixed.
pos = nx.spring_layout(G, k=0.5, iterations=50, scale = 3)
nx.draw_networkx_nodes(G, pos, node_size = 30)
nx.draw_networkx_edges(G, pos, edgelist = G.edges(), edge_color = 'black')
nx.draw_networkx_labels(G, pos, font_size = 12)
plt.show()