import math

total={}
def insert(items):
    if items in total:
        total[items] += 1
    else:
        total[items] = 1
insert('Apple')
insert('Ball')
insert('Apple')
print (len(total))
str1="6/4"

print("str1")
a = {}
a[1] = 1
a['1'] = 3
a[1]=a[1]+1
count = 0
for i in a:
    count += a[i]
print(count)
list1=[1,3,4,2]

x=list1.pop(3)

print(set([x]))

def f1():
    x=100
    x=x+2
    print(x)
x=+1
f1()
import collections
a=collections.Counter([1,1,2,3,3,4,4,4])
print(a)
m = [[x, y] for x in range(0, 1) for y in range(0, 4)]
print(len(m))
print(9//2)
p=1
print(math.e ** p)
set1={2,5,3}

set2={3,1}

set3={}

set3=set1&set2

print(set3)

set1={2,3,4,5}
set1=set1+{7}





print(chr(ord('a')+1))