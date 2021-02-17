class Queue:
    def __init__(self):
        self.items = []
        
    def print_elements(self):
        elem = []
        for i in range(len(self.items)):
            elem.append(self.items[i])
        print(elem)
    
    def enqueue(self, items):
        self.items.insert(0,items)
        
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []
    
    
    
####### TESTS AREA #######
#q=Queue()
	
#q.enqueue(4)
#q.enqueue('dog')
#q.enqueue(True)
#print(q.size())
#q.print_elements()
