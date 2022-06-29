

#  if we pass a function to another function as an input its called a callback function.

def a(fn):
    print('Hello, world!')
    fn()

def b():
    print(' Hello 2')


a(b)