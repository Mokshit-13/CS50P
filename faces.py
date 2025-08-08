def main():
    txt = input()
    res = convert(txt)
    print(res)
def convert(txt):
    txt1=txt.replace( ":)",'🙂')
    txt2=txt1.replace( ":(",'🙁')
    return txt2

main()
