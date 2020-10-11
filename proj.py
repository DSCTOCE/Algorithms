#Write a program that uses class to stor the marks of the person.
class Student:
    def __init__(self,name):
        self.name=name
        self.marks=[]
    def enterMarkd(self):
        for i in range(3):
            m=int(input("Enter the marks of %s in the subject %d:" %(self.name)))
            self.marks.append(m)

    def display(self):
        print(self.name,"got",self.marks)


s1=Student("Poorna")
s1.enterMarkd()
s2=Student("Aishwarya")
s2.enterMarkd()
