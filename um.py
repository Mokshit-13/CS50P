import re


def main():
    print(count(input("Text: ")))


def count(s):
    rex = "(^|\W)um($|\W)"
    m = re.findall(rex, s, re.IGNORECASE)
    if m:
        return(len(m))





if __name__ == "__main__":
    main()
