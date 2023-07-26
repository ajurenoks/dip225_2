# input information from keyboar and save it to list

names =[]     
# ask to enter 3 names in loop
for _ in range(3):
    name=input("What is your name? ")
    names.append(name)

# output sortet information in terminal

for name in sorted(names):
    print(f"hello, {name}")

# for more information about sorted list read using Python documentation https://docs.python.org/3/howto/sorting.html 
