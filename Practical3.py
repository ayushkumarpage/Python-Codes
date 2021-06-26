num=int(input("enter a interger: "))
a,b=0,1
if num<=0:
    print("Enter a positive Interger")
elif num==1:
    print("Fibnonacci sequence upto %s is %s"%(num,a))
else:
    i=3
    print("Fibnonacci sequence upto %s is"%(num))
    print(a)
    print(b)
    while i<=num:
        c=a+b
        print(c)
        a=b
        b=c
        i+=1
        num=int(input("enter a no : "))
