import csv
import sys
import datetime
filename = sys.argv[1]
reader = csv.reader(open(filename))
for row in reader:
    time = row[0]
    date = row[1]
    rain = row[2]
    dt = datetime.datetime.strptime(time + "," + date, "%H:%M,%m/%d/%Y")
    dt = int((dt - datetime.datetime(1970, 1, 1)).total_seconds())
    with open(filename+"unix.csv", 'a') as f:
        f.write(str(dt)+","+rain+"\n")
