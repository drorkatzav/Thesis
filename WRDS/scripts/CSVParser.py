import sys

def main(filename):
    f = file(filename, "rb")
    data = f.read()
    lines = data.splitlines()
    headers = lines[0]
    stock = ""
    for line in lines[1:]:
        stock_name = line.split(',')[0]
        if stock_name != stock:
            f.close()
            f = file(stock_name, "wb")
            stock = stock_name
            f.write("%s\n" % (headers, ))
        f.write("%s\n" % (line, ))
    f.close()

if __name__ == "__main__":    
    main(sys.argv[1])
