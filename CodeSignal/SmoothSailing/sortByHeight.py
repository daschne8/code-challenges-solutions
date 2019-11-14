def sortByHeight(a):
    ppl_indxs = []

    for i in range(len(a)):
        if a[i]  != -1:
            ppl_indxs.append(a[i])

    ppl_indxs.sort()

    for i in range(len(a)-1,-1,-1):
        if a[i] != -1:
            a[i] = ppl_indxs.pop()
    return a
