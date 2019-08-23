#can always add smaller grid + new cols + new rows

def rect_in_grid(cols, rows):
    total_rects = 0
    for down_cols in range(cols,0,-1):
        for down_rows in range(rows,0,-1):
            for i in range(down_cols):
                for j in range(down_rows):
                    total_rects += 1
    return total_rects

def approx_2_mill():
    #col,row,rect value
    closest_grid = [0,0,0]
    searching = 0
    col, row = 1, 1
    while(searching < 2):
        col+=1
        prospective = rect_in_grid(col,row)
        prospective_difference = abs(prospective - 2000000)
        last_difference = abs(closest_grid[2] - 2000000)

        if prospective_difference < last_difference:
            closest_grid = [col,row,prospective]
            print(closest_grid)
            searching = 0
        else:
            searching += 1
            col = 0
            row += 1
    return closest_grid

print(approx_2_mill())

