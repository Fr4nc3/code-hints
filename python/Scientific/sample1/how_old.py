# *************************************
# @Fr4nc3
# 02/11/2015
# This program calculate how old are you in days only if you are younger than
#  110 years old
from datetime import datetime
from dateutil.relativedelta import relativedelta


# calculating the 110 years in the pass
hundred_ten_years_ago = datetime.now() - relativedelta(years=110)

# enter dob as string
# used raw input bc input only accept integers
date_of_birth = input("Enter your date of birth (mm/dd/yyyy): ")
dob_arr = date_of_birth.split('/')


#convert date_of_birth in datetime object
try:
    dob = datetime(int(dob_arr[2]), int(dob_arr[0]), int(dob_arr[1]))
except:
    exit("format error: correct date format is mm/dd/yyyy")

#if the date that user enters is older than 110 year from today you can not
# calculate your date
if dob < hundred_ten_years_ago:
    print("You are too old for this program (younger than 110 years old)")
    exit()

#calculate difference between dob and today
delta = datetime.now() - dob

#print the difference in days (ignoring the extra seconds, half of the day or
#  midnight)
print("Your age is %d days " % delta.days)


