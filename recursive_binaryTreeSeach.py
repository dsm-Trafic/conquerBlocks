'''
BINARY SEACH TREE
BASE CASE: 
If the list is empty, return "No Child" to show that there is no node. 

RECURSIVE STEP:
1. Find the middle index of the list.
2. Create a tree node with the value of the middle index.
3. Assign the tree node's left child to a recursive call with the left half of list as input.
4. Assign the tree node's right child to a recursive call with the right half of list as input.
5. Return the tree node.
'''
def build_bst(my_list):
  if len(my_list) == 0:
    return "No Child"

  middle_index = len(my_list) // 2
  middle_value = my_list[middle_index]
  
  print("Middle index: {0}".format(middle_index))
  print("Middle value: {0}".format(middle_value))
  
  tree_node = {"data": middle_value}
  tree_node["left_child"] = build_bst(my_list[ : middle_index])
  tree_node["right_child"] = build_bst(my_list[middle_index + 1 : ])

  return tree_node
  
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

'''
***************************************************************************
Recursive Depth of Binary Search Tree
A binary search tree is a data structure that builds
a sorted input list into two subtrees. The left child of the subtree 
contains a value that is less than the root of the tree. 
The right child of the subtree contains a value that is 
greater than the root of the tree.
A recursive function can be written to determine the depth of this tree.
****************************************************************************
'''
def depth(tree):
  if not tree:
    return 0
  left_depth = depth(tree["left_child"])
  right_depth = depth(tree["right_child"])
  return max(left_depth, right_depth) + 1