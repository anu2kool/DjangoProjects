n=int(input())
str1=str(n)
lst1=list(str1)
if len(str1)==1:
    print(n)
elif lst1.count('0')==len(lst1)-1:
    n=n-1
    str1=str(n)
    lst1=list(str1)
    prod=1
    for i in lst1:
        prod*=int(i)
    print(prod)    
elif len(lst1)<6:
    l=len(str1)
    str2=""
    for i in range(l-1):
        str2+='9'
    left=int(str2)
    max1=1
    for i in range(left,n+1):
        list1=list(str(i))
        prod=1
        for i in list1:
            if i!='0':
                prod*=int(i)
        if prod>max1:
            max1=prod
    print(max1)
else:
    lst2=[]
    i=len(lst1)-1
    while i>=0:
        if lst1[i]=='9':
            lst2.append(lst1)
        else:
            lst1[i]='9'
            if i-1<0:
                break
            else:
                lst1[i-1]=str(int(lst1[i-1])-1)
                lst2.append(lst1)
        i-=1
    lst2.append(list('9'*(len(lst1)-1)))
    lst2.append(list(str1))
    prod=1
    max1=1
    for j in lst2:
        str2=''
        prod=1
        for s in range(len(j)):
            prod*=int(j[s])
        if prod>max1:
            max1=prod
    print(max1)
    print(lst2)
    