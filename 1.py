# Нам нужно перевернуть половину односвязного списка и сравнить с другой половиной 
# Вспоминаем, что у нас есть 2 метода - slow и fast
# Затем пока fast не пустой и пока значения узла fast не равно заданному значению, при каждой итерации обновляем значения slow и fast на следующий после них узел.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        turnover = None #реверс, с которым будем работать
        slow = fast = head
        while fast and fast.next: 
            fast = fast.next.next # половина списка
            turnover, turnover.next, slow = slow, turnover, slow.next #переопределяем - переворачиваем половину списка
        if fast: #при fast, slow будет выполняться медленне в 2 раза
            slow = slow.next 
        while turnover and turnover.val == slow.val: #перевернув значения, пройдем методом fast
            slow = slow.next
            turnover = turnover.next
        return not turnover #возращаем результат этих значений
                                  