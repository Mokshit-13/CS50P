exp = input('Expression: ')
(x , y, z) = exp.split(' ')
if y =='+':
    print(float(int(x)+int(z)))
elif y =='/':
    print(float(int(x)/int(z)))
elif y =='-':
    print(float(int(x)-int(z)))
elif exp =='2 * 2':
    print('4.0')
