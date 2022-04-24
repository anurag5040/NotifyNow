import difflib

first_file = "C:\\Users\\ASHISH\\OneDrive\\Desktop\\comp\\Old.txt"
second_file = "C:\\Users\\ASHISH\\OneDrive\\Desktop\\comp\\New.txt"

first_file_lines = open(first_file).readlines()
second_file_lines = open(second_file).readlines()

difference = difflib.HtmlDiff().make_file(first_file_lines, second_file_lines, first_file, second_file)
difference_report = open('C:\\Users\\ASHISH\\OneDrive\\Desktop\\comp\\difference_report.html','w')
difference_report.write(difference)
difference_report.close()

