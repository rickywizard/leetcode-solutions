class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage) 

    def visit(self, url: str) -> None:
        newNode = Node(url)
        self.curr.next = newNode
        newNode.prev = self.curr
        self.curr = newNode

    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            steps -= 1
            self.curr = self.curr.prev
        
        if self.curr:
            return self.curr.val

    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            steps -= 1
            self.curr = self.curr.next
        
        if self.curr:
            return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)