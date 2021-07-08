'''print('hello world')
temp=eval(input('enter val :- '))
print(temp)
print(temp+3456789)

print('hell',end='  ')
print('is',end='  ')
print('near')

x,y=input('enter values ').split()
print(int(x)+int(y))

temp=float(input('enter temperature in celcius :-'))
print('in farahite :- ',9/5+temp+32)
temp1=eval(input('enter temp in farahite :- '))
print('In Celcius :-',temp1-9/5-32)

for i in range(5):
    print(i*5)
for i in range(3*2):
    print(i)

for i in range(1,6):
    print('*'*i,end='\n')

k=5-1
for i in range(1,6):
    for j in range(k):
        print(' ',end='')
    k=k-1
    for j in range(0,i):
        print('*',end='')
    print()


def printp(n):
    k=n*2-1
    for i in range(0,n+1):
        for j in range(k):
            print(end=' ')
        k=k-1
        for j in range(i):
            print('* ',end='')
        print()
print(printp(10))

n= eval(input('enter values :-'))
for i in range(n+1):
    for j in range(i):
        print(i,end='')
    print()

n=5
for i in range(1,n+1):
    for j in range(i,n+1):
        print(i,end='')
    print()

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print()

n=5
for i in range(1,n+1):
    for j in range(n,0,-1):
        print(n,end='')
    n=n-1
    print()

a=list(map(int,input('enter the number ').split()))
print(a)
a=input('enter string :-')
for i in (len(a)):
    print(i)
print(list(a.split('')))

a= input()
l=[]
for i in (a):
    print(i)
    l.append(i)
print(l)
print(list(a.split(' ')))

k=list(a.split(' '))
print(a.replace('o','#'))

a= int(input())
if(a % 4 == 0 and (a % 100 != 0 or a % 400 == 0)):
    print(a,'is leap year')
else:
    print(a,'is not a leap year ')'''

