# Calculate area of rectangle/square/triangle using variable length arguments.
import math


# defining 'shapeArea' function
def shapeArea(*values):
    """ Function to calculate the area of square/rectangle/triangle """
    # For Square
    if len(values) == 1:
        s = values[0]
        area = s * s
    elif len(values) == 2:  # for rectangle
        l, b = values[0], values[1]
        area = l * b
    else:  # for triangle
        a, b, c = values[0], values[1], values[2]
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return area


# driver code
print('Area of square is:', shapeArea(5))
print('Area of rectangle is:', shapeArea(7, 4))
print('Area of triangle is: {:.2f}'.format(shapeArea(6, 3, 5)))
