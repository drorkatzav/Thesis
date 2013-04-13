"""
This will create for each csv from WRDS a csv
containing max, min, avg, for each value from:
PRIMEXCH,TRDSTAT,DCLRDT,DLAMT,DLPDT,DLSTCD,NEXTDT,PAYDT,RCRDDT,SHRFLG,DISTCD,DIVAMT,FACPR,FACSHR,ACPERM,ACCOMP,NWPERM,DLRETX,DLPRC,DLRET,TRTSCD,NMSIND,MMCNT,NSDINX,BIDLO,ASKHI,PRC,VOL,RET,BID,ASK,SHROUT,CFACPR,CFACSHR,OPENPRC,NUMTRD,RETX,vwretd,vwretx,ewretd,ewretx,sprtrn
This will also hold the date for each value.
"""
import sys
import Config

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def main(csv_filename):
    print csv_filename
    f = file(csv_filename, "rb")    
    data = f.read()
    f.close()
    lines = data.splitlines()
    output = [{'min' : [None, None], 'max' : [None, None], 'sum' : 0, 'count' : 0,} for i in range(272)]              
    for line in lines[1:]:
        values = line.split(',')
        for index, value in enumerate(values[5:]):
            if (None == output[index]['min'][0]) or (value < output[index]['min'][0]):
                output[index]['min'][0] = value
                output[index]['min'][1] = values[1] #set date
            if (None == output[index]['max'][0]) or (value > output[index]['max'][0]):
                output[index]['max'][0] = value
                output[index]['max'][1] = values[1] #set date                
            if is_number(value):
                output[index]['sum'] += float(value)
                output[index]['count'] += 1
    output_string = ""
    output_values = ""
    headers = Config.HEADER.split(',')
    for index, header in enumerate(headers):
        output_string += "%s max, %s max date, %s min, %s min date, %s avg, %s count," % (header, header, header, header, header, header)
        if output[index]['count'] != 0:
            output_values += "%s, %s, %s, %s, %s, %s," % (output[index]['max'][0], output[index]['max'][1],
                                                        output[index]['min'][0], output[index]['min'][1],
                                                        output[index]['sum']/output[index]['count'], output[index]['count'])
        else:
            output_values += "%s, %s, %s, %s, %s, %s," % (output[index]['max'][0], output[index]['max'][1],
                                                        output[index]['min'][0], output[index]['min'][1],
                                                        0, 0)
    f = file(Config.OUTPUT_DIR % (values[0], ), "wb")
    f.write("%s\n" % (output_string, ))
    f.write(output_values)
    f.close()
    print "Done %s" % (values[0], )
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "USAGE: python FindMax.py <csv file>"
    else:
        main(sys.argv[1])
    
