END = "2012-06-01"
START = "2012-03-01"

def main(input_filename, output_filename):
    try:
	f = file(input_filename, "rb")
        lines = f.readlines()
        f.close()
	date_column = lines[0].split(',').index('Date')
        open_column = lines[0].split(',').index('Open')
        if (date_column < 0) or (open_column < 0):
            print "%s was not a good input file" % (input_filename,)
        dates = {}
        for line in lines[1:]:
            dates[line.split(',')[date_column]] = line.split(',')[open_column]
        start = float(dates[START])
        end = float(dates[END])
        ratio = ((end - start) / start) * 100
        f = file(output_filename, "ab")
        name = input_filename[2:-4]
        f.write("%s, %s\n" % (name, ratio))
        f.close()
    except Exception, e:
        print "Error on file %s" % (input_filename, )
        raise e

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print "USAGE: python CalculateResults.py <input_filename> <output_filename>"
    else:
        main(sys.argv[1], sys.argv[2])
