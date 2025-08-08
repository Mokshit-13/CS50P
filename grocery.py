lst = []
cst = {}


while True:
     try:
         x = input().upper()
         lst. append(x)
     except EOFError:
         print('')
         for i in lst:
             if not i in cst:
                 cst[i] = 1
             else:
                 cst[i] += 1
         for key, value in sorted(cst.items ()):
            print(value, key)
         exit()

