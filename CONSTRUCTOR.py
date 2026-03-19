class Rect:
    def __init__(self,a,b):
        self.l=a 
        self.b=b 
    def display(self):
        print(self.l*self.b)
        
a=Rect(20,30)
b=Rect(30,40)
a.display()
b.display()