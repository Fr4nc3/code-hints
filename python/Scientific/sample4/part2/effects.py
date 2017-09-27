# ########################
# @Fr4nc3
# 04/06/2015
# file: effects.py
# File contains functions that allow different effects in an image
# ########################
from io import SEEK_CUR
import shutil


def ppm_filter(input_file, files, output_file):
    """Implements ppm images filter."""
    images = [load_file(input_file, 'list')]

    for file in files:
        images.append(load_file(file, 'list'))

    '''here I will assume 3 files
     and check if the 3 files have the same dimension. '''
    if len(images) != 3 or (images[0][1] != images[1][1]
                            or images[0][1] != images[2][1]
                            or images[0][2] != images[1][2]
                            or images[0][2] != images[2][2]):
        exit("The images don't have same dimension.")

    '''because assuming 3 files are now with the same dimensions
     I grab the first image to create the header of my new filtered image.'''
    file_type = images[0][0]
    column = images[0][1]
    row = images[0][2]
    max_color = images[0][3]

    # the new filtered image
    ppm_file = open(output_file, 'w')
    ppm_file.write("%s \n" % file_type)
    ppm_file.write("%s %s\n" % (column, row))
    ppm_file.write("%d\n" % max_color)

    for i in range(0, len(images[0][4]) - 1, 3):
        '''the 4th element in each image list is 'body_raw'
        here I am reading one pixel per file at the time.
        This is very similar to the method create_ppm, but with multiple
        files. Pixel has the structure [red, green, blue] . '''
        pixel1 = [int(images[0][4][i]), int(images[0][4][i + 1]),
                  int(images[0][4][i + 2])]

        pixel2 = [int(images[1][4][i]), int(images[1][4][i + 1]),
                  int(images[1][4][i + 2])]

        pixel3 = [int(images[2][4][i]), int(images[2][4][i + 1]),
                  int(images[2][4][i + 2])]
        '''here I am printing to the new filtered file the returned pixel
         from clean_image which is the pixel repeated at least twice'''
        ppm_file.write("%d %d %d\n" % clean_image(pixel1, pixel2, pixel3))

    ppm_file.close()


def bmp_filter(input_file, files, output_file):
    """create a new bmp """

    '''this is a horrible hack that I did because when I created a bmp
     from scratch gives me errors'''
    if input_file != output_file:
        shutil.copy(input_file, output_file)

    img_file = open(output_file, "rb+")
    file_size = read_int(img_file, 2)
    start = read_int(img_file, 10)
    width = read_int(img_file, 18)
    height = read_int(img_file, 22)

    '''here I assumed 2 files'''
    img_file2 = open(files[0], "rb")
    img_file3 = open(files[1], "rb")

    scan_line_size = width * 3
    if scan_line_size % 4 == 0:
        padding = 0
    else:
        padding = 4 - scan_line_size % 4

    if file_size != (start + (scan_line_size + padding) * height):
        exit("Not a 24-bit true color image file.")

    # assuming the three images have the same characteristic
    img_file.seek(start)
    img_file2.seek(start)
    img_file3.seek(start)

    for row in range(height):
        for col in range(width):
            pixel1 = process_pixel(img_file, 'list')
            pixel2 = process_pixel(img_file2, 'list')
            pixel3 = process_pixel(img_file3, 'list')

            blue, green, red = clean_image(pixel1, pixel2, pixel3)
            img_file.seek(-3, SEEK_CUR)
            img_file.write(bytes([blue, green, red]))

        img_file.seek(padding, SEEK_CUR)
        img_file2.seek(padding, SEEK_CUR)
        img_file3.seek(padding, SEEK_CUR)

    img_file.close()
    img_file2.close()
    img_file3.close()


def object_filter(input_file, output_file, kind, input_files):
    if kind == 't':
        ppm_filter(input_file, input_files, output_file)
    else:
        bmp_filter(input_file, input_files, output_file)


def clean_image(pixel1, pixel2, pixel3):
    """check which pixels are equals. """
    # comparing if the list are similar
    if pixel1 == pixel2 and pixel2 == pixel3:
        return pixel1[0], pixel1[1], pixel1[2]

    if pixel2 == pixel3:
        return pixel2[0], pixel2[1], pixel2[2]

    if pixel1 == pixel2:
        return pixel1[0], pixel1[1], pixel1[2]

    if pixel1 == pixel3:
        return pixel1[0], pixel1[1], pixel1[2]


def shades_of_gray(input_file, output_file, kind):
    create_file(input_file, output_file, kind, 'gray')


def negate_red(input_file, output_file, kind):
    create_file(input_file, output_file, kind, 'red')


def negate_green(input_file, output_file, kind):
    create_file(input_file, output_file, kind, 'green')


def negate_blue(input_file, output_file, kind):
    create_file(input_file, output_file, kind, 'blue')


def create_file(input_file, output_file, kind, action):
    if kind == 't':
        create_ppm(input_file, output_file, action)
    else:
        create_bmp(input_file, output_file, action)


def create_ppm(input_file, output_file, action):
    """implements image color filter."""
    file_type, column, row, max_color, body_raw = load_file(input_file)

    ppm_file = open(output_file, 'w')
    ppm_file.write("%s\n" % file_type)
    ppm_file.write("%s %s\n" % (column, row))
    ppm_file.write("%d\n" % max_color)

    for i in range(0, len(body_raw) - 1, 3):
        red = int(body_raw[i])
        green = int(body_raw[i + 1])
        blue = int(body_raw[i + 2])
        # uses action param to implement the filter to use
        red, green, blue = filter_color(red, green, blue, max_color, action)
        ppm_file.write("%d %d %d\n" % (red, green, blue))

    ppm_file.close()


def create_bmp(input_file, output_file, action):
    """create a new bmp """

    '''this is a horrible hack that I did because create bmp
     from scratch gives me errors'''
    if input_file != output_file:
        shutil.copy(input_file, output_file)

    img_file = open(output_file, "rb+")
    file_size = read_int(img_file, 2)
    start = read_int(img_file, 10)
    width = read_int(img_file, 18)
    height = read_int(img_file, 22)

    scan_line_size = width * 3
    if scan_line_size % 4 == 0:
        padding = 0
    else:
        padding = 4 - scan_line_size % 4

    if file_size != (start + (scan_line_size + padding) * height):
        exit("Not a 24-bit true color image file.")

    '''I left this block comment because I want to revisited later for
    a real solution when create a bmp file.'''
    # img_file = open(output_file, "wb")
    # #img_file.write(bytes(file_size))
    # #img_file.write(bytes(start))
    # img_file.write(bytes(width))
    # img_file.write(bytes(height))

    img_file.seek(start)

    for row in range(height):
        for col in range(width):
            blue, green, red = process_pixel(img_file)
            red, blue, green = filter_color(red, blue, green, 255, action)
            img_file.seek(-3, SEEK_CUR)
            img_file.write(bytes([blue, green, red]))
        img_file.seek(padding, SEEK_CUR)

    img_file.close()


def negate(color, max_color):
    """return the inverse of the color."""
    return max_color - color


def gray(red, blue, green):
    average = int((red + blue + green) / 3)
    # I can't think a pretty way to return the same color variable.
    return average, average, average


def load_file(file_input, action='variables'):
    """load image into an array or return the variables
    this is my way to recycle the open the file method."""
    f = open(file_input)
    '''assuming that the first 3 lines are the file_type
    dimensions and the maximum number of color.'''
    file_type = f.readline().strip()
    column, row = f.readline().split()
    max_color = int(f.readline())

    '''removing all the breaks lines from the body
    so, I will use the image body as big group of triples.'''
    body_raw = f.read().replace('\n', ' ').split()
    f.close()

    if action == 'list':
        return [file_type, column, row, max_color, body_raw]
    else:
        return file_type, column, row, max_color, body_raw


def filter_color(red, blue, green, max_color, action):
    if action == 'gray':
        red, green, blue = gray(red, green, blue)
    elif action == 'green':
        green = negate(green, max_color)
    elif action == 'red':
        red = negate(red, max_color)
    elif action == 'blue':
        blue = negate(blue, max_color)

    return red, blue, green


def apply_effects(input_filename, output_filename, kind, effects,
                  *input_filenames):
    functions = {1: object_filter, 2: shades_of_gray, 3: negate_red,
                 4: negate_green, 5: negate_blue}
    count = 0
    '''I use count I will apply the next filter to the output file'''
    for i in effects:
        option = int(i)
        '''This is used to apply the second effect to the output file'''
        if count != 0:
            read_file = output_filename
        else:
            read_file = input_filename

        count = count + 1
        if option == 1:
            files = []
            for file in input_filenames:
                files.append(file)
            functions[int(i)](read_file, output_filename, kind, files)
        else:
            functions[int(i)](read_file, output_filename, kind)


def process_pixel(file, action='variables'):
    """this method is similar to the one appears in the book
    it gets the 3 colors of a pixel. """
    the_bytes = file.read(3)
    blue = the_bytes[0]
    green = the_bytes[1]
    red = the_bytes[2]

    if action == 'list':
        return [blue, green, red]
    else:
        return blue, green, red


def read_int(file, offset):
    """this method is similar to the one that appear in the book.
    It is used to read a binary file."""
    file.seek(offset)
    the_bytes = file.read(4)
    result = 0
    base = 1
    for i in range(4):
        result = (result + the_bytes[i] * base)
        base = (base * 256)

    return result

