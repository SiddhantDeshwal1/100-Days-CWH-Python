from functools import reduce
l=[1,2,3,4,5,6]

def test(l):
    print(l+1)#print aur return me farak
    return (l+1)

a=map(lambda a:a+1,l)#lambda me bhi chalakar dekhle
print(list(a))

def filterfunction(a):
    return a>2
print(list(filter(filterfunction,l)))

print(reduce(lambda a,b:a*b,l))#do values ek sath lega