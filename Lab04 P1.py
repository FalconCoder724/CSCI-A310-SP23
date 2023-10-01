def largestIn(tree):
    if tree.right == None:
        return tree.key
    else:
        return largestIn(tree.right)

        
class BstNode:

    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.curr = self

    def insert(self, key):
        if self.key == key:
            return 
        elif self.key < key:
            if self.right is None:
                self.right = BstNode(key)
            else:
                self.right.insert(key)
        else: # self.key > key
            if self.left is None:
                self.left = BstNode(key)
            else:
                self.left.insert(key)
                   
    def remove(self, value):
        if self.key == value:
            if self.left == None:
                k = self.right
                self = k
                print(k)
                return self
            else:
                a = largestIn(self.left)
                self.key = a
                self.left.key = None
                print(str(a) + ' the largest key in left sub tree')
                #return self.left.remove(a)
        elif self.key > value: 
            # I assume the key can be found in left tree
            return self.left.remove(value)
            
        else: 
            # Check Right tree
            return self.right.remove(value)
        
  
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

def largestIn(tree):
    if tree.right == None:
        m = tree.key
        tree.curr=None
        return m
    else:
        return largestIn(tree.right)

import random

b = BstNode(50)


"""""""""""""""""
for _ in range(10):
    number = random.randint(0, 100)
    print("Inserting", number)
    b.insert(number)
    b.display()
    print("\n------\n")
"""""""""""""""""

b.insert(16)
b.insert(13)
b.insert(25)
b.insert(76)
b.insert(56)
b.insert(21)
b.insert(75)
b.display()
print("before remove")
b.remove(76)
b.display()

