class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        while curr and index > 0:
            index -= 1
            curr = curr.next
        
        if curr and index == 0 and curr != self.tail: return curr.val
        
        return -1

    def addAtHead(self, val: int) -> None:
        newHead = ListNode(val)
        next = self.head.next
        prev = self.head
        prev.next = newHead
        next.prev = newHead
        newHead.next = next
        newHead.prev = prev

    def addAtTail(self, val: int) -> None:
        newTail = ListNode(val)
        prev = self.tail.prev
        next = self.tail
        prev.next = newTail
        next.prev = newTail
        newTail.prev = prev
        newTail.next = next

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = ListNode(val)
        curr = self.head.next

        while curr and index > 0:
            index -= 1
            curr = curr.next

        if curr and index == 0:
            newNode = ListNode(val)
            next = curr
            prev = curr.prev
            next.prev = newNode
            prev.next = newNode
            newNode.prev = prev
            newNode.next = next

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        while curr and index > 0:
            index -= 1
            curr = curr.next
        if curr and curr != self.tail:
            next = curr.next
            prev = curr.prev
            prev.next = next
            next.prev = prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)