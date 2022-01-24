class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # BFS + graph
        
        # Time complexity: O(rows * cols) -> each cell is visited at least once
        # Space complexity: O(rows * cols) -> in the worst case if all the oranges are rotten they will be added to the queue
        
        rows = len(grid)
        cols = len(grid[0])
        
        # add rotten orange to the queue
        rotten = deque()
        fresh_cnt = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                elif grid[r][c] == 1:
                    fresh_cnt += 1
                    
        # keep track of minutes passed
        minutes_passed = 0
        
        while rotten and fresh_cnt > 0:
            minutes_passed += 1
            for _ in range(len(rotten)):
                x,y = rotten.popleft()
                
                # given x,y, visit all the adjacent cells
                for dx, dy in [(1,0),(-1,0),[0,1],[0,-1]]:
                    xx, yy = x + dx, y + dy
                    # exclude the coordinates that out of the grid boundary
                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue
                    # also ignore cells that are empty or have been visited
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                    # update the fresh count
                    fresh_cnt -= 1
                    
                    # mark the current orange as rotten and add to the queue
                    grid[xx][yy] = 2
                    
                    rotten.append((xx,yy))
        # return - if there are still fresh oranges left           
        return minutes_passed if fresh_cnt == 0 else -1
