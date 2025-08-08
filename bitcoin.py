import requests
import json
import sys
def main() :
    x = g()
    r(x)

def r(y):
    s = requests.get('https://api.coincap.io/v2/assets/bitcoin')
    r =s.json()
    f = r['data']['priceUsd']
    amount = float(f)*float(y)
    print(f"${amount:,.4f}")

def g():
    if len(sys.argv) == 2 :
        try :
            if float(sys.argv[1]):
                return sys.argv[1]
        except ValueError :
            print('Command-line argument is not a number')
            sys.exit
    else :
        print('Missing command-line argument')
        sys.exit

if __name__ == '__main__' :
    main()
