import sys
import csv

s = []

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 3:
    try:
        with open(sys.argv[1], "r") as rfile, open(sys.argv[2], "w") as wfile:
            r = csv.DictReader(rfile)
            for row in r:
                splited = row["name"].split(",")
                s.append({
                    "first": splited[1].lstrip(),
                    "last": splited[0],
                    "house": row["house"
                    ]})
            writer = csv.DictWriter(wfile, fieldnames=["first", "last", "house"])
            writer.writerow({
                "first": "first",
                "last": "last",
                "house": "house"
            })
            for row in s:
                writer.writerow({
                    "first": row["first"],
                    "last": row["last"],
                    "house": row["house"]
                })

    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")
