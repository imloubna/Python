class abc:
    def set_dim(self,a,b):
        self.n1=a 
        self.n2=b 
    def calc(self):
        self.set_dim(20,30)
        print(self.n1+self.n2)
x=abc()
y=abc()
x.set_dim(20,30)
x.calc()
y.set_dim(90,100)
y.calc()
