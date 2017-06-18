def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    ans = 0
    if exp == 0:
        ans = 1

    else:
        ans = base
        for n in range(exp-1):
            ans *= base

    return ans

print(iterPower(8.47, 6))


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return (base * recurPower(base, exp-1))



print(recurPower(2, 4))


