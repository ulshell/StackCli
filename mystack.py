import click
from services import *

@click.command()
@click.option('--screenshot', default='', help='Take a screenshot of query answer')
@click.option('--search', default='', help='Type your query(text)')
@click.option('--seekn', nargs=3, type=click.Tuple([str, int, str]), default='', help='Type your query(text) with position of answer to search within')
def cli(screenshot, search, seekn):
	if screenshot:
		main(screenshot, 'screenshot')

	elif search:
		get_answers(search, 'search')

	elif seekn:
		if len(seekn) == 3:
			nth_answer(n=seekn[1], question=seekn[0], option=seekn[2])
		else:
			nth_answer(n=seekn[1], question=seekn[0])
