class ListNode:

    def __init__(self, val=0, nxt=None):
        self.val = val
        self.nxt = nxt


class MyCircularQueue:

    def __init__(self, k: int):
        # use a linked list
        # head is a dummy node to distinguish empty and full
        self.head = ListNode(0)
        self.tail = self.head

        curr = self.head
        for _ in range(k):
            curr.nxt = ListNode(0)
            curr = curr.nxt
        curr.nxt = self.head
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.tail = self.tail.nxt
        self.tail.val = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.head = self.head.nxt
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.head.nxt.val

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.tail.val

    def isEmpty(self) -> bool:
        return self.head == self.tail

    def isFull(self) -> bool:
        return self.tail.nxt == self.head
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()