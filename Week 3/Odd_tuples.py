def oddTuples(aTup):
    rtnTup =  ()
    count = 1
    for element in aTup:
        if count % 2 != 0:
            rtnTup = rtnTup + (element,)
        count+= 1
    return rtnTup

print(oddTuples(("I", "am", "a", "test", "tuple")))

