import sys
import csv
from tabulate import tabulate
def main():
    f = get_file()
    with open(f) as file :
        r = csv.DictReader(file)
        print(tabulate(r, headers="keys", tablefmt="grid"))

def  get_file():
    try :
        f = sys.argv[1]
    except IndexError :
        sys.exit('Too few command-line arguments')
    if len(sys.argv) == 2 :
        if '.csv' in f :
            return f
        else :
            sys.exit('Not a CSV file')
    else :
        sys.exit('Too many command-line arguments')

if __name__ == '__main__' :
    main()
