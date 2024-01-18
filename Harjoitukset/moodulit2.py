age = 5
print(age)
age = 6
print(age + 2)
#   merkkijono
age_string = "seitsemän"
#   kokonaisluku
age_int = 6
#   ei toimi (age_int + age_string)
#   plus lasku
print(age_int + 4)
#   merkkijonojen liittymine (concvatenation)
print(age_string + " vuotta")

#   liukuluvut [float/ tuple] (ei ihan sama kuin desimaaliluku)

depth = 1000.0
width = 7_000 # merkki _ helpottaa lukemista
area = depth * width
print(area)





#    boolean: totta vai tarua (pyhtonissa 1 tai 0)

is_it_true = True
print(is_it_true)
is_it_false = False

#   tyyppimuunnokset
age_input = input("kuinka vanha olet?")
age_int = int(age_input) #esim. 13  -> 13
new_age = age_int + 1
print("vuoden päästä olet " + str(new_age) + " vuotta.")
#   tai f-stringgillä
print(f"Vuoden pääsät olet {new_age} vuotta.")
