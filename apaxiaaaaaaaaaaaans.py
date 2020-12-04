#Apaxiaaaaaaaaaaaans

inplist = list(input())
result = ""
for letter in inplist:
    if not result.endswith(letter):
        result += letter
print(result)
