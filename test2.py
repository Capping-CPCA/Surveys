import csv
#conn = cpcapep.connect(connection)
#cursor = conn.cursor()
csvfile = open("r2.csv","rb")

reader = csv.reader(csvfile)
for row in reader:
	#r = 0
	print(row[0]+" - "+row[1]+" - "+row[2])
	print "  "
	#Q1 = row[0]
	#Q2 = row[1]
	#Q3 = row[2]
	#r+=1
	print("INSERT INTO answers (Q1, Q2, Q3) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16]))
	#17 
	print "  "
	#cursor.execute(query, data)
	#print query
(csvfile).close
