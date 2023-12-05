class testclass():
    def __init__(self,n) -> None:
        self.no=n
    def __str__(self) -> str:
        print(f'The No. is {self.no}')

    @property    
    def tenvalue(self):
        return 10*self.no

    @tenvalue.setter
    def tenvalue(self,nv):
        self.no=nv*10
a=testclass(10)
a.tenvalue=50
print(a.tenvalue)#Fucntion call ke time pe no parantyesis   