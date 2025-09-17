# Sudoku Solver by Backtracking

N = 9

# Print the grid
def printing(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()

def isSafe(grid, row, col, num):

    # check if the number is already present in the row
    for x in range(9):
        if grid[row][x] == num:
            return False
        
    # check if the number is already present in the column    
    for x in range(9):
        if grid[x][col] == num:
            return False
        
    # Check if the number is already present in the 3x3 grid    
    startrow = row - row % 3
    startcol = col - col % 3

    for i in range(3):
        for j in range(3):
            if grid[i + startrow][j + startcol] == num:
                return False
    return True
    
def Sudoku(grid, row, col):

    # if the we reacher at the end of the grid return true
    if(row == N-1 and col == N):
        return True
    
    # if we reached end of the row moved to the next row
    if col == N:
        row += 1
        col = 0

    # if we reached at predefined cell, skip and moved to the next cell
    if grid[row][col] > 0:
        return Sudoku(grid, row, col + 1)
    
    # try all the possibilities of the current cell
    for num in range(1, N+1, 1):
        if isSafe(grid, row, col, num):
            grid[row][col] = num
            
    # if placing a number gives the solution than return true
            if Sudoku(grid, row, col + 1):
                return True
        
    # otherwise backtracks by original cell
        grid[row][col] = 0

    return False

grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

if (Sudoku(grid, 0, 0)):
    printing(grid)
else:
    print("No Solution Found!!")

