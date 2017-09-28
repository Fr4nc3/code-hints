'''
template code 

'''

from tkinter import *

myGui = Tk()
myGui.geometry('400x400')
myGui.title('*UNOFFICIAL* CS-521 Grade Calculator')

welcome_label = Label(myGui, text='Unofficial CS-521 Grade Calculator', fg='red').grid(row=0, column=2)


def calculate_grade():
    '''
    Lab Grades - Calculates invoked the .get() from StringVAR which returns the string entered by user. We then float the string.
    After we add all the lab grades, divide by 4(total labs) and multiply by 10 (10% of grade)
    '''
    try:
        lab_grades = ((float(lab1_grade.get()) + float(lab2_grade.get()) + float(lab3_grade.get()) + float(
            lab4_grade.get())) / 4) * 10

        # Floats the Assignment grades and divides by 6(total assisgnments) and multiplies by 0.60 (60%)
        assignment_grades = ((float(assignment1_grade.get()) + float(assignment2_grade.get()) + float(
            assignment3_grade.get())
                              + float(assignment4_grade.get()) + float(assignment5_grade.get()) + float(
            assignment6_grade.get())) / 6) * 0.60

        # Floats Final grade and multiplies it by 0.30 (30%)
        finalgrade = float(final_grade.get()) * 0.30

        # Sums up the number grade, rounds 2 decimals
        grade = round(lab_grades + assignment_grades + finalgrade, 2)

        # If/elif as per syllabus to calculate letter grade
        if 100 >= grade >= 95:
            letter_grade = 'A'
        elif 94.99 >= grade >= 90:
            letter_grade = 'A-'
        elif 89.99 >= grade >= 85:
            letter_grade = 'B+'
        elif 84.99 >= grade >= 80:
            letter_grade = 'B'
        elif 79.99 >= grade >= 75:
            letter_grade = 'B-'
        elif 74.99 >= grade >= 70:
            letter_grade = 'C+'
        elif 69.99 >= grade >= 65:
            letter_grade = 'C'
        elif 64.99 >= grade >= 60:
            letter_grade = 'C-'
        elif 59.99 >= grade >= 50:
            letter_grade = 'D'
        else:
            letter_grade = 'F'
        # Displays number grade and letter grade for course
        calculated_grade = Label(myGui, text='Your Grade is: {0}'.format(grade)).grid(row=18, column=2)
        calculated_letter_grade = Label(myGui, text='Your Letter Grade is: {0}'.format(letter_grade)).grid(row=19,
                                                                                                           column=2)
    # In case we don't have numbers entered...yes I didn't clear it out if you fix it...sorry!
    except ValueError:
        bad_input = Label(myGui, text='Bad Input Was Entered!').grid(row=18, column=2)
        bad_input2 = Label(myGui, text='Please fix and enter only numbers!').grid(row=19, column=2)


'''
Creating each variable for the Entry, could have used DoubleVar and would not require to float on calculate_grade
However with DoubleVar it autofills with 0.0
'''
lab1_grade, lab2_grade, lab3_grade, lab4_grade = StringVar(), StringVar(), StringVar(), StringVar()

'''
Lab Labels and Entrys
'''
lab_label = Label(myGui, text='Labs', fg='blue', font='bold').grid(row=1, column=0)
lab1 = Label(myGui, text='Lab 1 Grade:').grid(row=2, column=0)
lab2 = Label(myGui, text='Lab 2 Grade:').grid(row=3, column=0)
lab3 = Label(myGui, text='Lab 3 Grade:').grid(row=4, column=0)
lab4 = Label(myGui, text='Lab 4 Grade:').grid(row=5, column=0)

lab1_entry = Entry(myGui, textvariable=lab1_grade).grid(row=2, column=2)
lab2_entry = Entry(myGui, textvariable=lab2_grade).grid(row=3, column=2)
lab3_entry = Entry(myGui, textvariable=lab3_grade).grid(row=4, column=2)
lab4_entry = Entry(myGui, textvariable=lab4_grade).grid(row=5, column=2)

'''
Assignments Variables, Labels and Entrys
'''
assignment1_grade, assignment2_grade, assignment3_grade, assignment4_grade, assignment5_grade, assignment6_grade = \
    StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
Assignment_label = Label(myGui, text='Assignments', fg='blue', font='bold').grid(row=7, column=0)
Assignment1 = Label(myGui, text='Assignment 1 Grade:').grid(row=8, column=0)
Assignment2 = Label(myGui, text='Assignment 2 Grade:').grid(row=9, column=0)
Assignment3 = Label(myGui, text='Assignment 3 Grade:').grid(row=10, column=0)
Assignment4 = Label(myGui, text='Assignment 4 Grade:').grid(row=11, column=0)
Assignment5 = Label(myGui, text='Assignment 5 Grade:').grid(row=12, column=0)
Assignment6 = Label(myGui, text='Assignment 6 Grade:').grid(row=13, column=0)

Assignment1_entry = Entry(myGui, textvariable=assignment1_grade).grid(row=8, column=2)
Assignment2_entry = Entry(myGui, textvariable=assignment2_grade).grid(row=9, column=2)
Assignment3_entry = Entry(myGui, textvariable=assignment3_grade).grid(row=10, column=2)
Assignment4_entry = Entry(myGui, textvariable=assignment4_grade).grid(row=11, column=2)
Assignment5_entry = Entry(myGui, textvariable=assignment5_grade).grid(row=12, column=2)
Assignment6_entry = Entry(myGui, textvariable=assignment6_grade).grid(row=13, column=2)

'''
Final Exam Variable, Label and Entry
'''
final_grade = StringVar()
Final_label = Label(myGui, text='Final Exam', fg='blue', font='bold').grid(row=15, column=0)
Final = Label(myGui, text='Final Exam Grade:').grid(row=16, column=0)
Final_entry = Entry(myGui, textvariable=final_grade).grid(row=16, column=2)

button_calculate = Button(myGui, text='Calculate Grade', command=calculate_grade).grid(row=17, column=0)
button_quit = Button(myGui, text='Quit', command=myGui.quit).grid(row=17, column=2)

# Invoking mainloop for TK object
myGui.mainloop()
