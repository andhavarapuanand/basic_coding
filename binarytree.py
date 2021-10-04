#binary search tree insertion
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def insertion(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    def print(self):
        if self.left:
            self.left.print()
        print(self.data)
        if self.right:
            self.right.print()
        
    def inorder(self,root):
        r=[]
        if root is not None:
            r=self.inorder(root.left)
            r.append(root.data)
            r=r+self.inorder(root.right)
        print(r)

n=int(input())
l=list(map(int,input().split()))
root=Node(l[0])
for i in range(1,n):
    root.insertion(l[i])
root.print()
root.inorder(root)    
