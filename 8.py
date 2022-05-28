def func():
    global x
    x=50
    print('x is', x)
    x = 2
    print('Changed global x to', x)
func()
print('Value of x is', x)
