from random import randint
while True :
    try :
        i = int(input('level: '))
        if i > 0 :
            break
    except:
        pass
x = randint(1,i)
while True :
    try :
        g = int(input('Guess: '))
        if g > 0 :
            if g < x :
                print('Too small!')
            elif g > x :
                print('Too large!')
            else :
                print('Just right!')
                break
    except :
        pass



