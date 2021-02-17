
class Stack:
    def __init__(self):
        self.items=[]
    
    def print_elements(self):
        elem = []
        for i in range(len(self.items)):
            elem.append(self.items[i])
        print(elem)
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, items):
        self.items.append(items)
    
    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[-1]
        
    
####### TESTS AREA #######

#s=Stack()

#print(s.isEmpty())
#s.push(4)
#s.push('dog')
#print(s.peek())
#s.push(True)
#print(s.size())
#print(s.isEmpty())
#s.push(8.4)
#s.print_elements()
#print(s.pop())
#print(s.pop())
#print(s.size())
