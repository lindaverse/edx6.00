def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    for num in range(a, 0, -1):
        if a % num == 0 and b % num == 0:
            return(num)


print(gcdIter(12, 6))

def gcdRecur(a, b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

print(gcdRecur(12, 6))