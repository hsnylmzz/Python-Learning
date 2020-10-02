"""
Usage:
	boxOfficeRequest [-dow]
Options:
	-d 		All time domestic box-office
	-o 		All time worldwide box-office
	-w		Weekend box-office
"""

import requests
import time
from bs4 import BeautifulSoup
from docopt import docopt
from prettytable import PrettyTable

#This is the function to generate all time domestic box office chart
def domestic():
	#Get url address of boxofficemojo.com
	res = requests.get('http://www.boxofficemojo.com/alltime/domestic.htm')
	soup = BeautifulSoup(res.text, 'lxml')
	#Get movie details by resolving html tags from soup object
	movieInfo = soup.select('div[id=body] > table > tr > td > center > table > tr > td > table > tr > td > font')

	"""
	#1 Rank
	#2 Title
	#3 Studio
	#4 Lifetime gross
	#5 Year
	"""	
	title = []
	domesticGross = []
	year = []
	rank = []
	#For each time getting movie data, we first delete all rows in table
    #cur.execute('DELETE FROM domestic')

	#Append movie detials into created array
	for i in movieInfo:
		if movieInfo.index(i)%5 is 0:
			rank.append(i.get_text())
		elif movieInfo.index(i)%5 is 1:
			title.append(i.get_text())
		elif movieInfo.index(i)%5 is 3:
			domesticGross.append(i.get_text())
		elif movieInfo.index(i)%5 is 4:
			year.append(i.get_text())

	#Create table with field name
	ptable = PrettyTable(["Rank", "Movie Name", "Domestic Gross", "Year"])
	#Iterate each movie item and add to the table
	for i in range(1,101):
		ptable.add_row([rank[i],title[i],domesticGross[i],year[i]])

	print(ptable)

#This is the function to generate all time worldwide box office chart
def worldwide():
	res = requests.get('http://www.boxofficemojo.com/alltime/world/')
	soup = BeautifulSoup(res.text, 'lxml')
	movieInfo = soup.select('div[id=body] > table > tr > td > table > tr > td > font')
	"""
	#1 Rank
	#2 Title
	#3 Studio
	#4 Worldwide
	#5 Domestic
	#6 Domestic%
	#7 Overseas
	#8 Overseas%
	#9 Year 
	"""	
	rank = []
	title = []
	worldwidegross = []
	year = []

	for i in movieInfo:
		if movieInfo.index(i)%9 is 0:
			rank.append(i.get_text())
		elif movieInfo.index(i)%9 is 1:
			title.append(i.get_text())
		elif movieInfo.index(i)%9 is 3:
			worldwidegross.append(i.get_text())
		elif movieInfo.index(i)%9 is 8:
			year.append(i.get_text())
	
	#Create table with field name
	ptable = PrettyTable(["Rank", "Movie Name", "Worldwide Gross", "Year"])
	#Iterate each movie item and add to the table
	for i in range(1,101):
		ptable.add_row([rank[i],title[i],worldwidegross[i],year[i]])
	print(ptable)

#This is the function to generate weekend box office chart
def weekend():
	#Get most recent week number
	weekNumber = int(time.strftime("%W")) - 1
	#year parameter
	year = 2018

	url = 'http://www.boxofficemojo.com/weekend/chart/?yr={}&wknd={}&p=.htm'.format(year, weekNumber)
	res = requests.get(url)
	soup = BeautifulSoup(res.text, 'lxml')
	movie_info = soup.select('div[id=body] > table > tr > td > table > tr > td > font')

	title = []
	weekendgross = []
	totalgross = []

	for i in movie_info:
		if movie_info.index(i) % 12 == 2: #title
			title.append(i.get_text())
		if movie_info.index(i) % 12 == 4: #weekend gross
 			weekendgross.append(i.get_text())
		if movie_info.index(i) % 12 == 9: #total gross
			totalgross.append(i.get_text())

	ptable = PrettyTable(["Title", "Weekend Gross", "Total Gross"])
	for i in range(1,21):
		ptable.add_row([title[i], weekendgross[i], totalgross[i]])
	print(ptable)

def main():
	arguments = docopt(__doc__)
	#Get arguments information and call method based on argument
	if arguments['-d'] is True:
		domestic()
	elif arguments['-o'] is True:
		worldwide()
	elif arguments['-w'] is True:
		weekend()

if __name__ == "__main__":	
	main()