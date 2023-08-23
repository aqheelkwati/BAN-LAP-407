import csv

fields = ["Place","Food","price(per plate)","ratings(out of 10)"]

rows = [["Hyderabad","Bawarchi","200","8"],
        ["Bangalore","Bisi bele bath","100","9"],
        ["Chennai","Idly&sambar","50","9"],
        ["Mumbai","Vadapav","20","8"]
        ]

filename = "record.csv"

with open(filename,"w+" ) as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
    
    csvfile.seek(0)
    csvreader = csv.reader(csvfile)
    # print(csvreader)
    liss = list(csvreader)
    # print(liss)
    for lines in liss:
        if lines:
            # print(lines)
            print("  ".join(lines))