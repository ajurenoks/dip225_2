# Work with text file in python
This are examples that are used in our classes. Video education video is available on YouTube channel https://www.youtube.com/@digitalasprasmes.

This repository is an excellent resource for anyone looking to grasp the fundamentals of text type file Input/Output (I/O) processing in Python. With a carefully curated collection of five examples, it offers an insightful and hands-on approach to working with text files, enabling users to gain a solid understanding of file handling in Python.

Whether you are a beginner aiming to explore file I/O concepts or an experienced Python developer seeking a refresher, this repository caters to all levels of expertise. Each example is thoughtfully designed to cover essential aspects of text file manipulation, allowing you to comprehend the core principles with ease.

Examples Included:
- Reading Text Files: Understand how to open, read, and close text files in Python, gaining insights into various reading modes and handling different types of data.
- Writing to Text Files: Learn how to create, write, and modify text files using Python, exploring techniques to add content and overwrite existing data.
- Text Processing: Discover methods to manipulate text data read from files, such as string operations, data cleaning, and text analysis.

**Example program**  read_csv_task.py

This Python program aims to read data from a CSV file containing a Zoom meeting report and generate a comprehensive report file. The report will contain a list of unique users who participated in the Zoom meeting, sorted alphabetically. Let's break down the code:

1. `attendance = []`: This initializes an empty list called `attendance`, which will be used to store the unique users who attended the Zoom meeting.
2. `date = ''`: This variable will hold the date of the Zoom meeting. It is initialized as an empty string.
3. `with open("zoom.csv", "r") as f`: This opens the CSV file named "zoom.csv" in read mode and assigns it to the file object `f`. The `with` statement ensures that the file is automatically closed after it's done being processed.
4. `next(f)`: This skips the first line of the CSV file, assuming it contains header information and not actual data.
5. `for line in f:`: This iterates through each line in the CSV file.
6. `row = line.rstrip().split(",")`: This splits the line into individual data elements using the comma as the separator and stores them in the `row` list.
7. `l = len(row)`: This calculates the length of the `row` list, which is the number of data elements in each line of the CSV file.
8. `if l == 8:`: This checks if the line contains exactly 8 data elements. This assumes that each line in the CSV file represents a record, and a valid record should have 8 data elements.
9. `if date == '':`: This checks if the `date` variable is still an empty string, indicating that it hasn't been assigned a date yet.
10. `date = row[2]`: This assigns the value of the third data element in the `row` list to the `date` variable. This is based on the assumption that the date of the meeting is located in the third column of the CSV file.
11. `date = date.replace("/", "-")`: This replaces any forward slashes in the `date` with dashes, assuming that the date is in a format like "MM/DD/YYYY."
12. `date = date[0:9]`: This extracts the first 9 characters of the `date` variable, assuming it contains the date in the format "MM-DD-YYYY."
13. `name = row[0]`: This assigns the value of the first data element (username) in the `row` list to the `name` variable.
14. `if name not in attendance:`: This checks if the `name` is not already in the `attendance` list. If the user's name is not present in the list, it means they are a unique participant, and their name is added to the `attendance` list.
15. `with open(date + ".txt", "w") as f:`: This opens a new text file named with the extracted `date` (formatted as "MM-DD-YYYY.txt") in write mode. This file will be used to store the final report.
16. `for user in sorted(attendance):`: This loops through the sorted list of unique participants (`attendance`) alphabetically.
17. `f.write(user + "\n")`: This writes each user's name followed by a newline character in the text file. The resulting file will contain a list of unique participants in alphabetical order.

It's important to note that this program assumes a specific CSV file format with eight data elements per record, and it extracts the date from the third column of the CSV file. Depending on the actual CSV file's structure, modifications may be needed to suit different data layouts or formats.
