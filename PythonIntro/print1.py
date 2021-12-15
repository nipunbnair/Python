print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*')
print(1, 2, 3, 4, sep='*', end='#')
x = 5
y = 10
print('The value of x is {} and y is {}'.format(x, y))
print('I love {0} and {1}'.format('bread', 'butter'))
print('I love {1} and {0}'.format('bread', 'butter'))
print('Hello {name},{greeting}'.format(greeting='Good Morning', name='Nipun'))
a = '''Nipun'''
b = '60'
c = "9.89"
print(a, b, c)
d = 15
e = 4
print('x+y', d + e)
print('x-y', d - e)
print('x*y', d * e)
print('x/y', d / e)
print('x//y', d // e)  # Quotient
print('x**y', d ** e)  # To the power of x^y
print('x%y', d % e)  # Remainder
print('x>y', d > e)
print('x<y', d < e)
print('x==y', d == e)
print('x!=y', d != e)
print('x>=y', d >= e)
print('x<=y', d <= e)
f = True
g = False

print('x&&y', f and g)
print('x||y', f or g)
print('!x', not f)
x1 = 2
y1 = 2
x2 = "Hello"
y2 = "Hello"
x3 = [1, 2, 3]
y3 = [1, 2, 3]
print(x1 is y1)
print(x2 is not y2)
print(x3 is y3)
