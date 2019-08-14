#Basic binary tree. 
#Inspired from Gayle Lakman's tree implementation in java.

class treeNode:
#Node gets intialized with siblings and a value
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
#assigns a new node to the left of parent node
    def assign_left(self, newLeftNode):
        self.left = newLeftNode;
#assigns a new node to the right of parent node    
    def assign_right(self, newRightNode):
      self.right = newRightNode;
#inserts the value, starting from the root node. This is a recursive method that recurses until it finds a leaf node.    
    def insert(self,value):
      if value <= self.data:
        if self.left == None:
          self.left = treeNode(value)
        else:
          self.left.insert(value)
      else:
          if self.right == None:
            self.right = treeNode(value)
          else:
              self.right.insert(value)  
  #finds whether the tree contains a specific value. This is also a recursive method.  
    
    def contains(self, value):
      if self.data == value: 
        # print("True")
        return True
      if value < self.data:          #goes to the left
        if self.left == None: 
          # print("False")
          return False
        else:
          return self.left.contains(value)
      else:                         #goes to the right
        if self.right == None: 
          # print "False"
          return False
        else:
          return self.right.contains(value)
    
    def inOrderTraversal(self):   
       #traverses in this form: left-->root/parent-->right
      if self.left!=None:
        self.left.inOrderTraversal()
      print self.data
      if self.right!=None:
        self.right.inOrderTraversal()
   
     #traverses in this form: root/parent-->left-->right
    def preOrderTraversal(self):
     print self.data
     if self.left!=None:
       self.left.preOrderTraversal()
     if self.right!=None:
       self.right.preOrderTraversal()
    
     #traverses in this form: left-->right-->root/parent
    def postOrderTraversal(self):
      if self.left!=None:
       self.left.postOrderTraversal()
      if self.right!=None:
       self.right.postOrderTraversal()
      
      print self.data
    
     #deletes the node that contains the input value
    def delete(self,value):
      if self.data == value:
        self.data = None
        return True
      if value < self.data:
        if self.left==None:
          return False
        else:
            return self.left.delete(value)
      else:
        if self.right == None: 
          # print "False"
          return False
        else:
          return self.right.delete(value)      

    


# root = treeNode(10)
# #initiating first level nodes
# newLeft = treeNode(8)
# newRight = treeNode(7)

# #assinging first level nodes
# root.assign_left(newLeft)
# root.assign_right(newRight)

# #initiating second level nodes
# secondLeft = treeNode(6)
# secondRight = treeNode(5)

# #assinging second level nodes
# newLeft.assign_left(secondLeft)
# secondLeft.assign_right(secondRight)



#Improvised binary tree with all the operations
#first implement add function to a binary tree that adds node upon #the invocation of "add". bt.add(5). if current == null current = new TreeNode(value). bt.add(4); if current.left.data == null && current.left.data < current.left.val    ==> /...


root = treeNode(10)
root.insert(5)
root.insert(15)
root.insert(8)
root.insert(4)
# first = root.left
# print first.right.data
# print(root.contains(5))
# print(root.preOrderTraversal())
print(root.delete(5)) 
print(root.inOrderTraversal())
print(root.delete(8))
print(root.inOrderTraversal())