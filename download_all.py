"""
Date: 01/10/2012
Author: Dror Katzav
Purpuse: This will download the data for all the companies in the text file NYSE.txt.
			That file should contain all the nyse symbols.
"""
import re

import download_spreadshit_yahoo

FILENAME = "NYSE.txt"
def main():
	f = file(FILENAME, "rb")
	symbol_re = re.compile("([A-Z.-]+)\t[\w]+")
	lines = f.readlines()
	for line in lines:
		symbol = re.findall(symbol_re, line)[0]
		download_spreadshit_yahoo.download(symbol, "%s.csv" % (symbol, ))
	f.close()
	
if __name__ == "__main__":
	main()