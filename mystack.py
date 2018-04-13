import click
from bs4 import BeautifulSoup
import re
import requests
r = requests.get("http://stackoverflow.com/search?q=hello")
soup = BeautifulSoup(r.text, 'html.parser')
def cli():
	#s = soup.find("div", attrs={'class':'qwidget-dollar'})
	s = soup.findAll('a', attrs={'href': re.compile("^https://")})
	#s = soup.findAll('a')
	for link in s:
		click.echo(link.get('href'))
