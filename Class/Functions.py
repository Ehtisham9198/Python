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


def Even(list):
      for item in list:
            if (item%2==0):
              return True
       
      return False

list = [7,0,3,5,9]
print(Even(list))

def Even(list,l):
      for item in list:
            if (item%2==0):
              l.append(item)
       
      return l

list = [7,0,3,4,8,5,9]
l=[]
print(Even(list,l))



