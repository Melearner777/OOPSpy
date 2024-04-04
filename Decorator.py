import functools
def decor(func):
    @functools.wraps(func)

    def inner():
     print('hello guys,welcome to all')
     func()
    return inner 

@decor 
def first():
     '''
     Hello sir
     '''
     print('I am first function')

@decor 
def second():
   print('I am second function')

#first=decor(first)
first()
print(first.__name__)
print(first.__doc__)

#second=decor(second)
second()



