def getCommandLineOptions():
	from optparse import OptionParser, OptionGroup

	parser = OptionParser(usage=__doc__)
	parser.add_option("--runcard", dest="runcards",action='append',
					default=[], help="Start from a (series of) runcard(s)")
	parser.add_option("--resume", dest="resume",action='append',
					default=[], help="Resume session from an output file")
	return parser