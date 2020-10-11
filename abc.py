class ABC():
    class_variable=0
    def __init__(self,var):
        ABC.class_variable+=1
        self.var=var
        print("The object values:",var)
        print("The value of the class variable:",ABC.class_variable)
obj1=ABC(100)
obj2=ABC(200)
obj3=ABC(300)
