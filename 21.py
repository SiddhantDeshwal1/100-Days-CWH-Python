def anything(*a):
    print(type(a))
    print(a)
anything(12345)

def dct(**dic):
    print(dic)

dct(name='Siddhant',sname='Deshwal')