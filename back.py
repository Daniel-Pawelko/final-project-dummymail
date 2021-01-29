import csv

with open('temp.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)
    for line in csv_reader:
        print(line[2])
        
