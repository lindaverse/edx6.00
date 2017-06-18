def isIn(char, aStr):

    if len(aStr) == 0:
        return False

    midPoint = int(len(aStr) / 2)
    midChar = aStr[midPoint]

    if char == midChar:
        return True
    if char < midChar:
        return isIn(char, aStr[0: midPoint])
    if char > midChar:
        return isIn(char, aStr[midPoint+1:])

print(isIn("c", "abcd"))
