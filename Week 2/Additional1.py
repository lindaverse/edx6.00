import math

def polysum(n, s):

    """
    test
    :param n:
    :param s:
    :return:
    """
    area = (0.25 * n * s**2)/math.tan(math.pi/n)
    perimeter = n * s
    sum = round(area + perimeter**2, 4)
    return sum

print(polysum(38, 53))


#Correct output:
#4378242.092