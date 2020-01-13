class MyQueue(object):
    qu = []
    def __init__(self):
        qu = []
    
    def peek(self):
        return self.qu[0]

        
        
    def pop(self):
        rev_q = reversed(self.qu)
        rev_q = list(rev_q)
        val = rev_q.pop()
        self.qu = list(reversed(rev_q))
        return val
        
        
    def put(self, value):
        self.qu.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())


