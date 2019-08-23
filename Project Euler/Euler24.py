def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]


num_str = list('0123456789')
i = 0
for perm in all_perms(num_str):
    i += 1
    if i == 1000000:
        print(perm)