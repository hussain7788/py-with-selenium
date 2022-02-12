import csv
# write the number of records in csv file
with open('mycsv.csv', 'w', newline='') as f:
    wr = csv.writer(f)
    wr.writerow(['col1', 'col2', 'col3'])
    wr.writerow(['one', 'two', 'three'])
    print("data added")


# read all records from csv file
with open("mycsv.csv", 'r') as f:
    r = csv.reader(f)

    # reading data adding into another csv file
    with open("csv1.csv", "w", newline='') as c:
        w = csv.writer(c)
        w.writerow(['new_col1', 'new_col2', 'new_col3'])
        for index, i in enumerate(r):
            w.writerow(i)

with open("C:/Users/Admin/Desktop/mycsv.csv", 'w', newline='') as f:
    wr = csv.writer(f)
    wr.writerow(['name', 'age'])
    wr.writerow(['hussain', '23'])
    print("csv file added")


with open("C:/Users/Admin/Desktop/mycsv.csv", 'r') as f:
    re = csv.reader(f)

    for i in re:
        print(i[0])

with open("file1.txt", 'w', newline='') as file1:
    file1.writelines("my name is hussain")
    file1.writelines("my name is valli")

    file1.close()
    print("file1 added")

with open("file1.txt", 'r') as file2:
    read = file2.read()
    print(read)
