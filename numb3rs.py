import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if match := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip) :
        for x in range(1,5) :
            if int(match.group(x)) > 255 or int(match.group(x)) < 0 :
                return False
        return True
    else :
        return False



if __name__ == "__main__":
    main()
