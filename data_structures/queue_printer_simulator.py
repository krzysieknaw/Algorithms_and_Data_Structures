from queue_implementation import Queue
import random

print_queue = Queue()

class printer():
    def __init__(self):
        self.cuerrent_task = None
        #not end
        
    def busy(self):
        if self.current_task == None:
            return True
        else:
            return False
        
