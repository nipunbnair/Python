def average(a, b, c):
    avg = (a + b + c) / 3
    return avg


a = int(input('Enter no 1'))
b = int(input('Enter no 2'))
c = int(input('Enter no 3'))
avg = average(a, b, c)
print(round(avg))
