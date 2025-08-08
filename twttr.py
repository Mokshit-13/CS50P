def shorten(t):
    l = ['A','E','I','O','U','a','e','i','o','u']
    x = ''
    for i in t :
        if i not in l :
            x +=i
    return x
def main():
    txt = input('input: ')
    y = shorten(txt)
    print(y)

if __name__ == '__main__' :
    main()
