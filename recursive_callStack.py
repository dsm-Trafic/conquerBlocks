'''
Modeling Recursion as Call Stack
One can model recursion as a call stack with execution contexts using a while loop and a Python list.
When the base case is reached, print out the call stack list in a LIFO (last in first out) manner 
until the call stack is empty.
Using another while loop, iterate through the call stack list.
Pop the last item off the list and add it to a variable to store the accumulative result.
Print the result.
'''
def countdown(value):
  call_stack = []
  while value > 0 : 
    call_stack.append({"input":value})
    print("Call Stack:",call_stack)
    value -= 1
  print("Base Case Reached")
  while len(call_stack) != 0:
    print("Popping {} from call stack".format(call_stack.pop()))
    print("Call Stack:",call_stack)
countdown(4)
'''
Call Stack: [{'input': 4}]             
Call Stack: [{'input': 4}, {'input': 3}]         
Call Stack: [{'input': 4}, {'input': 3}, {'input': 2}]     
Call Stack: [{'input': 4}, {'input': 3}, {'input': 2}, {'input': 1}]                                
Base Case Reached                                  
Popping {'input': 1} from call stack                       
Call Stack: [{'input': 4}, {'input': 3}, {'input': 2}]  
Popping {'input': 2} from call stack                   
Call Stack: [{'input': 4}, {'input': 3}]       
Popping {'input': 3} from call stack            
Call Stack: [{'input': 4}]                                 
Popping {'input': 4} from call stack              
Call Stack: []
'''
def countdown(value):
  call_stack = []
  while value > 0 : 
    call_stack.append({"input":value})
    print("Call Stack:",call_stack)
    value -= 1
  print("Base Case Reached")
  while len(call_stack) != 0:
    print("Popping {} from call stack".format(call_stack.pop()))
    print("Call Stack:",call_stack)
countdown(4)
'''
Call Stack: [{'input': 4}]             
Call Stack: [{'input': 4}, {'input': 3}]         
Call Stack: [{'input': 4}, {'input': 3}, {'input': 2}]     
Call Stack: [{'input': 4}, {'input': 3}, {'input': 2}, {'input': 1}]                                
Base Case Reached                                  
Popping {'input': 1} from call stack                       
Call Stack: [{'input': 4}, {'input': 3}, {'input': 2}]  
Popping {'input': 2} from call stack                   
Call Stack: [{'input': 4}, {'input': 3}]       
Popping {'input': 3} from call stack            
Call Stack: [{'input': 4}]                                 
Popping {'input': 4} from call stack              
Call Stack: []
'''