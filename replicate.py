file_to_read ="output.txt"
write_to_file="Old.txt"


file = open(file_to_read,"r")
data = file.read()
file.close()


with open(write_to_file,"a") as file:
    f = open('Old.txt', 'r+')
    f.truncate(0)
    file.write(data)
print('completed')