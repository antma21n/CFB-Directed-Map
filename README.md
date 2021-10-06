# CFB-Directed-Map
Directed Map of the 2021 College Football Season

## What is this project?
This project is a passion project to show my use of linked list data structures and directed graphs to improve my programing skills. Additionally, this project improved my skills in webscraping and data cleaning. Finally, this is my first project put onto GitHub where I am learning to use git tools such as TortoiseGit. 

The CFB Directed Map shows all FBS college football teams in a map and connects an arrow towards who they beat and an arrow pointed at them when they are beat by a team. This map can show which team might be better than another and show interesting 'love triangles' where team A beat B, B beat C, but C also beat A. 

## How It Works
1. Scrapes win-loss data (using BeautifulSoup library for python) for every FBS college football team
2. Creates a data structure for each team for all games that team played including who they played and if the selected team won
3. Creates a directed graph (using NetworkX library for python) for all FBS team. Arrows that point toward a team means that team lost 
	- example: Alabama beat Ole Miss therefore an arrow would point from Alabama to Ole Miss

## Future Works
- Fix directed graph and make it more visually pleasing
- Update for the rest of the season and future seaons 

## Resources
- Netgraph: https://github.com/paulbrodersen/netgraph