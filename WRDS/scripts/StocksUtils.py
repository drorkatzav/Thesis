"""
Utils for using the results.
"""
import Config

def find_number_for_symbol(symbol):
    f = file(Config.STOCK_NUMBERS, "rb")
    lines = f.readlines()
    f.close()

    for line in lines:
        if (symbol == line.split(',')[1].strip()):
            return int(line.split(',')[0])
    return None

def find_symbol_by_number(number):
    num = int(number)
    f = file(Config.STOCK_NUMBERS, "rb")
    lines = f.readlines()
    f.close()

    for line in lines:
        if (num == int(line.split(',')[0])):
            return line.split(',')[1].strip()
    return None

def is_stock_up(symbol):
    f = file(Config.STOCK_RESULTS_FILE, "rb")
    lines = f.readlines()
    f.close()

    for line in lines:
        if (symbol == line.split(',')[0].strip()):
            return float(line.split(',')[1]) > 0
    return None

def how_much_stock_up(symbol):
    f = file(Config.STOCK_RESULTS_FILE, "rb")
    lines = f.readlines()
    f.close()

    for line in lines:
        if (symbol == line.split(',')[0].strip()):
            return float(line.split(',')[1])
    return None
