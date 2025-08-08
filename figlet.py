import sys
from pyfiglet import figlet_format
if sys.argv[1] == 'test' or sys.argv[1] == '--front' or sys.argv[1] == '--font':
    sys.exit('Invalid usage')
s = input('Input: ')
l = ['slant','rectangles','alphabet']

if len(sys.argv) < 3:
    x = figlet_format(s)
    print(x)

if len(sys.argv) == 3 :
    if sys.argv[2] in l :
        x = figlet_format( s , font = sys.argv[2] )
        print(x)
    else:
        sys.exit('Invalid usage')



