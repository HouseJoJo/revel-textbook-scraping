import csv

with open("table.csv", "r") as input_file:
    csv_reader = csv.reader(input_file)
    for row in csv_reader:
        line = row[1]
        if(line[:1].isdigit()):
            print("\n \n \n" + line)
        else: print("\n" + line)