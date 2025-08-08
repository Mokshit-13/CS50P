import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    rex = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    match = re.search(r"^" + rex + " to " + rex + "$", s)
    if match:
        t1 = format(match.group(1), match.group(2), match.group(3))
        t2 = format(match.group(4), match.group(5), match.group(6))
        return f"{t1} to {t2}"
    else:
        raise ValueError

def format(hr, min, a):
    if hr == "12":
        if a == "AM":
            h = "00"
        else:
            h = "12"
    else:
        if a == "AM":
            h = f"{int(hr):02}"
        else:
            h = f"{int(hr)+12}"
    if min == None:
        m = "00"
    else:
        m = f"{int(min):02}"
    return f"{h}:{m}"


if __name__ == "__main__":
    main()

