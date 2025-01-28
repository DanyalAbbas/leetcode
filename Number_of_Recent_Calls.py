class RecentCounter:

    def __init__(self):
        self.requests = []
        

    def ping(self, t: int) -> int:
        count = 0
        self.requests.append(t)
        for i in self.requests:
            if i >= (t-3000) and i <= t:
                count += 1
        return count
    

r1 = RecentCounter()
print(r1.ping(1))
print(r1.ping(2))
print(r1.ping(3001))
print(r1.ping(3002))


