a=['h','a','r','s','h','i','t']
num=['1','2','3','4','5','6','7','8','9','0']
sym=['!','@','#','$','%','&']

a1=int(input('no. of alphabets: '))
number= int(input('no. of numbers: '))
symbol=int(input('no. of symbols: '))

import random
list=[]
for alphabet in range(1,a1+1):
    n=a[random.randint(1,6)]
    list.append(n)
for nu in range(1,number+1):
    n=num[random.randint(1,9)]
    list.append(n)
for s in range(1, symbol+1):
    n=sym[random.randint(1,5)]
    list.append(n)
list_1=[]
for i in range(1,len(list)):
    n=list[random.randint(1,len(list)-1)]
    list_1.append(n)
for j in list_1:
    print(j, end='')
    