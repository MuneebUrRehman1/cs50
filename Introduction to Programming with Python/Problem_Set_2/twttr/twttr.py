vowels = "aeiou"
str = input("Input: ")
for s in str:
    if(s.lower() in vowels):
        str = str.replace(s,"")
print("Output:", str)