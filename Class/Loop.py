# COMARISION OPERATORS

2+2
2==2
2==4
2!=4
2!=2
2<0

# CHAINNED COMAPARISION OPEARTOR
1<3<4
1<2 and 3>2 #True
1<2 or 3<2  #True
# Note - python is checking both instance of comparision

            #H W 
#Which operator has more priority in chain comparision?

            #LOOP
x = False

if(x):
    print(2+3)
    print("Ehtisham")  
elif(4<5 or 3<5):
    print(-1)
    print("ijfid")
else:
    print("CE")
 # For loop act as iterator in pytrhon it goes through    
for i in range(1,3):
    print(i)

l =[1,2,3,4,"he"]
for num in l:
    print(num)

for i in ["hi","hello"]:
    print(i)

for i in ["hi","hello","hiok"]:
    print(i+" Ehtisham")


for num in [1,2,3,4,5,6,7,8,9]:
    if(num%2==0):
        print(num," is Even",end = " : ")

print()
sum =0
for num in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum+num

print("Sum of the 10 numbers is",sum,sep = ": ")

# While loop
print()
i =0
while i<5:
    i+=1

x =4
y =0

# When no of iteration is not defined, use while loop

if(x+y==10): print(x+y)
elif(x==y):
    print("Equal")
elif(x==0 and y==0):
    print("Equal to zero")
elif(x!=0 and y==0):
    print("y is equal to zero")
elif(x!=y):
    print("Not Equal")
else:
    print("Aur kitni condition dalega be")



# break
# Continue
# Pass











