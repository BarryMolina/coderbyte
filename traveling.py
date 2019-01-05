def ChessboardTraveling(str): 
        
    # get base and height of rectangle
    coords = str.strip('()').split(')(')
    start = coords[0].split()
    end = coords[1].split()
    b = int(end[0]) - int(start[0]) + 1
    h = int(end[1]) - int(start[1]) + 1
    
    # create matrix of 0's
    matrix = [[0 for x in range(b)] for y in range(h)]
    # set all number of route options in first row to 1
    matrix[0][:] = [1]*len(matrix[0])
    # set first route options of every row to 1
    for item in matrix:
        item[0] = 1
    # iterate over every row but first, start index at 1
    for y, row in enumerate(matrix[1:], 1):
        # iterate over every route options in the row except the first, start index at 1
        for x, routes in enumerate(row[1:], 1):
            # number of routes is the sum of routes below and to the left
            row[x] = row[x - 1] + matrix[y - 1][x]
    #return last item in last row of matrix
    return matrix[-1][-1]
    
# keep this function call here  
print ChessboardTraveling(raw_input())  


  
