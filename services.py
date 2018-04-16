from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from termcolor import colored
import requests
import os
import random
import click

global chrome_options
global chromedriver
global driver


def configure_headless():
	global chrome_options
	global chromedriver
	global driver

	#Initialising webbrowser with headless option to work in background
	chrome_options = Options()
	#chrome_options.add_argument("--headless")
	chrome_options.add_argument("--window-size=1920x1080")
	chrome_driver = os.getcwd() +"/chromedriver"
	#Passing location of the chromedriver executable
	driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)


def stackoverflow(question):
	configure_headless()
	global chrome_options
	global chromedriver
	global driver

	#opening stackoverflow in the headless chrome browser
	driver.get("https://stackoverflow.com/")

	#location search box using the Xpath (XML Path)
	search = driver.find_element_by_xpath("/html/body/header/div/form/input")
	search.send_keys(question)
	#writing queries to the search box using send_keys
	search_button = driver.find_element_by_xpath("/html/body/header/div/form/button")
	search_button.click()
	#Simulating click on the seach button on the page

	return driver.current_url
	#Returning the url of the page after initiating click

def display_answers(questions, answers):
	index = 0
	#Picking elements from the question and answers list using the index
	for index in range(0, len(questions)):
		#Priting the question on index
		click.echo(colored(questions[index].text.replace("  ",""), 'red'))

		link = questions[index]
		for a in link.find_all('a'):
			if a.has_attr('href'):
				ans = a.attrs['href']

		#Generating clickable link on the terminal
		click.echo(colored('http://stackoverflow.com'+ans, 'green'))
		#Priting the answer on the index
		click.echo(colored(answers[index].text.replace("  ",""), 'blue'))

def kill_browser():
	#killing the webdriver processes for cleaning up the memory due to
	#unexpected network error
	driver.close()
	driver.quit()

def get_answers(question, option=''):

	url = stackoverflow(question)
	page = requests.get(url)
	data = page.text
	soup = BeautifulSoup(data,'html.parser')
	#generating the source of the page and locating Q&A section
	soup = soup.find("div", {"class":"search-results"})


	try:
		questions = soup.find_all('div', {"class":"result-link"})
		answers = soup.find_all('div', {"class":"excerpt"})
		#eaching for questions and answers using the class id's

		if option == "search":
			display_answers(questions, answers)
			
	except:
		get_answers(question, option)
		#click.echo('Network Error --> Killing Browser')

def main(question, screenshot):
	global driver
	get_answers(question, screenshot)
	filename = str(random.randint(0,1000))
	driver.get_screenshot_as_file(filename + '.png')
	#Generating screenshot and saving it with a random name
