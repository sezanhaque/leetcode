class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class BrowserHistory:
    """
    Implemented using doubly linked list
    """

    def __init__(self, homepage: str):
        self.curr_page = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.curr_page.next = self.curr_page = ListNode(url, self.curr_page)

    def back(self, steps: int) -> str:
        while self.curr_page.prev and steps > 0:
            self.curr_page = self.curr_page.prev
            steps -= 1

        return self.curr_page.val

    def forward(self, steps: int) -> str:
        while self.curr_page.next and steps > 0:
            self.curr_page = self.curr_page.next
            steps -= 1

        return self.curr_page.val


class BrowserHistory:
    """
    Implemented using list
    """

    def __init__(self, homepage: str):
        self.curr_idx = 0
        self.len = 1
        self.history = [homepage]

    def visit(self, url: str) -> None:
        if len(self.history) < self.curr_idx + 2:
            self.history.append(url)
        else:
            self.history[self.curr_idx + 1] = url

        self.curr_idx += 1
        self.len = self.curr_idx + 1

    def back(self, steps: int) -> str:
        self.curr_idx = max(self.curr_idx - steps, 0)
        return self.history[self.curr_idx]

    def forward(self, steps: int) -> str:
        self.curr_idx = min(self.curr_idx + steps, self.len - 1)
        return self.history[self.curr_idx]
