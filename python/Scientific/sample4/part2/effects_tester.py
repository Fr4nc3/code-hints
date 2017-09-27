# ########################
# @Fr4nc3
# 04/06/2015
# file: effects_tester.py
# File contains functions that allow test effects in  bmp or ppm image
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

    option = input("Enter your the list of effects ie. (1,2,3): ")
    input_filename = input("Enter an input file name: ")
    output_filename = input("Enter name of output file: ")
    kind = input("Kind is the file? (t for text or b for binary): ")

    effects_list = option.split(',')

    if kind == '':
        kind = 't'

    if input_filename == '':
        input_filename = 'tetons1.ppm'

    if output_filename == '':
        output_filename = 'test_output.ppm'

    file2 = ''
    file3 = ''
    if "1" in effects_list:
        file2 = input("Enter an second file name: ")
        file3 = input("Enter an third file name: ")

        # test purposes
        if file2 == '' or file3 == '':
            file2 = 'tetons2_bmp.bmp'
            file3 = 'tetons3_bmp.bmp'

    # start time  to calculate only the image processing time
    start_time = time.time()

    effects.apply_effects(input_filename, output_filename, kind, effects_list,
                          file2, file3)

    print("--- %s seconds ---" % (time.time() - start_time))


main()