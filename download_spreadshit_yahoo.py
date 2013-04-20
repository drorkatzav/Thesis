"""
Date: 26/09/2012
Author: Dror Katzav
Purpuse: This will download a csv of hisotric quotes of nyse stocks.
"""
import urllib

def download_file(url, output_file_path):
	"""
	This function will download a url and save it to file names output_file_path
	"""
	try:
		data = urllib.urlopen(url).read()
	except Exception, e:
		print "--> Error with url %s" %(url, )
		raise e
	try:
		f = file(output_file_path, "wb")
		f.write(data)
		f.close()
	except Exception, e:
		print "--> Error with the file name %s" %(output_file_path, )
		raise e
	return 0

def create_url(name, s_day, s_month, s_year, e_day, e_month, e_year):
	"""
	This function will get the dates and name and create the url line of getting the relevant csv.
	"""
	#http://ichart.finance.yahoo.com/table.csv?s=AAPL&a=00&b=1&c=2009&d=00&e=1&f=2012&g=d&ignore=.csv
	start_day = str(s_day-1).zfill(2)
	end_day = str(e_day-1).zfill(2)
	url = "http://ichart.finance.yahoo.com/table.csv?s=%s&a=%s&b=%s&c=%s&d=%s&e=%s&f=%s&g=d&ignore=.csv" % \
			(name, start_day, s_month, s_year, end_day, e_month, e_year)
	return url
	
def download(stock_name, output_file, s_day = 1, s_month = 1, s_year = 2011, e_day = 1, e_month = 1, e_year = 2012):
	"""
	This will get the stock name, create the url , download the file and save it into a csv file.
	"""
	url = create_url(stock_name, s_day, s_month, s_year, e_day, e_month, e_year)
	if (0 == download_file(url, output_file)):
		print "Downloaded %s Successfuly!" % (stock_name,)
		return
	return 1

if __name__ == "__main__":
	import sys
	if len(sys.argv) < 2:
		print "USAGE: download_spreadshit_yahoo.py <stock name> <output filename> [<start date> <end date>]"
	else:
		download(*sys.args)
