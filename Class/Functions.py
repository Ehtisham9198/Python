#               Functions
#   A block of code that perform a specific task

def Swap(a,b):
    
        temp =a
        a=b
        b=temp
        return a,b

print(Swap(2,3))

def SUM(n):
        if(n==0): return 0
        else:
           return (n + int(SUM(n-1)))

print(SUM(10))

def Factorial(n):
      if(n==0): return 1
      else:
            return n*Factorial(n-1)

print(Factorial(5))
