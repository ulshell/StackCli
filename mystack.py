import click
from services import *
@click.command()
@click.option('--search', default='', help='Type your query(text)')
def cli(search):
	if search:
		get_answers(search)
@click.command()
@click.option('--screenshot', default='', help='Take a screenshot')
def cli(screenshot):
	if screenshot:
		main(screenshot, 'screenshot')
