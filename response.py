import validators

def main():
    print(validate(input("What's your email address: ")))

def validate(g):
    if validators.email(g) == True :
        return f'Valid'
    else :
        return f'Invalid'

if __name__ == '__main__' :
    main()
