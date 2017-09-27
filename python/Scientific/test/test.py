# ####################
# zthis program reads
# a list of ids and 
# salaries and creates
# new file in sorted order
#####################


def swap(list, i, j):
    """ swaps the items at the two given indexes in the list """
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def sort(salary_list):
    """ sorts the given salary_list """

    for i in range(len(salary_list)):

        smallest_index = i
        smallest_salary = salary_list[i][1]

        for j in range(i + 1, len(salary_list)):
            if salary_list[j][1] < smallest_salary:
                smallest_salary = salary_list[j][1]
                smallest_index = j

        if not smallest_index == i:
            swap(salary_list, i, smallest_index)

def read_file(filename):
    """ function that reads in all the lines in the file """

    emp_list = []

    with open(filename, 'rU') as infile:
        for line in infile:
            emp_list.append(line)

    return emp_list

def create_salary_list(file_lines):
    """ formats the lines of the file into a salary list """

    salary_list = []

    for item in file_lines:
        line_list = item.split()
        line_list[0] = int(line_list[0])
        line_list[1] = int(line_list[1])
        line_list = line_list[:2]
        salary_list.append(line_list)

    return salary_list

def write_salary_list(filename, salary_list):
    """ writes the salary list to the given output file name """
    outfile = open(filename, 'w')

    for item in salary_list:
        outfile.write(str(item[0]) + '\t' + str(item[1]) + '\n')

    outfile.close()

def main():
    infile_name = input("What file would you like to read from? ")
    outfile_name = input("What file would you like to write to? ")

    lines = read_file(infile_name)
    salary_list = create_salary_list(lines)
    sort(salary_list)
    write_salary_list(outfile_name, salary_list)

def change(a):
    a = a[:3]

def main2():
    a = [1, 2, 3, 4]
    change(a)
    print(a)

main2()