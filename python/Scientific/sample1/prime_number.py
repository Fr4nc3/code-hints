# ***********************************************************
# @Fr4nc3
# 02/11/2015
# file: prime_number.py
# This program determinants if a number not greater than 10,000,001 is prime
# or it is not

number = input("Enter a number: ")

ten_millions_one = 10000001  # so we can accept 10 millions as number to check
if ten_millions_one < number:
    print("the number is too big")
    exit()

i = 2  # i will increase until encounter a integer smaller than "number"
# which can divide it
while i < number:

    if number % i == 0:
        print
        str(number) + " is not a prime."
        break
    i += 1
else:
    print
    str(number) + " is a prime."