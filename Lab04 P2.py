class BinarySearchTree(object): # A binary search tree class

    def __init__(self): 
        # The tree organizes nodes by their keys. Initially, it is empty.
        self.__root = None
    class __Node(object): 
        def __init__(self): 
            self.__root = None

        def __init__(self,key,data, left=None, right=None):
            self.key = key 
            self.data = data 
            self.leftChild = left 
            self.rightChild = right

        def __str__(self):
            return "{" + str(self.key) + ", " + str(self.data) + "}"    

        def isEmpty(self):
            return self.__root is None
        
        def root(self):
            if self.isEmpty():
                raise Exception("No root node in empty tree")
            return (self.__root.data, self.__root.key)


    def __find(self, goal): 
        current = self.__root 
        parent = self
        while (current and goal != current.key): 
            parent = current 
            current = (current.leftChild if goal < current.key else current.rightChild)
        return (current, parent)

    def search(self, goal): 
        node, p = self.__find(goal) 
        return node.data if node else None 

    def insert(self, key, data):
        node, parent = self.__find(key) 
        if node:
            node.data = data
            return False
        if parent is self:
            self.__root = self.__Node(key, data)
        elif key < parent.key: 
            parent.leftChild = self.__Node(key, data, right=node) 
        else:
            parent.rightChild = self.__Node( key, data, right=node)
        return True
    
    def inOrderTraverse(self, function=print):
        self.__inOrderTraverse(self.__root, function=function)
    def __inOrderTraverse(self, node, function):
        if node: 
            self.__inOrderTraverse(node.leftChild, function) 
            function(node) 
            self.__inOrderTraverse(node.rightChild, function)
    
    def traverse_rec(self, traverseType="in"):
        if traverseType in ['pre', 'in', 'post']:
            return self.__traverse( self.__root, traverseType)
        raise ValueError("Unknown traversal type: " + str(traverseType))
    
    def minNode(self): # Find and return node with minimum key 
        if self.isEmpty(): # If the tree is empty, raise exception
            raise Exception("No minimum node in empty tree")
        node = self.__root 
        while node.leftChild:
            node = node.leftChild
        return (node.key, node.data)

    def delete(self, goal): # Delete a node whose key matches goal node, parent = self.__find(goal) # Find goal and its parent
        node, parent = self.__find(goal)
        if parent is self:
            self.__root = node.leftChild # update root
    
    def __delete(self,parent, node):
        deleted = node.data 
        if node.leftChild:
            if node.rightChild:
                self.__promote_successor(node)

            else:
                if parent is self:
                    self.__root = node.leftChild # update root
                elif parent.leftChild is node: # If node is parent's left, parent.
                    parent.leftChild = node.leftChild # child, update left
                else: # else update right child parent.
                    parent.rightChild = node.leftChild 
        else:
            if parent is self:
                self.__root = node.rightChild
            elif parent.leftChild is node:
                parent.leftChild = node.rightChild 
            else:
                parent.rightChild = node.rightChild
        return deleted
    
    def __promote_successor( self,node):
        successor = node.rightChild 
        parent = node
        while successor.leftChild:
            parent = successor
            successor = successor.leftChild 
            node.key = successor.key # node.data = successor.data # 
            self.__delete(parent, successor)


  