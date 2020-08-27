import csv

with open("example.csv") as csv_file:
    csv_read = csv.DictReader(csv_file)

    for l in csv_read:
        print(l)

     
