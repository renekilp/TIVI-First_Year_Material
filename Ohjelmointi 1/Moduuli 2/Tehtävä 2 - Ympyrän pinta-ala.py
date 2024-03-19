from math import pi

user_input = input("Syötä ympyrän säde: \n")
user_int = int(user_input)
new_value = pi * user_int ** 2
print("Ympyrän pinta-ala on: \n" + str(new_value))
