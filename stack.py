class Stack:
   """Stack Obyekt"""
   def __init__(self):
      self.stack = []
      
   def isEmpty(self):
      return len(self.stack) == 0
   
   def push(self, data):
      self.stack.append(data)
      return True
   
   def pop(self):
      if self.isEmpty():
         return 'Stack is empty'
      else:
         return self.stack.pop()
      
   def peek(self):
      if self.isEmpty():
         return 'Stack is empty'
      else:
         return self.stack[-1]
      
