# ########################
# @Fr4nc3
# 03/30/2015
# file: effects.py
# File contains functions that allow different effects in an image
# ########################


def object_filter(files, output_file):
    '''Implements ppm images filter.'''
    images = []
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

    #the new filtered image
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


def clean_image(pixel1, pixel2, pixel3):
    '''check which pixels are equals. '''
    # comparing if the list are similar
    if pixel1 == pixel2 and pixel2 == pixel3:
        return pixel1[0], pixel1[1], pixel1[2]

    if pixel2 == pixel3:
        return pixel2[0], pixel2[1], pixel2[2]

    if pixel1 == pixel2:
        return pixel1[0], pixel1[1], pixel1[2]

    if pixel1 == pixel3:
        return pixel1[0], pixel1[1], pixel1[2]


def shades_of_gray(input_file, output_file):
    create_ppm(input_file, output_file, 'gray')


def negate_red(input_file, output_file):
    create_ppm(input_file, output_file, 'red')


def negate_green(input_file, output_file):
    create_ppm(input_file, output_file, 'green')


def negate_blue(input_file, output_file):
    create_ppm(input_file, output_file, 'blue')


def create_ppm(input_file, output_file, action):
    '''implements image color filter.'''
    file_type, column, row, max_color, body_raw = load_file(input_file)

    ppm_file = open(output_file, 'w')
    ppm_file.write("%s\n" % file_type)
    ppm_file.write("%s %s\n" % (column, row))
    ppm_file.write("%d\n" % max_color)

    for i in range(0, len(body_raw) - 1, 3):
        red = int(body_raw[i])
        green = int(body_raw[i + 1])
        blue = int(body_raw[i + 2])
        #uses action param to implement the filter to use
        if action == 'gray':
            red, green, blue = gray(red, blue, green)
        elif action == 'green':
            green = negate(green, max_color)
        elif action == 'red':
            red = negate(red, max_color)
        elif action == 'blue':
            blue = negate(blue, max_color)

        ppm_file.write("%d %d %d\n" % (red, green, blue))

    ppm_file.close()


def negate(color, max_color):
    '''return the inverse of the color.'''
    return max_color - color


def gray(red, blue, green):
    average = (red + blue + green) / 3
    # I can't think a pretty way to return the same color variable.
    return average, average, average


def load_file(file_input, action='variables'):
    '''load image into an array or return the variables
    this is my way to recycle the open the file method.'''
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
