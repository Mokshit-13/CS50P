msg = input('What is the Answer to the Great Question of Life, the Universe, and Everything?: ')

if msg.strip() == '42':
    print('yes')
elif msg == 'forty-two' or msg =='forty two' or msg =='FoRty TwO':
    print('yes')
elif msg == 'Forty two':
    print('yes')
else:
    print('no')

