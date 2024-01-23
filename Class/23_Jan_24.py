                
'''
    LIST
Mutable sequence
in {} or []

'''

list = [1,2,3]
list  = ["Hi","How","are",1,2,7.8]
print(list)
print(len(list))

hi = [1,2,3,4,5]
print(hi)

hello = list+hi  #concatenate
print(hello)

list = ["OKAY"]+hi
list = hi+["OKAY"]
print(list)

print(list*2)  #Doubled the list

        # Methods
# Append

my =["kya","hua"]
name = my.append("Bhai")
print(my)

# POP , remove last entered element
my.pop(0)  #removed first element
my.pop(1)  #removed second element
print(my)

# Reverse
list1 = ['a','b','c','d','e']
list1.reverse()
print(list1)

# Sorting
list2 =[3,4,1,2,6,7,-1]
list2.sort()
print(list2)
# Multiple data types can't be sort in a list, there should be only one data type elements for to apply sorting


# Nesting a list
list_1 =[1,2,3]
list_2 =[4,5,6]
list_3 =[7,8,9]
matrix = [list_1,list_2,list_3]
print(matrix)

# List comprehension
#  print zeroth column element
first_col = [row[0] for row in matrix]
print(first_col)
