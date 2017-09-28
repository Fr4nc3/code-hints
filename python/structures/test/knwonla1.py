import random

# Constants
SOURCE_FILE = 'knowlass_1_annotated_source.txt'
SEPARATOR = '@'

# Contents of SOURCE_FILE are on the console --AND--
# content_list = list of fragments in SOURCE_FILE, separated by SEPARATOR

fileR = open(SOURCE_FILE)
content_of_file = fileR.read()
print('Entire file: ---------------------------')
print(content_of_file)
print('-----------------------------------------')
content_list = content_of_file.split(SEPARATOR)

# (1) reordered_fragment_indices is a re-ordering of 0, 1, ..., content_list.length - 1
# AND (2) the elements of content_list, are on the console in this order

# Part (1)
reordered_fragment_indices = list(range(len(content_list)))  # *
random.shuffle(reordered_fragment_indices)
# Part (2)
print(reordered_fragment_indices)
print()
for i in range(len(content_list)):
    current_index = reordered_fragment_indices[i]
    print(str(current_index) + '.' + content_list[current_index])
