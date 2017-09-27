# ########################
# @Fr4nc3
# 03/30/2015
# file: effects_tester.py
# File contains functions that allow test effects in an image
# ########################
import time
import effects


def main():
    '''main function that takes the user option of manipulate an image.'''

    print("Portable Pixmap (PPM) Image Editor!")
    print("Choose the effect you would like to try:")
    print("1) object_filter")
    print("2) shades_of_gray")
    print("3) negate_red")
    print("4) negate_green")
    print("5) negate_blue")

    option = input("Enter your Option: ")
    input_file = input("Enter an input file name: ")
    out_file = input("Enter name of output file: ")

    # this code block is only for test fast and avoid error
    if option == '':
        option = 1
    else:
        option = int(option)

    if input_file == '':
        input_file = 'tetons1.ppm'

    if out_file == '':
        out_file = 'test_output.ppm'

    # to calculate the time of execution
    start_time = time.time()

    if option == 1:
        files = [input_file]
        file = input("Enter  other image  \n(to finish enter 0): ")
        while file != '0':
            files.append(file)
            file = input("Enter  other image  \n(to finish enter 0): ")

        #this part is for test faster
        if len(files) != 3:
            files = ['tetons1.ppm', 'tetons2.ppm', 'tetons3.ppm']

        #reset start time  to calculate only the image processing time
        start_time = time.time()
        effects.object_filter(files, out_file)

    elif option == 2:
        # shades of gray
        effects.shades_of_gray(input_file, out_file)

    elif option == 3:
        # negate_red
        effects.negate_red(input_file, out_file)

    elif option == 4:
        # negate_green
        effects.negate_green(input_file, out_file)

    elif option == 5:
        # negate_blue
        effects.negate_blue(input_file, out_file)

    else:
        print("out of options")

    print("--- %s seconds ---" % (time.time() - start_time))


main()