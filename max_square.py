# This program takes a list of strings containing a matrix of
# 1's and 0's and returns the area of the largest square containing only 1's

# check if submatrix contains all 1's
def IsSquare(subMatrix):
    for row in subMatrix:
        for digit in row:
            if digit == 1:
                continue
            else:
                return False
    return True

def MaximalSquare(strArr): 
    # create matrix
    matrix = []
    row = []
    for string in strArr:
        for digit in string:
            row.append(int(digit))
        matrix.append(row)
        row = []
    base = len(matrix[0])
    height = len(matrix)
 
    maxArea = 1
    # check each item in each row of each list
    for y, line in enumerate(matrix):
        for x, digit in enumerate(line):
            if digit == 1:
                # size of first square submatrix to check
                side = 2
                # create an incrementally bigger submatrix if it contains all 1's
                while x + side <= base and y + side <= height:
                    subMatrix = [matrix[i][x:x + side] for i in range(y, y + side)]
                    if IsSquare(subMatrix) == True:
                        area = side**2
                        # set new largest area of square containing 1's
                        if area > maxArea:
                            maxArea = area
                        side += 1
                    else:
                        break
            else:
                continue
    return maxArea
    
# keep this function call here  
print MaximalSquare(raw_input())  
