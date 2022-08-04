import csv
import re
import time
r = input("Enter the regex syntax you want to find: ")

start_time = time.time()
rows = []
with open("txns2.csv",'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row[0])

count = 0
for i in rows:
    if bool(re.search(r,i)):
        #print(i)
        print(count)

print(count)
print(time.time()-start_time)