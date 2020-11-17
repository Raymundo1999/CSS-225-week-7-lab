#Raymundo Sanchez
#Nov 16, 2020
#a person can type a letter a,b, or c and if they do it correctly they get a great job symbol.
#also if they dont put these three responses it will just keep telling to put one of these responses.
user_input = input("Type 'a','b', or 'c': ")
print(user_input)
while user_input != "a" and user_input != "b" and user_input != "c":
    user_input = input("Type 'a', 'b', or 'c': ")
    print(user_input)

print("great Job")
