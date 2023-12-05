def decor(fx):
        def mfx(*args,**kwargs):
                print('Good Morning\n\n')
                fx(*args,**kwargs)
                print('\nThank You for using CODE 37')
        mfx()        
#@decor      
class employee:
        def __init__(self,n,id,mn):
                self.name=n
                self.id=id
                self.mobno=mn
        def __str__(self):
                return (f'Employee Name {self.name}\nEmployee ID {self.id}\nMobile No. {self.mobno}')
decor(employee)('Siddhant Deshwal',14940,8800693196)