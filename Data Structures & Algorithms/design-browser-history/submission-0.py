class ListNode:
    def __init__(self, val='', next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = ListNode(homepage)

    def visit(self, url: str) -> None:
        new_node = ListNode(val=url, prev=self.history)
        self.history.next = new_node
        self.history = new_node
        

    def back(self, steps: int) -> str:
        while steps > 0 and self.history.prev:
            self.history = self.history.prev
            steps -= 1
        return self.history.val
        

    def forward(self, steps: int) -> str:
        while steps > 0 and self.history.next:
            self.history = self.history.next
            steps -= 1
        return self.history.val
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)