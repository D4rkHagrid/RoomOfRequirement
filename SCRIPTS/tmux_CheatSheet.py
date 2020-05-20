import click
import pyperclip as pc

from pyfiglet import Figlet
from PyInquirer import prompt, Separator


@click.command()
def main():
	# show Figlet
	fig = Figlet(font='slant')
	print(fig.renderText('TMUX - Cheat Sheet'))

	# Cheat Sheet
	TMUXCheatSheet = [{
		'type': 'list',
		'name': 'TMUX_Cheat_Sheet',
		'message': 'Copy Command:',
		'choices': [
			Separator(),
			{'name': " ", 'disabled': 'SESSIONS'},
			Separator(),
			"tmux                                        # start session",
			"tmux ls                                     # list sessions",
			"tmux new -s <SessionName>                   # start session with name",
			"tmux attach -t <SessionName>                # attach to a session",
			"tmux kill-session -t <SessionName>          # kill a specific session",
			"tmux kill-server                            # kill all sessions",
			"exit                                        # exit current session",
			"<prefix> + d                                # detach current session",
			"<prefix> + $                                # change session numbering",
			Separator(),
			{'name': " ", 'disabled': 'WINDOWS'},
			Separator(),
			"<prefix> + C                                # create window",
			"<prefix> + ,                                # change window name",
			"<prefix> + &                                # kill current window",
			Separator(),
			{'name': " ", 'disabled': 'SPLIT PANES'},
			Separator(),
			"<prefix> + \"                                # split into top/bottom",
			"<prefix> + %                                # split into left/right",
			"<prefix> + x                                # kill current pane",
			"<prefix> + <arrow-keys>                     # switch between panes",
			Separator(),
		]
	}]

	# Print the sheet
	selected = prompt(TMUXCheatSheet)

	# extract command from selected String
	command = selected["TMUX_Cheat_Sheet"].split("#")[0].rstrip()

	# use pyperclip to copy to clipboard
	pc.copy(command)
	
	click.echo(command)

if __name__ == '__main__':
    main()