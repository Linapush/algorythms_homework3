# У нас есть первый элемент в списке, являющийся ссылочным узлом на односвязный список. Узел содержит значение и ссылку на следующий элемент.
# Используем length, чтобы представить значения в виде кортежа

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        self.head = head
        self.next = next 
        if not self.head:   #значение head = 1, в противном случае - 0
            return 0
        current = self.head #текущий элемент
        res = length = 0
        while current.next: 
            length += 1     #значение следующего элемента = 1 - возвращаем длину элемента +1 
            current = current.next
        current = head      
        while current:      #и, наконец, рассматривая значения каждого элемента
            if current.val == 1: 
                res += 2 ** length #считаем, чему будет равно значение результата в десятичной системе счисления
            length -= 1
            current = current.next
        return res #та-да
