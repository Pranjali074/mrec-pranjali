a=[1,3,4,7,6,5]
first=second=a[0]
for i in range(len(a)):
    if(a[i]>first):
        second=first
        first=a[i]
    elif(a[i]>second and a[i]<first):    
        second=a[i]
print(second,first)        