#String formating
'''
1- The oldest method involves olcase holder include modulo character
2- Dot formate string method
3- Formated string litetral call F-String(py-3.6)

'''

print("I'm going to inject %s here" %'something') #invalid syntax


print("Im going to inject %s text here, and %s text here" %('some','here'))

print("I'm %s , and I study in %s" %('EHTISHAM','IIIT BBSR'))
x,y ="EHTISHAM","IIIT BBSR"
print("I'm %s and I study in %s" %(x,y))

'''
repr( function)
 it returns a printable representaion of an object in python it means in python repr(function) return a prentable representation 
of an object by converting the object into a string

'''

num = [1,2,3,4,5]
print_num = repr(num)
print(print_num)

print("My name is %s" %"Ehtisham")
print("My name is %r"%"Ehtisham")

print("My name is %s "% 'Mohd \Ehtisham')
print("My name is %r "% "Mohd\Ehtisham")
 # %d for injected integer

print('Floating point number: %10.2f' %(12.144)) # 10 - No_of_digit = no of spaces
"""
--floating point numbers use the formate %5.2f, here 5 would be the minimum number of characters that a string should contains, this may be 
padded with wode spaces if the entire number does not have rhis many digits

.2f stands for how many number to show pass the decimal points 
"""

