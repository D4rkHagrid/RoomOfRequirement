import click
import subprocess

from pyfiglet import Figlet
from PyInquirer import prompt

from os import listdir, getcwd
from os.path import isfile, join

@click.command()
def main():
	# show Figlet
	fig = Figlet(font='chunky')
	print(fig.renderText('Gobuster'))
	
	wordlists = [fil for fil in listdir('/usr/share/wordlists/dirbuster/') if isfile(join('/usr/share/wordlists/dirbuster/', fil))]
	
	WordlistSelection = [{
		'type': 'list',
		'name': 'WordlistSelection',
		'message': 'Which wordlist do you wanna use?',
		'choices': wordlists
	}]
	
	WebsiteInput = [{
		'type': 'input',
		'name': 'WebsiteInput',
		'message': 'Enter website to scan:'
	}]

	### Start All Questions
	websiteObject = prompt(WebsiteInput)
	wordlistObject = prompt(WordlistSelection)
	
	### parse Selections to the right strings
	# Wordlist
	wordlist = '-w ' + join('/usr/share/wordlists/', wordlistObject['WordlistSelection']) + ' '
	
	# Website
	website = '-u ' + websiteObject['WebsiteInput'] + ' '
		
	# Assemble nmap command
	gobusterString = 'gobuster -e ' + website + wordlist
	
	click.echo(gobusterString)

	process = subprocess.call(gobusterString, shell=True)

if __name__ == '__main__':
    main()
    
    
