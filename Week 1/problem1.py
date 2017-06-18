numbob = 0
state = 0

s = 'sjshsbobbobsdhfjkafsdjkncvakhufvjkhvckjvcjkvjdackljasvdkljvlkacsjkvljcaxklavc'

for letter in s:
    if state == 0:
        if letter == "b":
            state = 1
    elif state == 1:
        if letter == "o":
            state = 2
        elif letter == "b":
            state = 1
        else:
            state = 0
    elif state == 2:
        if letter == "b":
            numbob += 1
            state = 3
        else:
            state = 0
    elif state == 3:
        if letter == "o":
            state = 2
        elif letter == "b":
            state = 1
        else:
            state = 0
print(numbob)

from re import findall

print(len(findall("(?=bob)", s)))

#-----------------------------------------

numbobs = 0

for num in range(len(s)):
    if s[num:num+3] == "fvjkhvc":
        numbobs += 1
print(numbobs)

#------------------------------------------

numbobs = 0


while 