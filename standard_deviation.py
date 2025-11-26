import csv
import statistics

raw_data = []
std_deviation = []
line_loop = 0

with open('std_dev_calc.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        raw_data.append(row)

for row in range(len(raw_data)):
    for data in raw_data[line_loop]:
        num_conversion = float(data)
        std_deviation.append(num_conversion)
    print(line_loop + 1)
    #print(std_deviation)
    print(statistics.stdev(std_deviation))
    std_deviation = []
    line_loop += 1

