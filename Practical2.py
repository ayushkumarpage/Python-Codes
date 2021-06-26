num=int(input("enter a no.:"))
mod=num%2
if num==0 or num<0:
    print("enter no greater thasn zero:")
else:
    if mod>0:
        print("This is an odd number")
    else:
        print("This is and even number")
