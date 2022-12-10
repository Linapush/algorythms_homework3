#В данной задаче будем использовать обход в глубину, проверять правых и левых детей у каждого

class Solution(object):
    def averageOfLevels(self, root):
        result = []
        if (root is None):
            return result
        queue = [root]
        result.append(float(root.val))
        #print (result)
        while queue:
            nextQueue = []
            temp = []
            while queue:  # узлы должны идти слева направо, поэтому сначала нужно извлекать левый узел
                # используем pop(0), так что первый узел 
                node = queue.pop(0)
                if (node.left): #проверяем, есть ли левый ребенок
                    nextQueue.append(node.left)
                    # мы должны добавить значение узла, чтобы мы могли представить его в желаемом формате
                    temp.append(node.left.val)
                if (node.right): #проверяем, есть ли правый ребенок
                    nextQueue.append(node.right)
                    temp.append(node.right.val)
                
            if(temp):
                s = sum(temp)/float(len(temp))
                result.append(s)
            
            queue = nextQueue
        return result