def main():
    m = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
     ]
    while True:
            d = input('Date: ').strip().replace('""', '')
            if '/' in d:
                x, y, z = d.split('/')
                if x not in m and z != 1912:
                    if 1 <= int(x) <= 31 and 1 <= int(y) <= 12:
                        print(f'{z}-{x.zfill(2)}-{y.zfill(2)}')
                        break
            elif ',' in d:
                a , b = d.split(',')
                c , d = a.split(' ')
                e = m.index(c)+1
                if c in m:
                    if 1 <= int(e) <= 31 and 1 <= int(d) <= 12:
                        print(f'{b}-{str(e).zfill(2)}-{d.zfill(2)}')
                        break


main()
