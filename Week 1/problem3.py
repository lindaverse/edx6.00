s = 'rilascmwfxylwq'

alpha_sequences = []
alpha_string = ""

for letter in s:
    if len(alpha_string) == 0:
        alpha_string += letter
    else:
        if letter >= alpha_string[(len(alpha_string))-1]:
            alpha_string += letter
        else:
            alpha_sequences.append(alpha_string)
            alpha_string = letter
alpha_sequences.append(alpha_string)

max_len = len(max(alpha_sequences, key=len))

for sequence in alpha_sequences:
    if len(sequence) == max_len:
        print(sequence)
        break

