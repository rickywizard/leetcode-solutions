class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        q = collections.deque()
        visit = set()
        area = 0

        def bfs(r, c) -> int:
            res = 1
            q.append((r, c))
            visit.add((r, c))

            while q:
                r, c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    row, col = (r + dr), (c + dc)

                    if (row in range(rows) and
                        col in range(cols) and
                        grid[row][col] == 1 and
                        (row, col) not in visit):
                        q.append((row, col))
                        visit.add((row, col))
                        res += 1
            
            return res

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = max(bfs(r, c), area)
        
        return area
                    