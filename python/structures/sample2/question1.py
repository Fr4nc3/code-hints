# ***********************************************************
# Fr4nc3
# This program/script write and read 10 int in a csv file write them back
# in a list and print the list


with open('lab2.csv', 'w') as f:  # w always rewrite content from the file
    for num in range(11):
        f.write(str(num) + '\n')

number_list = []  # I will storage the number in this list

with open('lab2.csv') as f:
    for line in f.readlines():
        number_list.append(int(line))

# print(number_list)  dump content of the list in the console
for x in number_list:
    print(x)  # print to console content of the list one by one
