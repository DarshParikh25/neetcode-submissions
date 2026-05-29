from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # For 9x9: TC: O(1), SC: O(1)
        # In general, TC: O(n*n), SC: O(n*n)
        # rows = [set() for _ in range(9)]
        # cols = [set() for _ in range(9)]

        # boxes = defaultdict(set)

        # for r in range(9):
        #     for c in range(9):
        #         num = board[r][c]

        #         if num != '.':
        #             if num in rows[r] or num in cols[c] or num in boxes[(r // 3, c // 3)]:
        #                 return False
        #             else:
        #                 rows[r].add(num)
        #                 cols[c].add(num)
        #                 boxes[(r // 3, c // 3)].add(num)

        # return True

        # For 9x9: TC: O(1), SC: O(1)
        # In general, TC: O(n*n), SC: O(n)
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue

                num = int(board[r][c]) - 1

                bit = 1 << num

                box = (r // 3) * 3 + (c // 3)

                if rows[r] & bit or cols[c] & bit or boxes[box] & bit:
                    return False

                rows[r] |= bit
                cols[c] |= bit
                boxes[box] |= bit

        return True