NUM_FRAGMENTS = 4  # easier to change by defining separately rather than embedding a number
# response_list contains the user's input of fragment numbers
form_of_request = "Enter student's {0}?fragment response separated by commas, e.g., 1,3,4,2:"
print(form_of_request.format(str(NUM_FRAGMENTS)))  # NUM_FRAGMENTS, as string, where {0} is
student_response = input()
response_list = student_response.split(',')  # separate the actual numbers
print("You entered" + str(response_list))  # echo
correct_count = 0
for first_number in range(0, NUM_FRAGMENTS - 1):  # will look at every possible pair in the submission
    for second_number in range(first_number + 1, NUM_FRAGMENTS):  # e.g., first_number=1, second_number=2,3
        temp_first = int(response_list[first_number])  # shorthand for convenience
        temp_second = int(response_list[second_number])
        print('Comparing ' + str(temp_first) + ' and ' + str(temp_second))  # inform user of progress
        if temp_first < temp_second:  # correctly ordered
            correct_count += 1

# The proportion of correctly ordered pairs is on the monitor
total_correct_pairs = NUM_FRAGMENTS * (NUM_FRAGMENTS - 1) / 2  # e.g., 4+3+2+1 = 4*5/2 = 10
print('Score is ' + str(round(100 * correct_count / total_correct_pairs)) + '%')
