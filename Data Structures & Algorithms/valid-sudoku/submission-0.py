class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_row(b, row_i):
            row = b[row_i]
            seen = set()
            for n in row:
                if n in seen:
                    print("seen/is_valid_row:", seen)
                    print("n", n)
                    return False
                if n != '.': seen.add(n)
            return True
        
        def is_valid_col(b, col_i):
            col = [b[row][col_i] for row in range(len(b))]
            seen = set()
            for n in col:
                if n in seen: 
                    print("seen/is_valid_col:", seen)
                    print("n:", n)
                    return False
                if n != '.': seen.add(n)
            return True

        def is_valid_square(b, row_i, col_i):
            sqr = [b[r][c] for c in range(col_i, col_i + 3) for r in range(row_i, row_i + 3)]
            seen = set()
            for n in sqr:
                if n in seen:
                    print("seen/is_valid/sqr:", seen)
                    print("n:", n)
                    print("sqr:", sqr)
                    return False
                if n != '.': seen.add(n)
            return True
        
        rows = all([is_valid_row(board, i) for i in range(0, len(board))])
        cols = all([is_valid_col(board, i) for i in range(0, len(board))])
        sqrs = all([is_valid_square(board, i, j) for i in [0, 3, 6] for j in [0, 3, 6]])
    
        return all([rows, cols, sqrs])




