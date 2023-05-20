from node import Node

'''
methods class Stack:
push(): this method takes in a value and adds it to the top of the stack. 
It will print the message “All out of space!” if the stack has no room.
pop(): this method removes the top value in the stack if there are existing values. 
If there are no values, it will print the message “All out of space!”.
peek(): this method returns the top value in the stack if there are existing values. 
If there are no values, it will print the message “This stack is totally empty.”.
is_empty(): this method checks to see if the stack is empty and will return True or False if it is not.
'''
 
class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
 
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
    else:
      print("All out of space!")
 
  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This stack is totally empty.")
 
  def peek(self):
    if self.size > 0:
      return self.top_item.get_value()
    else:
      print("Nothing to see here!")
 
 
  def is_empty(self):
    return self.size == 0

