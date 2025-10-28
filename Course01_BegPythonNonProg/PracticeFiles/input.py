your_name = input("Your name: ")

print(your_name.upper())


#Challenge:
#First ask for some text, then prompt
#"Enter 1 to uppercase and 2 to lowercase"
#and then either upper or lower case it

text_prompt = input("Provide text: ")
casing = int(input("Enter 1 for uppercase or 2 for lowercase"))

if casing == 1:
    print(text_prompt.upper())
elif casing == 2:
    print(text_prompt.lower())
else:
    print(text_prompt)