# def Fibo(n):
#     if(n<=1): return n
#     else: return Fibo(n-1) + Fibo(n-2)

# print(Fibo(5))

# def Binery_Search(list,target,l,u):
#     if(l>u): return -1
#     mid = (l+u)//2
#     if(list[mid]==target):
#         return mid
#     elif(list[mid]>target):
#         return Binery_Search(list,target,l,mid-1,)
#     else:
#         return Binery_Search(list,target,mid+1,u)
# list = [1,2,3,4,5,8,9]
# print(Binery_Search(list,5,0,len(list)-1))

# def Power(a,b):
#     if(b==0): return 1
#     else: return a*Power(a,b-1)
# print(Power(2,4))

# def String_rev(str):
#     if(len(str)==0): return str
#     else:
#         return String_rev(str[1:])+str[0]
    
# input_string = "Hello, World!"
# reversed_string = String_rev(input_string)
# print(reversed_string)

# def Swapped_keys_val(dic):
#     swapped={}
#     for key,value in dic.items():
#         swapped[value] = key
#     return swapped

# dic = {"my":1, "name":"2"}
# print(Swapped_keys_val(dic))
    
# def Remove_duplicate(list):
#    list.sort()
#    list1=[]
#    for i in range(len(list)):
#         if list[i] != list[i-1]:
#             list1.append(list[i])
#    return list1
# list = [1,2,2,3,4,4,5,6,7]
# print(Remove_duplicate(list))


# def Remove_duplicate(lst):
#     new_lst = set(lst)
#     lst = list(new_lst)
#     return lst

# lst = [1, 2, 2, 3, 4, 4, 5, 6, 7]
# print(Remove_duplicate(lst))

# a set cannot have duplicate values
# def Sort_Name(list):
#     for i in range(0,len(list)):
#         for j in range(i+1,len(list)):
#             if list[i]>list[j]:
#                 list [i],list[j] = list[j],list[i]
#     return list

# list = ["hi","am","i","name"]
# print(Sort_Name(list))

# def gcd(a,b):
#     if(b==0): return a
#     else: return gcd(b,a%b)

def Transpose(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = mat[j][i]
    return mat

def Transpose(mat):
    Transposed =[]
    for i in range(len(mat[0])):
        Transpose_row =[]
        for j in range(len(mat)):
            Transpose_row.append(mat[j][i])
        Transposed.append(Transpose_row)
    return Transpose

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(Transpose(mat))

