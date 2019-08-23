import turtle
import time

def coord_convert(raw_coords):
    coords = []
    lined_coords = raw_coords.split('\n')
    for coord in lined_coords:
        new_coord = coord.split()
        #increse coord size by 10 for graphics window
        coords.append([int(new_coord[0])*10,int(new_coord[1])*10])
    return coords

def algor_graphics(coords,lines):

    wn = turtle.Screen()
    tu = turtle.Turtle()
    tu.clear()
    #draw points
    for coord in coords:
        tu.up()
        tu.setpos(coord)
        tu.down()
        tu.dot()
        #time.sleep(.3)
    #draw lines
    for line in lines:
        tu.up()
        tu.setpos(line[0])
        tu.down()
        tu.setpos(line[1])
        #time.sleep(.3)
    wn.exitonclick()


def mesh_generator(coords):
    coords = sorted(coords)
    lines = []
    #fix so that it only connects to every point in it's current area, as the xrange inceaeses sorted point by sorted point
    #draw lines as you increase points available
    for i in range(len(coords)+1):
        coord_set = coords[:i]
        for j in range(len(coord_set)):
            for k in range(1,len(coord_set[j:])):
                line_intersect = False
                for line in lines:
                    if intersecting_line_segments([coord_set[j],coord_set[j+k]],line) == True :
                        line_intersect = True
                if line_intersect == False:
                    lines.append([coord_set[j],coord_set[j+k]])

    algor_graphics(coords,lines)


def intersecting_line_segments(seg1, seg2):
    #seg1 ab and seg2 cd
    a = seg1[0]
    b = seg1[1]
    c = seg2[0]
    d = seg2[1]
    x = 0
    y = 1

    #check if point is on  line segment pr?
    def on_segment(p,q,r):
        if q[x] <= max(p[x],r[x] and q[x] >= min(p[x],r[x]) and q[y] <= max(p[y],r[y]) and q[y] >= min(p[y],r[y])):
            return True
        return False

    # find orientation
    def orientation(p,q,r):
        val = (q[y]-p[y])*(r[x]-q[x]) - (q[x]-p[x])*(r[y]-q[y])

        if val == 0: return 0 # colinear
        if val > 0: return 1  # clockwise
        if val < 0: return 2  #counterclockwise

    def do_intersect(p1,q1,p2,q2):
        #find 4 orientations needed for general
        #and special cases
        o1 = orientation(p1,q1,p2)
        o2 = orientation(p1,q1,q2)
        o3 = orientation(p2,q2,p1)
        o4 = orientation(p2,q2,q1)

        if p1 == p2 or p1 == q2 or q1 == p2 or q1 == q2:
            return False

        #general case
        if(o1 != o2 and o3 != o4):
            return True


        '''
        #specialCases
        #p1, q1 and p2 are colinear and p2 lies on segment p1q1
        if o1 == 0 and on_segment(p1,p2,q1): return True

        #p1, q1 and q2 are colinear and q2 lies on segment p1q1
        if o2 == 0 and on_segment(p1,q2,q1): return True

        #p2, q2 and p1 are colinear and p1 lies on segment p2q2
        if o3 == 0 and on_segment(p2,p1,q2): return True

        #p2, q2 and q1 are colinear and q1 lies on segment p2q2
        if o4 == 0 and on_segment(p2,q1,q2): return True
        '''
        return False

    return do_intersect(a,b,c,d)


raw_coords = '''0 0 
0 6 
6 0 
6 6 
2 2 
2 4 
4 2 
4 4'''


print(intersecting_line_segments([[0,0],[1,1]],[[0,0],[2,1]])) #false
print(intersecting_line_segments([[1,0],[1,1]],[[0,2],[3,3]])) #false
print(intersecting_line_segments([[1,0],[1,4]],[[1,1],[3,3]])) #true
print(intersecting_line_segments([[1,0],[1,4]],[[0,1],[3,3]])) #true

mesh_generator(coord_convert(raw_coords))