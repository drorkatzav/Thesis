def main(input_filename, output_filename, nyse_filename):
    f = file(input_filename, "rb")
    input_lines = f.readlines()
    f.close()
    f = file(nyse_filename, "rb")
    stocks_lines = f.readlines()
    f.close()
    nyse_stocks = [line.split('\t')[0] for line in stocks_lines]
    f = file(output_filename, "wb")
    for stock in input_lines:
        stock_name = stock.split(',')[1].strip()
        if stock_name in nyse_stocks:
            f.write("%s" % (stock,))
    f.close()
    
if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 4):
        print "USAGE: python IsNyse.py <csv input filename> <csv output filename> <NYSE stocks list>"
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
