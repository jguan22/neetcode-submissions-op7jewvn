class ListNode():

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        # use double linked list
        self.head = ListNode(0)
        self.tail = self.head
        curr = self.head
        for _ in range(k):
            curr.next = ListNode(0)
            curr = curr.next
        curr.next = self.head

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.tail = self.tail.next
        self.tail.val = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = self.head.next
        return True

    def Front(self) -> int:
        if self.head == self.tail:
            return -1
        return self.head.next.val

    def Rear(self) -> int:
        if self.head == self.tail:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.head == self.tail

    def isFull(self) -> bool:
        return self.tail.next == self.head
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()