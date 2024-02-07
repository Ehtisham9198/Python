'''
1-Implement a fun that check weheter a given string isn pallindrome is or not?
'''
def pallindrome(str):
        str = str.replace(" ", "").lower()
        str = str.replace('!', "")
        if(str==str[::-1]):
          print("YES\n")
        else:
           print("NO")


str = input("Enter the string:- ")
pallindrome(str)