#!/usr/bin/env python
# coding: utf-8

# In[20]:


class node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None
        

        
        
class Bst():
    def __init__(self):
        self.head=None
       
       
    
        
     
    def insert(self,data):
        if self.head==None:
            self.head=node(data)
         
         
            
        else:
            self._insert(data,self.head)
        
    def _insert(self,data,currnode):
        if data <currnode.data:
            if currnode.left==None:
                currnode.left=node(data)
              
                
                
            else:
                self._insert(data,self.currnode.left)
                
        elif data>currnode.data:
            if currnode.right==None:
                currnode.right=node(data)
                
                
            else:
                self._insert(data,self.currnode.right)
        
        elif(data==currnode.data):
            print("node already exists")
            
   
  
        
            
            
    def display(self):
        if self.head!=None:
            self.inorder(self.head)
            
    def inorder(self,currnode):
        if currnode!=None:
            self.inorder(currnode.left)
            
            print(currnode.data)
            
           
            
            self.inorder(currnode.right)
        
        
        
        
    
 
            
            
b=Bst()

b.insert(1)
b.insert(0)
b.insert(2)

b.display()
            


# In[ ]:





# In[ ]:




