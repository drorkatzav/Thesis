def main(input_filename, output_filename):
    f = file(input_filename, "rb")
    lines = f.readlines()
    f.close()
    try:
        column_number = lines[0].split(',').index('TICKER')
    except:
        print "Bad input file %s" % (input_filename, )
    ticker = lines[1].split(',')[column_number]
    number = lines[1].split(',')[0]
    f = file(output_filename, "ab")
    f.write("%s, %s\n" % (number, ticker))
    f.close()

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print "USAGE: python NumberToName.py <csv input filename> <csv output filename>"
    else:
        main(sys.argv[1], sys.argv[2])
