"""
Date: 04/10/2012
Author: Dror Katzav
Purpuse: This will call a function for all the companies in the text file NYSE.txt.
			That file should contain all the nyse symbols.
"""
import re
from os import system
import sys

FILENAME = "NYSE.txt"

def main(command, argv):
	f = file(FILENAME, "rb")
	symbol_re = re.compile("([A-Z.-]+)\t[\w]+")
	lines = f.readlines()
	f.close()
	if [] != argv:
		command += ' ' + ' '.join(argv)
	for line in lines:
		symbol = re.findall(symbol_re, line)[0]
		system('%s %s' % (command, symbol))
		print "SYMBOL %s Successfuly done!" % (symbol, )
		
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "USAGE: python for_all_stocks_do.py <cmd command> [<extra arguments>]"
	else:
		main(sys.argv[1], sys.argv[2:])