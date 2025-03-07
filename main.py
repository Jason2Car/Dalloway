text=""

with open('Dalloway.txt', encoding='utf8') as file_object:
    text = file_object.read()

text = text.split()
name = 0;
title = 0;
for index in range(len(text)-1):
    if text[index] == "Mrs." and text[index+1] == "Dalloway":
        title+=1
    elif text[index] == "Clarissa":
        name+=1
print("Mrs. Dalloway mentioned: "+str(title))
print("Clarissa mentioned: "+ str(name))