import inflect
p = inflect.engine()
s = []
while True :
    try:
        x = str(input('Name: '))
        s.append(x)

    except EOFError:
        print()
        break

print('Adieu, adieu, to',p.join(s))
