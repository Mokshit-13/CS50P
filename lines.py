import sys
def main():
    f = get_file()
    try:
        with open(f) as file :
            count = 0
            for line in file:
                if not line.lstrip().startswith("#") and line.lstrip() != "":
                    count += 1
        print(count)
    except :
        raise FileNotFoundError


def  get_file():
    try :
        f = sys.argv[1]
    except IndexError :
        sys.exit('Too few command-line arguments')
    if len(sys.argv) == 2 :
        if '.py' in f :
            return f
        else :
            sys.exit('Not a Python file')
    else :
        sys.exit('Too many command-line arguments')


if __name__ == '__main__' :
    main()

