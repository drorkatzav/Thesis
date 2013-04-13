"""
This will append all FindMax.py csv-s to one. It will do so without the headers..
"""
import sys

def main(main_csv_filename, csv_filename):
    if "." == csv_filename:
        return
    f = file(csv_filename, "rb")
    data = f.read()
    f.close()
    lines = data.splitlines()
    stock_name = csv_filename[:-4]
    main_csv = file(main_csv_filename, "ab")
    main_csv.write("%s, %s\n" % (stock_name, lines[1], ))
    main_csv.close()
    return

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "USAGE: python AppendFiles.py <main csv file> <file to append>"
    else:
        main(sys.argv[1], sys.argv[2])
