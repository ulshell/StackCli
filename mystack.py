import click
from services import *




@click.command()
@click.option('--screenshot', default='', help='Take a screenshot')
@click.option('--search', default='', help='Type your query(text)')
def cli(screenshot, search):
	if screenshot:
		main(screenshot, 'screenshot')
	else:
		get_answers(search, 'search')
