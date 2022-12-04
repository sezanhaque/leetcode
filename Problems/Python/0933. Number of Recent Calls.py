from collections import deque

class RecentCounter:
    def __init__(self):
        self.requests = deque()
        self.range = [0, 0]

    def ping(self, t: int) -> int:
        limit = 3000
        self.range[0], self.range[1] = t - limit, t
        self.requests.append(t)
        while self.range[0] > self.requests[0]:
            self.requests.popleft()

        return len(self.requests)

class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()

        self.requests.append(t)
        
        return len(self.requests)

# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
obj.ping(1)
obj.ping(100)
obj.ping(3001)
obj.ping(3002)
# param_1 = obj.ping(t)
