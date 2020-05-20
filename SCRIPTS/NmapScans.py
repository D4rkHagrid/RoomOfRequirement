import click
import subprocess

from pyfiglet import Figlet
from PyInquirer import prompt

from os import listdir, getcwd
from os.path import isfile, join

@click.command()
def main():
	# show Figlet
	fig = Figlet(font='block')
	print(fig.renderText('MY NMAP'))
	
	PortQuestions = [{
		'type': 'list',
		'name': 'PortSelection',
		'message': 'Which ports do you wanna scan?',
		'choices': ['Default 1000 Ports', '100 most common ports', 'all ports', 'custom ports']
	}]
	
	CustomPortInput = [{
		'type': 'input',
		'name': 'CustomPortInput',
		'message': 'Enter Ports (with commas or as Range): '
	}]
	
	IPAdressInput = [{
		'type': 'input',
		'name': 'IPInput',
		'message': 'Enter IP to scan:'
	}]
	
	ScanTypeSelection = [{
		'type': 'list',
		'name': 'ScanTypeSelection',
		'message': 'What scan type do you wanna proceed with?',
		'choices': ['TCP SYN scan (default)', 'TCP connect', 'UDP Ports', 'both TCP and UDP']
	}]
	
	IgnoreDiscoveryConfirmation = [{
		'type': 'confirm',
		'name': 'IgnoreDiscoveryConfirmation',
		'message': 'Ignore Discovery? (may result in slowdown)',
		'default': False,
	}]
	
	ServiceDetectionSelection = [{
		'type': 'list',
		'name': 'ServiceDetectionSelection',
		'message': 'What type of Service Detection do you wanna use?',
		'choices': ['No Service Detection', 'Standard Service Detection', 'Advanced OS and Services Detection']
	}]
	
	OutputFileFormatSelection = [{
		'type': 'list',
		'name': 'OutputFileFormatSelection',
		'message': 'What file format do you need for the output?',
		'choices': ['Default Output', 'As XML', 'grep Format', 'All Formats', 'I dont want an outputfile'],
	}]
	
	FilenameInput = [{
		'type': 'input',
		'name': 'FilenameInput',
		'message': 'Enter output file name (without extension):',
	}]


	### Start All Questions
	ipAdressObject = prompt(IPAdressInput)
	portObject = prompt(PortQuestions)
	portsStringObject = ''
	if portObject['PortSelection'] == 'custom ports':
		portsStringObject = prompt(CustomPortInput)
	scanTypeSelectionObject = prompt(ScanTypeSelection)
	ignoreDiscoveryObject = prompt(IgnoreDiscoveryConfirmation)
	serviceDetectionObject = prompt(ServiceDetectionSelection)
	outputFormatObject = prompt(OutputFileFormatSelection)
	if outputFormatObject['OutputFileFormatSelection'] != 'I dont want an outputfile':
		fileNameObject = prompt(FilenameInput)
	
	### parse Selections to the right strings
	# IP
	ip = ipAdressObject['IPInput']
	
	# Ports
	ports = ''
	portSelection = portObject['PortSelection']
	if portSelection == '100 most common ports':
		ports = '-F '
	elif portSelection == 'all ports':
		ports = '-p- '
	elif portSelection == 'custom ports':
		ports = '-p ' + portsStringObject['CustomPortInput']
	
	# Scan Type
	scanType = ''
	scanTypeSelection = scanTypeSelectionObject['ScanTypeSelection']
	if scanTypeSelection == 'TCP connect':
		scanType = '-sT '
	elif scanTypeSelection == 'TCP SYN scan (default)':
		scanType = '-sS '
	elif scanTypeSelection == 'UDP Ports':
		scanType = '-sU '
	elif scanTypeSelection == 'both TCP and UDP':
		scanType = '-sT -sU '
	
	# Ignore Discovery
	ignoreDiscovery = ''
	if ignoreDiscoveryObject['IgnoreDiscoveryConfirmation']:
		ignoreDiscovery = '-Pn ' 
		
	# Service Detection
	serviceDetection = ''
	serviceDetectionSelection = serviceDetectionObject['ServiceDetectionSelection']
	if serviceDetectionSelection == 'Standard Service Detection':
		serviceDetection = '-sV '
	elif serviceDetectionSelection == 'Advanced OS and Services Detection':
		serviceDetection = '-A '
	
	# Outputfile format
	output = ''
	outputFormatSelection = outputFormatObject['OutputFileFormatSelection']
	if outputFormatSelection == 'Default Output':
		output = '-oN ' + fileNameObject['FilenameInput'] + '.txt '
	elif outputFormatSelection == 'As XML':
		output = '-oX ' + fileNameObject['FilenameInput'] + '.xml '
	elif outputFormatSelection == 'grep Format':
		output = '-oG ' + fileNameObject['FilenameInput'] + '.txt '
	elif outputFormatSelection == 'All Formats':
		output = '-oA ' + fileNameObject['FilenameInput'] + ' '
		
	# Assemble nmap command
	nmapString = 'sudo nmap ' + scanType + ignoreDiscovery + serviceDetection + output + ports + ip
	
	click.echo(nmapString)

	process = subprocess.call(nmapString, shell=True)

if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
