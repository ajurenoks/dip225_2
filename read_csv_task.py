# This example showcases the process of extracting information from a CSV file,
# specifically a Zoom meeting report, to automatically generate a comprehensive 
#report containing a list of unique users who participated in the Zoom meeting.

attendance=[]
date=''


with open("zoom.csv","r") as f:
    next(f)
    for line in f:
        row=line.rstrip().split(",")
        l=len(row)
        if l==8:
            if date=='':
                date=row[2]
                date=date.replace("/","-")
                date=date[0:9]
            name=row[0]
            if name not in attendance:
                attendance.append(name)


with open(date+".txt","w") as f:
    for user in sorted(attendance):
        f.write(user+"\n")            
