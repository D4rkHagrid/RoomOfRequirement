import click

from pyfiglet import Figlet
from PyInquirer import prompt

@click.command()
def main():
	# show Figlet
	fig = Figlet(font='chunky')
	print(fig.renderText('Metasploit'))
	print(fig.renderText('Cheat Sheet'))
	
	click.echo('')

if __name__ == '__main__':
    main()
    
