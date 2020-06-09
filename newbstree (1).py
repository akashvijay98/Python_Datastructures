#!/usr/bin/env python
# coding: utf-8

# In[15]:


class node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

        
    
class bst:
    
    def __init__(self):
        self.root=None
       
        
    
    
    def insert(self,val):
        if self.root==None:
            self.root=node(val)
        else:
            self._insert(self.root,val)
            
    
    def _insert(self,root,val):
        if val<root.val:
            if root.left==None:
                root.left=node(val)
            else:
                self._insert(root.left,val)
        elif val>root.val:
            if root.right==None:
                root.right=node(val)
            else:
                self._insert(root.right,val)
        elif val==root.val:
            print("node exists in tree")
                    
                    
    def display(self):
        if self.root!=None:
            self.inorder(self.root)
            
        
    def inorder(self,start):
        if start!=None:
            self.inorder(start.left)
            print(start.val)
            self.inorder(start.right)
    
    def maxsum(self):       
        q=[]
        q.append(self.root)
        res=self.root.val
        
        while(len(q)!=0):
       
            count=len(q)
            sum=0
        
            while(count>0):
                count-=1
                temp=q[count]
                
                q.remove(q[count])
                
                sum=sum+temp.val
                
                
                if temp.left!=None:
                    q.append(temp.left)
        
                    
                if temp.right!=None:
                    q.append(temp.right)
            
                
                
        
            
            res=max(res,sum)
            
        return res
                
                
                
            
            
            
            
            
        
        
        
                      
                    
n=bst()

n.insert(2)
n.insert(3)
n.insert(1)
n.insert(4)
n.insert(5)
n.insert(8)
n.insert(7)
n.insert(9)
n.display()
n.maxsum()

                    
            
            
    
    

        


# In[ ]:





# In[12]:





# In[ ]:




