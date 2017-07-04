import csv

with open("example.csv") as csvfile:
    read_csv = csv.reader(csvfile, delimiter=",")
    print(read_csv)
    for row in read_csv:
        print(row)
        print(row[2])
