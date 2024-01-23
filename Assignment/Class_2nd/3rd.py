sentence = input("Enter the sentence = ")
list = sentence.split()
new_sentence = ''
for i in list[::-1]:
    new_sentence = new_sentence + i[0].upper() + i[1:] + ' '
print(new_sentence)
