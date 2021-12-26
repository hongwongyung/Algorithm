class stack : 

     def __init__(self):
          self.stk = []
     
     def push(self, item):
          self.stk.append(item)
     
     def pop(self):
          if self.stk == 0:
               raise Exception(-1)
          return self.stk.pop()
     

     def is_empty(self):
          if self.stk == []:
               return 1
          else :
               return 0
     
     def top(self):
          return self.stk[-1]

     def size(self):
          return len(self.stk)
s = stack()
s.push(1)
s.push(2)
print(s.top())
print(s.size())
print(s.is_empty())
print(s.pop())
print(s.pop())
print(s.pop())
