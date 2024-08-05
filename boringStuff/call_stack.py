def a():
    print('a() starts') #1
    b() 
    d()
    print('a() returns') #8

def b():
    print('b() starts') #2
    c() 
    print('b() returns') #5

def c():
    print('c() starts') #3
    print('c() returns') #4

def d():
    print('d() starts') #6
    print('d() returns') #7

a()