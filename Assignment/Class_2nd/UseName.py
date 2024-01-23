# WAP that takes a user fullname as input an print the initials in UPPER case followed by the lastname in lower case

full_name = input("Enter your full name = ")
name = full_name.split()
first = ''
last_num=len(name)
for i in name[:last_num-1]:
    first = first + i[0].upper() + '. '
second = name[last_num-1].lower()
answer = first + second
print(answer)

