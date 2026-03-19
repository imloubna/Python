class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
        
    def insert(self,data):
        Newnode=Node(data)
        if(self.head==None):
            self.head=Newnode
            
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=Newnode
            
    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.data, end="-->")
            temp=temp.next
            

x=Linkedlist()
x.insert(100)
x.insert(200)
x.insert(300)
x.insert(400)
x.insert(500)
x.insert(600)
x.insert(700)
x.insert(800)
x.insert(900)
x.insert(1000)
x.display()

