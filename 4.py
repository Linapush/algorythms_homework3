# Учитывая m x nдвумерную двоичную сетку grid, которая представляет карту '1's (суша) и '0's (вода),
# верните число островов .
# Остров окружен водой и образован путем соединения соседних земель по горизонтали или вертикали.
# Вы можете предположить, что все четыре края сетки окружены водой.

# Рассмотрим каждую ячейку. Если это остров (1) запускаем поиск в глубину, чтобы осмотреться вправо, влево, вверх и вниз
# Используем рекурсивную функцию

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0 

        count = 0 #рассмотрим значение для каждой ячейки
        for row in range(len(grid)): #смотрим значения строки
            for col in range(len(grid[0])): #и столбца
                if grid[row][col] == '1':
                    self.dfs(grid, row, col)
                    count += 1
        return count
    
    # в случае, если мы выйдем за край матрицы 
    def dfs(self, grid, row, col):
        if row<0 or col<0 or row>=len(grid) or col>=len(grid[0]) or grid[row][col] != '1':
            grid[row][col] = '0' # в случае, если не выйдем за границу, помечаем ячейку как 0 
            self.dfs(grid, row+1, col) #смотрим вверх
            self.dfs(grid, row-1, col) #смотрим вниз
            self.dfs(grid, row, col+1) #смотрим влево
            self.dfs(grid, row, col-1) #смотрим вправо
            return 1
        else:
            return 0