#!/usr/bin/python
from options import getCommandLineOptions
import readline
import code
import os
import logging
import subprocess

class Job:
	def __init__(self, pop, host, command):
		self.pop = pop
		self.host = host
		self.command = command
		self.args = args
		self.pid = pop.pid

	def poll():
		return pop.poll()

	def wait():
		return pop.wait()

	def kill():
		return pop.kill()


def close(savefile=""):
	save(savefile)
	exit()

def save(savefile=""):
	return True

def openjob(host, command, args=[]):
	for a in args:
		command+=" "+a
	print "lol"
	return Job(subprocess.Popen(["ssh","-o","StrictHostKeyChecking=no","%s" % host+"", command],
		shell=False,
		stdin=None,
		stdout=open('stdout.log', 'w'),
		stderr=open('stdout.log', 'w')), host, command)

def parsecommand(command):
	command = command[command.find('('):]
	command = command.replace('(','')
	command = command.replace(')','')
	print command
	return [x.strip() for x in command.split(',')]

parser = getCommandLineOptions()
opts, args = parser.parse_args()

command = ""
jobs = []

while command.find("exit") < 0:
	command = raw_input(os.getcwd()+' $> ')
	if command.find("openjob") > -1:
		com = parsecommand(command)
		if len(com)	< 2:
			print "COULD NOT PARSE COMMAND!"
		else:
			jobs.append(openjob(com[0],com[1],com[2:]))
	elif command.find("show") > -1:
		for j in jobs:
			print j.host
			print j.pop.poll()
	elif command.find("cd") > -1:
		command.replace('cd','')
		os.chdir(command)
	else:
		try:
			os.system(command)
		except:
			print "COULD NOT PARSE COMMAND!"