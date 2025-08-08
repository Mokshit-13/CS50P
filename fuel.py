def main():
    x = get_int()
    print(f"{x}")

def get_int():
     while True:
         try:
             x , y = input("Fraction: ").split("/")
             z = float((int(x)/int(y))*100)
             if int (x) <= int(y):
                 if z >= 99:
                     print("F")
                 elif z <= 1:
                     print("E")
                 else:
                     print(f"{round(float(z))}%")
                 exit()
             else:
                 return get_int()
         except (ValueError, ZeroDivisionError):
             continue
main()

