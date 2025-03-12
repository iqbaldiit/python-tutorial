'''
Source: https://www.w3schools.com/python/python_strings.asp
Strings in python are surrounded by either single quotation marks,
or double quotation marks. 'hello' is the same as "hello".
'''
x="hello World"
y='Hello world'

print(x)
print(y)
print(x.upper())
print(y.lower())
print(x.isupper())
print(y.islower())
print(x.capitalize())
print(y.replace("h","W"))
print("Jamal,Kamal,Rahim".split(","))
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

'''
Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string. 
'''
print()
print("======String are arrays======")
x="hello"
print("1st Character of 'Hello World': ",x[0])
print("2st Character of 'Hello World': ",x[1])
print("3st Character of 'Hello World': ",x[2])
print("4st Character of 'Hello World': ",x[3])
print("5st Character of 'Hello World': ",x[4])

print()
print("======Checking String======")
txt = "The best things in life are free!"
print(txt)
print("is 'free' exists in the above sentence :","free" in txt)
print("Yes, 'free' is present" if 'free' in txt else "No, 'free' is not present.")
print("Yes, 'Hello' is present" if 'Hello' in txt else "No, 'Hello' is not present.")

print()
print("======Slicing String======")
txt="Ostrich"
print(txt)
print(f"First 3 character of '{txt}': ",txt[:3])
print(f"Last 3 character of '{txt}': ",txt[-3:])
print(f"3rd to 5th character of '{txt}': ",txt[2:5])

print()
print("======Modify String======")
txt="  ostrICH    "
print(txt)
txt2=txt.strip()
print(f"Remove white space of  '{txt}': ",txt2)
print(f"Upper case of '{txt2}': ",txt2.upper())
print(f"Lower case of '{txt2}': ",txt2.lower())
print(f"Replace W to h case of '{txt2}': ",txt2.replace("H","W"))
txt="Lion, Tiger, Cat, Fox"
print(f"split of '{txt}': ",txt.split(","))

print()
print("======Concatenation of String======")
txt1="Happy"
txt2="learning"
txtAry=["Happy","learning"]
print(f"Concatenation of '{txt1}' and '{txt2}' is : ",txt1+" "+txt2)
print(f"Using join, Concatenation of '{txtAry}' is : "," ".join(txtAry))

print()
print("======Escape Characters======")
txt = 'It\'s alright.'
print(f"To show Single Quote of {txt}: ",txt)
txt = "This will insert one \\ (backslash)."
print(f"To show double Quote of {txt}: ",txt)
txt = "Happy\nlearning!"
print(f"new line of 'Happy learning': ",txt)
txt = "Happy\tlearning!"
print(f"tab of 'Happy learning': ",txt)

