print("Hello World!")

for i in range(1,10):
    print(i)

def evenOdd(n):
    if(n%2==0):
        print("Even")
    else:
        print("Odd")


n=int(input("Enter an integer: "))
evenOdd(n)

def sum(x):
    if(x>0):
        result=x+sum(x-1)
    elif(x<=0):
        result=0
    return result

x=int(input("Enter a number: "))
print(sum(x))