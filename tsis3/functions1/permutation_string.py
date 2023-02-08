def permutations(rem, ind=''):
    if len(rem) == 0:
        print(ind)

    for i in range(len(rem)):
        newCan = ind + rem[i]
        newRem = rem[0:i] + rem[i + 1:]

        permutations(newRem, newCan)

s = input()
permutations(s)