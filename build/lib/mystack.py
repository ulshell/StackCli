import click
from services import *

@click.command()
@click.option('--screenshot', default='', help='Take a screenshot of query answer')
@click.option('--search', default='', help='Search your query(text)')
@click.option('--seekn', '-n', multiple=True , default='', help='Type your query(text) with position of answer to search within\n or \n -n Type your query -n question number -n screenshot to take screenshot of answer within')
def cli(screenshot, search, seekn):
	if screenshot:
		main(screenshot, 'screenshot')

	elif search:
		get_answers(search, 'search')

	#elif seekn and n:
	#	nth_answer(n=seekn[1], question=seekn[0], option='screenshot')

	elif seekn:
		if len(seekn) == 3:
			nth_answer(n=int(seekn[1]), question=seekn[0], option='screenshot')
		else:
			nth_answer(n=int(seekn[1]), question=seekn[0])
