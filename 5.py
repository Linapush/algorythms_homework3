class Solution:
    def islandPerimeter(self, grid):
        count = 0 #счетчик
        #прибавляем нули, чтобы не было ошибки list index out of range
        grid.insert(0, [0]*len(grid[0])) #сверху
        grid.append([0]*len(grid[0])) #снизу
        for i in range(len(grid)): 
            grid[i].insert(0, 0) #слева
            grid[i].append(0) #справа
        #проходимся по всей матрице
        for row in range(len(grid)): #ряды
            for col in range(len(grid[0])): #столбцы
                if grid[row][col] == 1: #если клетка - это суша
                    count += 4 #у квадрата 4 грани
                    if grid[row-1][col] == 1: #если сверху не граница, а еще одна суша
                        count -= 1 #вычитаем 1 (там нет стенки)
                    if grid[row+1][col] == 1: #если снизу не граница, а еще одна суша
                        count -= 1 #вычитаем 1
                    if grid[row][col-1] == 1: #если слева не граница, а еще одна суша
                        count -= 1 #вычитаем 1
                    if grid[row][col+1] == 1: #если справа не граница, а еще одна суша
                        count -= 1 #вычитаем 1
        return count