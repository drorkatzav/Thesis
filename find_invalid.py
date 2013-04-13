"""
Date: 05/10/2012
Author: Dror Katzav
Purpuse: This will find the invalid printouts in the input_file
"""
import sys

def find_invalid(input_filename, output_filename):
	f = file(input_filename, "rb")
	lines = f.readlines()
	f.close()
	output = file(output_filename, "wb")
	for line in lines:
		if 'not valid' in line:
			output.write(line)
	output.close()
	
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "USAGE: python find_invalid.py <input_filename> <output_filename>"
	else:
		find_invalid(sys.argv[1], sys.argv[2])