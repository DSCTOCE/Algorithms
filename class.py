class Number():
    even=0 #Default value
    def check(self,num):
        if num%2==0:
            self.even=1

    def even_odd(self,num):
        self.check(num)
        if self.even==1:
            print('It is even8')

        else:
            print("It is odd")

n=Number()
n.even_odd(20)
