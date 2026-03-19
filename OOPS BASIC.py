class student:
    dept="CSE"
    def set_dim(self,name,marks):
        self.name=name
        self.marks=marks
        self.p=0
    def per(self):
        self.p=sum(self.marks)//3
    
    def display(self):
        self.per()
        print("1.NAME:",self.name)
        print("2.SCORE:",self.p)
        print("3.DEPARTMENT:",student.dept)
uday=student()
indra=student()
thiru=student()
uday.set_dim("UK",[40,50,60])
indra.set_dim("JITH",[45,55,65])
thiru.set_dim("TK",[30,60,89])

uday.display()
indra.display()
thiru.display()