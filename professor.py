import random

def main():
        level = get_level()
        generate_integer(level)

def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level in[1,2,3]:
                return level
        except ValueError :
            pass

def generate_integer(level):
    c = 3
    s = 0
    for i in range(10):
        if level == 1 :
            x = random.randint(0,9)
            y = random.randint(0,9)
        elif level == 2 :
            x = random.randint(10,99)
            y = random.randint(10,99)
        elif level == 3 :
            x = random.randint(100,999)
            y = random.randint(100,999)
        while True :
            try :
                ans = input(f'{x} + {y} = ')
                if int(ans) == (x + y) :
                    s += 1
                    break
                elif ans!= (x + y) :
                    c -= 1
                    print('EEE')
                if c <= 0 :
                    print(f'{x} + {y} = {x + y}')
                    break
            except ValueError:
                    c -= 1
                    print('EEE')
                    if c <= 0 :
                        print(f'{x} + {y} = {x + y}')
                        break
                    pass
    else :
        print(f'Score : {s}')

if __name__ == "__main__":
    main()
