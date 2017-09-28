'''Source of data'''

point_data_file = open('sampleData.txt')
# Where in tuple the data is stored
X_COORD_IND = 0
Y_COORD_IND = 1
INCLUDED_IND = 2
LAST_LINE_IND = 3


def get_next_data():
    '''
    Precondition: Not at end of file
    Returns tuple with the following:
    ofType1 = first (numerical) element in next line
    ofType2 = second (numerical) element in next line
    inRegion = (boolean) third element
    last_char = '\n' only if the line read is not the last
    '''

    raw_line = point_data_file.readline()
    line = raw_line.split()
    ofType1 = float(line[X_COORD_IND])  # value of the first real-world parameter
    ofType2 = float(line[Y_COORD_IND])
    # Whether or not this is a valid data point
    inRegion = (lambda x: True if x == "true" else False)(line[INCLUDED_IND])
    last_char = raw_line[len(raw_line) - 1]  # '\n' only when not last line
    return ofType1, ofType2, inRegion, last_char


class Rectangle:
    # Class Invariant 1: x_lo <= x_hi
    # Class Invariant 2: y_lo <= y_hi

    def __init__(self, an_x_lo, a_y_lo, an_x_hi, a_y_hi):
        self.x_lo, self.x_hi, self.y_lo, self.y_hi = an_x_lo, an_x_hi, a_y_lo, a_y_hi

    def create_expanded(self, an_x, a_y):
        # Produces a rectangle based on self, enlarged by an_x and a_y if applicable
        if an_x < self.x_lo: self.x_lo = an_x
        if an_x > self.x_hi: self.x_hi = an_x
        if a_y < self.y_lo: self.y_lo = a_y
        if a_y > self.y_hi: self.y_hi = a_y
        return self

    def print(self):
        print('Rectangle: {0}, {1}, {2}, {3}'.format(self.x_lo, self.y_lo, self.x_hi, self.y_hi))


def get_rectangle():
    '''
    Preconditions:
    1. sampleData.txt contains at least one line
    2. Each line in sampleData.txt consists of text, text, and "true" or "false"
    3. At least one "true" occurs

    Post 1: All applicable data are in applicable_rectangle
    Post 2: No inapplicable data read in are in applicable_rectangle
    Post 3: applicable_rectangle is minimal in size
    Post 4: applicable_rectangle has been returned

    Illustrations: (see 1 below)
    '''

    # Objective 1 = Post 3: applicable_rectangle is minimal in size
    # Objective 2: All applicable data read in are in applicable_rectangle
    # Objective 3 = Post 2: No inapplicable data read in are in applicable_rectangle

    # next_data is first line with applicable data (note precondition 3)
    next_data = get_next_data()  # first line
    while not next_data[INCLUDED_IND] and (next_data[LAST_LINE_IND] == '\n'):
        # not applicable and not last line
        next_data = get_next_data()

    # Objectives 1-3 are fulfilled:
    applicable_rectangle = Rectangle (next_data[X_COORD_IND], next_data[Y_COORD_IND], next_data[X_COORD_IND], next_data[Y_COORD_IND])

    # Objective 4: All data has been read
    while next_data[LAST_LINE_IND] == '\n':
        next_data = get_next_data()
        if next_data[INCLUDED_IND]:
            applicable_rectangle.create_expanded(next_data[X_COORD_IND], next_data[Y_COORD_IND])

    # Objective 5 = Post 4: applicable_rectangle has been returned
    return applicable_rectangle


get_rectangle()
