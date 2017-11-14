import csv
reader = csv.reader(open("/home/saumya/Downloads/temps_out.csv"))
for row in reader:
   final_time=""
   final_date=""
   final_field=""
   time=row[0]
   date=row[1]
   rain=row[2]

   time_split = time.split(":")
   final_time=final_time+time_split[0]+time_split[1]

   date_split = date.split("/")
   final_date=final_date+date_split[2]+date_split[1]+date_split[0]

   final_field=final_field+final_date+final_time

   with open('temps_out.csv', 'ab') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow([final_field,rain])




