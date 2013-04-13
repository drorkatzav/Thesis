"""
Date: 05/10/2012
Author: Dror Katzav
Purpuse: This will find the min and max for every colomn in the portfolio.
"""
import os.path
import sys

def find_min_max(output_filename, input_path, input_stockname):
	input_filename = os.path.join(input_path, "%s.csv" % (input_stockname, ))
	f = file(input_filename, "rb")
	lines = f.readlines()
	f.close()
        #OPEN, HIGH, LOW, CLOSE, VOLUME, ADJ CLOSE.
	max_list = [[0, '1900-01-01'], [0, '1900-01-01'], [0, '1900-01-01'], [0, '1900-01-01'], [0, '1900-01-01'], [0, '1900-01-01']]
	min_list = [[0, '1900-01-01'], [0, '1900-01-01'], [0, '1900-01-01'], [0, '1900-01-01'], [0, '1900-01-01'], [0, '1900-01-01']]
	for line in lines[1:]: #first line has only headers.
		data = line.strip().split(',')
		date = data[0]
		data = data[1:]
		for i in range(len(data)):
			if max_list[i][0] < float(data[i]) or 0 == max_list[i][0]:
				max_list[i][0] = float(data[i])
				max_list[i][1] = date
			if min_list[i][0] > float(data[i]) or 0 == min_list[i][0]:
				min_list[i][0] = float(data[i])
				min_list[i][1] = date	
	output = file(output_filename, "ab")
	output_strings = ["%s,%s" % (data[0], data[1]) for data in max_list + min_list]
	output.write(",".join([input_stockname] + output_strings) + '\n')
	output.close()
	
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "USAGE: python find_min_max.py <output_filename> <input_path> <input_stock_name>"
                print "  The output file will contain data for the stock. input_path is the .csv path."
                print "  Make sure that the .csv is named with the stock name."
	else:
		try:
			find_min_max(sys.argv[1], sys.argv[2], sys.argv[3])
		except:
			print "%s is not valid!" % (sys.argv[3], )
