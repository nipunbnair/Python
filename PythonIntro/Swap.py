def swap(x, y):
    temp = x
    x = y
    y = temp
    return x, y


x = input('Enter value of x')
y = input('Enter the value of y')
print('the values of x and y are:')
print(x)
print(y)
x, y = swap(x, y)
print('the swapped values')
print(x)
print(y)
