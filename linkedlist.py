#!/usr/bin/env python
# coding: utf-8

# In[1]:


class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    
    def __init__(self):
        self.head=None
    
    def insert(self,value):
        newnode=node(value)
        if self.head==None:
            self.head=newnode
            return
        l=self.head
        while(l.next):
            l=l.next
        l.next=newnode
    
    def printv(self):
        a=[]
        printval=self.head
        while(printval is not None):
            a.append(printval.data)
            print(printval.data)
            printval=printval.next
            
        return a
    
    def cycle(self):
        p1=p2=self.head
        
        while(p2!=None and p2.next!=None):
            p1=p1.next
            p2=p2.next.next
            
            if(p1==p2):
                return True
            
            
        
            
        return False
 
        
            

    
        
l=linkedlist()
l.head=node(0)
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
l.printv()

l.cycle()




# In[ ]:




