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