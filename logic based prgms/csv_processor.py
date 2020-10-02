import csv

with open("example.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line)

        line["Roll_no"] = int(line.get("Roll_no"))

        print(line)