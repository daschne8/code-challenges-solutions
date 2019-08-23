#start at base of triangle next time
#see mathers explanation page 1

def import_num_tri():
    num_tri = []
    with open('Euler18Text', newline='\n') as inputfile:
        pre_tri = inputfile.read().splitlines()
        for i in pre_tri:
            num_line = []
            for j in i.split():
                num_line.append(int(j))
            num_tri.append(num_line)
    return num_tri

def triangle_path(triangle):
    length = len(triangle)
    #0 = path, 1 = value so far, 2 = depth
    paths = [[[0],triangle[0][0],0]]
    completed_paths = []
    while(len(paths)>0):
        path_1 = paths.pop(0)
        path_2 = [list(path_1[0]),path_1[1], path_1[2]]
        #nature of triangele means positions that can be added will always be its own position(n) and (n+1)
        n = path_1[0][-1]
        depth = path_1[2]
        if depth < length :
            path_1[0].append(n)
            path_1[1] += triangle[depth+1][n]
            path_1[2] += 1
            if depth + 1 == length -1:
                completed_paths.append(path_1)
            else:
                paths.append(path_1)

            path_2[0].append(n+1)
            path_2[1] += triangle[depth+1][n+1]
            path_2[2] += 1
            if depth+1 == length -1:
                completed_paths.append(path_2)
            else:
                paths.append(path_2)

    print(paths)
    max_path_value = 0
    max_path = []
    for path in completed_paths:
        if path[1] > max_path_value:
            max_path_value = path[1]
            max_path = path
    return(max_path)


def base_up(triangle):
    for row in range(len(triangle)-1,0,-1):
        for column in range(len(triangle[row])-1):
            triangle[row-1][column] += max(triangle[row][column], triangle[row][column + 1])
            print(triangle)
    return triangle[0][0]

print(base_up(import_num_tri()))
#print(triangle_path(import_num_tri()))
#[[0, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6, 7, 8, 8, 9], 1074, 14]