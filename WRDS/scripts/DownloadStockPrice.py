import download_spreadshit_yahoo

def main(input_filename, output_folder):
	f = file(input_filename, "rb")
        lines = f.readlines()
        f.close()
	for line in lines:
		symbol = line.split(',')[1].strip()
		download_spreadshit_yahoo.download(symbol, "./%s/%s.csv" % (output_folder, symbol, ), s_day = 3, s_month = 1, s_year = 2012, e_day = 6, e_month = 2, e_year = 2012)

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print "USAGE: python DownloadStockPrice.py <input_filename> <output_folder>"
    else:
        main(sys.argv[1], sys.argv[2])
