

lst1=[]
lst2=[]
res=[]
n=int(input("Enter the no of test cases:"))

for i in range(0,n):
    case1=int(input())
    lst1.append(case1)


for i in range(0,n):
    case2=int(input())
    lst2.append(case2)


print(lst1)
print(lst2)
alice=0
bob=0
for i in range(0,n):
    if lst1[i]>lst2[i]:
        alice+=1

    elif lst1[i]<lst2[i]:
        bob+=1


print([alice,bob])
