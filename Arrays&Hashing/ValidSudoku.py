class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] == '.':
                    pass
                else:
                    if board[i][j] in row:
                        return False
                    else:
                        row.add(board[i][j])

        for j in range(9):
            col = set()
            for i in range(9):
                if board[i][j] == '.':
                    pass
                else:
                    if board[i][j] in col:
                        return False
                    else:
                        col.add(board[i][j])

        

        for k in range(3):
            for l in range(3):
                sqr = set()
                for i in range(3):
                    for j in range(3):
                        ele = board[i + k*3][j + l*3]
                        if ele == '.':
                            pass
                        else:
                            if ele in sqr:
                                return False
                            else:
                                sqr.add(ele)
        
        return True

                