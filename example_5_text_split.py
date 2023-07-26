row=[]

with open("sample.log") as file:
    for line in file:
        row=line.rstrip().split(" ") 
        if len(row)>4:
            print(row[3]+" "+row[0])

