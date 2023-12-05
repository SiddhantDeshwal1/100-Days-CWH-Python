def links(fx):
    def mfx(*args,**kwargs):
        fx(*args,**kwargs)
        print('Follow for more :-\n\ninstagram-deshwalsiddhant\nYoutube-CodewithSiddu')
    return mfx

@links
class person:
    def __init__(self,n,o):
        self.name=n
        self.occ=o
        print(f'My name is {self.name} and i am a {self.occ} developer')

a=links(person)('Siddhant','HR')


