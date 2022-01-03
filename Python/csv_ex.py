import csv
### write the number of records in csv file
with open('mycsv.csv', 'w', newline='') as f:
    wr = csv.writer(f)
    wr.writerow(['col1', 'col2', 'col3'])
    wr.writerow(['one', 'two', 'three'])
    print("data added")
    
    
### read all records from csv file
with open("mycsv.csv", 'r') as f:
    r = csv.reader(f)

    ## reading data adding into another csv file
    with open("csv1.csv", "w", newline='') as c:
        w = csv.writer(c)
        w.writerow(['new_col1', 'new_col2', 'new_col3'])
        for index, i in enumerate(r):
            w.writerow(i)
            
    
