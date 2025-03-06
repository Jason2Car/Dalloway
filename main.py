text=""

with open('Dalloway.txt', encoding='utf8') as file_object:
    text = file_object.read()

for dalloway in text.split():
    print(dalloway)