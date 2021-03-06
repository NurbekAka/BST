#from future import print_function
#from logger_decor import myDecorator

def myDecorator(func):
    def wrapper(*args, **kwargs):
        print('Calling {}{}{}'.format(func.__name__, args, kwargs))
        w = func(*args, **kwargs)
        print('Finished {}'.format(func.__name__),w)
    return wrapper
@myDecorator
def testFunc(a, b=1, *args, **kwargs):
    print("argument a: ", a)
    print("argument b: ", b)
    print("argument args: ", args)
    print("argument kwargs: ", kwargs)

    return a + b

testFunc(2, 3, 4, 5, c=6, d=7)
print()
testFunc(2, c=5, d=6)
print()
testFunc(10)
