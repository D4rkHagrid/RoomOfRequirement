import click
import subprocess

from pyfiglet import Figlet
from PyInquirer import prompt

from os import listdir, getcwd
from os.path import isfile, join, dirname

@click.command()
def main():
	# show Figlet
	fig = Figlet(font='slant')
	print(fig.renderText('RAUM'))
	print(fig.renderText('DER'))
	print(fig.renderText('WUENSCHE'))

	scriptsPath = join(dirname(__file__), 'SCRIPTS')
	scripts = [fil for fil in listdir(scriptsPath) if isfile(join(scriptsPath, fil))]

	# main menu
	menu = [{
		'type': 'list',
		'name': 'MainMenu',
		'message': 'What do you want to do?',
		'choices': [
			'Tools',
			'Cheat Sheets',
		],
	}]

	# Ask what to do
	questions = [
		{
			'type': 'list',
			'name': 'scriptSelection',
			'message': 'What do you want to do?',
			'choices': scripts
		}
	]

	menuSlection = prompt(menu)

	if menuSlection['MainMenu'] == 'Tools':
		# Check for scripts
		if len(scripts)>0:
			result = prompt(questions)
			
			fileEnding = result['scriptSelection'].split('.', 1)[1]

			# execute selected script
			sPath = join(dirname(__file__), 'SCRIPTS', result['scriptSelection'])
			click.echo(sPath)
			if fileEnding == 'py':
				commandStr = 'python3 ' + sPath
				process = subprocess.call(commandStr, shell=True)

if __name__ == '__main__':
    main()
