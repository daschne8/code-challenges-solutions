def create_spiral(xLen, yLen):
    spiral_array = []
    for j in range(yLen):
        row = []
        for i in range(xLen):
            row.append(0)
        spiral_array.append(row)

    x_dir = 1
    y_dir = 0 #increment walk length each time y direction changes
    walk_length = 1
    walked = 0
    total_numbers = xLen * yLen
    x, y = int(xLen/2) , int(yLen/2)
    spiral_array[y][x] = 1

    for i in range(2,total_numbers + 1):
        x += x_dir
        y += y_dir
        walked += 1

        if walked == walk_length:

            if x_dir == 1:
                x_dir = 0
                y_dir = 1
                walked = 0

            elif y_dir == -1:
                x_dir = 1
                y_dir = 0
                walk_length += 1
                walked = 0

            elif x_dir == -1:
                x_dir = 0
                y_dir = -1
                walked = 0

            elif y_dir == 1:
                x_dir = -1
                y_dir = 0
                walk_length += 1
                walked = 0

        spiral_array[y][x] = i

    return spiral_array

def sum_spiral(len):
    spiral_array = create_spiral(len, len)
    sum = 1
    spiral_range = int(len/2)
    center = spiral_range
    for i in range(1,spiral_range+1):
        sum += spiral_array[center + i][center + i]
        sum += spiral_array[center + i][center - i]
        sum += spiral_array[center - i][center + i]
        sum += spiral_array[center - i][center - i]
    return(sum)



#for row in create_spiral(5,5): print(row)
print(sum_spiral(1001))
#669171001
'''probably a much simpler math based approach to this but i wanted to create the spiral'''

