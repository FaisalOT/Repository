from math import sqrt
def printBoard(board):
        lngth = len(board)
        b = ''
        for row in range(lngth):
                b +='\n'
                for col in range(lngth):
                        b += f' {board[row][col]}'

        print(b)


def SelectUnassignedVariable(board, n, i, j):
        for x in range(i,n):
                for y in range(j,n):
                        if board[x][y] == 0:
                                return x,y
        for x in range(0,n):
                for y in range(0,n):
                        if board[x][y] == 0:
                                return x,y
        return None,None

def consistent(board, n, i, j, val):
        for x in range(len(board)):
                if board[i][x] == val and j != i:
                        return False

        for y in range(len(board)):
                if board[y][j] == val and i != y:
                        return False
        block = int(sqrt(n))
        r = (i//block)*block
        c = (j//block)*block

        for x in range(r, r + block):
                for y in range(c, c + block):
                        if board[x][y] == val:
                                return False
        return True

def solveSudoku(board, n, i=0, j=0):
        #printBoard(board) #print progress
        i,j = SelectUnassignedVariable(board, n, i, j)
        if i == None:
                return True
        for val in range(1, n+1):
                if consistent(board, n, i, j, val):
                        board[i][j] = val
                        if solveSudoku(board, n, i, j):
                                return True

                        board[i][j] = 0

        return False

def main():
        input = [[0,3,0,4],[0,4,0,0],[4,0,2,3],[3,0,4,0]]
        solved = solveSudoku(input,len(input))
        if not solved:
                print('unsolvable')
        else: printBoard(input)

if __name__ == '__main__':
        main()