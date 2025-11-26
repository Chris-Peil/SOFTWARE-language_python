import csv

csv_one = 'MC1_MB-0-1-5 MSC.csv'
csv_two = 'MC1_MB-0-1-5 ATR_mod.csv'

with open(csv_one, 'r') as t1, open(csv_two, 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

t1.close()
t2.close()

with open ('comparison.csv', 'w') as outFile:
    for line in fileone:
        if line not in filetwo:
            outFile.write(line)
