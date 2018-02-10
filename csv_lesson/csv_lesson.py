""" This script contains lessons for CSV module"""
import csv

# reading a csv and writing the data into a new csv file
with open('mock_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv', 'w')  as new_file:
        csv_writer = csv.writer(new_file,delimiter="\t")

        for line in csv_reader:
            csv_writer.writerow(line)


""" Reading a file with a delimiter of tab """
with open('new_names.csv', 'r')  as csv_file:
    csv_reader = csv.reader(csv_file, delimiter="\t")

    for line in csv_reader:
        print(line)