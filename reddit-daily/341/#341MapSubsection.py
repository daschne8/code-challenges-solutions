#[2017-11-24] Challenge #341 [Hard] Finding a Map Subsection
#define limits
#get SQUARE size
#shift square as necessary


def bounding_map(size, coords):
    min_x, max_x, min_y, max_y = coords[0][0], coords[0][0], coords[0][1], coords[0][1]
    for coord in coords:
        min_x = min(min_x, coord[0])
        max_x = max(max_x, coord[0])
        min_y = min(min_y, coord[1])
        max_y = max(max_y, coord[1])

    square_size = max(max_x - min_x, max_y - min_y) + 60
    if (square_size > size):
        square_size = size
    #center of square
    square_x = (min_x + max_x) / 2
    square_y = (min_y + max_y) / 2
    #square point
    square_x = square_x - square_size / 2
    square_y = square_y - square_size / 2
    #check for out of bounds
    if (square_x < 0):
        square_x = 0
    if(square_y < 0):
        square_y = 0
    if((square_x + square_size) > size):
        square_x = size - square_size
    if ((square_y + square_size) > size):
        square_y = size - square_size

    return (int(square_x + .5), int(square_y + .5)), square_size

print(bounding_map(2000, [(600, 600), (700, 1200),(630,1100),(650,1000)]))
print(bounding_map(2000, [(300, 300), (1300, 300)]))
print(bounding_map(2000, [(825, 820), (840, 830), (830, 865), (835, 900)]))
print(bounding_map(5079, [(5079, 5079), (4479, 4479)]))

