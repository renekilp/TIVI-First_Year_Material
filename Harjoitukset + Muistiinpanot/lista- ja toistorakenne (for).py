
#   Lista on tietorakenne, jossa alkiot ovat niin ikään kuin jonossa, määrätyssä järjestyksessä

people = ['Juha', 'Matti', 'Oskari', 'Pekka', 'Olli', 'Nea']
#   0, 1, 2, 3,...
#print(people[-3])
#   [indexing], [2:4] esim., [1:5:2] esim., [-3], KÄÄNTEINEN JÄRJESTYS [::-1]
people.append('Onni')
print(people)

people2 = ['Martin', 'Olga']
people.extend(people2)  # extend lisää haluttuun listaan
print(people)

x = 'Onni' in people    # True / False
print(x)

print(people.index('Olga')) # kertoo indexin

people.sort()   # järjestää ihmiset
print(people)

#   ------------------------------------------

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
odd_numbers = []

for value in values:
    if value % 2 == 0:
        even_numbers.append(value)
    if value % 2 != 0:
        odd_numbers.append(value)
print(f'Parilliset luvut: {even_numbers} ja parittomat luvut: {odd_numbers}')

#   ------------------------------------

probabilities = [0.52, 0.49, 0.72, 0.81, 0.12, 0.11]
prob_list = []

for prob in probabilities:
    if prob > 0.5:
        prob_list.append(1)
    if prob < 0.5:
        prob_list.append(0)
print(f'{prob_list}')

#   ---------------------------

lista = ['a', 'b', 'c', 'd', 'e']
pituus = print(len(lista))  #len antaa pituuden

lista.pop(3)
print(lista)

lista.remove('a')
print(lista)

myrange = range(1, 10, 2) # "pussi"
# print(myrange) printtaa "range(1, 10, 2)"
for number in myrange :
    print(number)

#   --------------------------------------

myrange = range(0, 100, 11)
values = []

for value in myrange :
    values.append(value)
values.pop(0)
print(f'values: {values}')


#   -------------------------------------


for _ in range(6): # _ jos ei haluta antaa luvulle arvoa
    print("Moi!") # tulostaa 6 kertaa "Moi!" 0-5 index
    print(luku)

#   -------------------------------


luvut = []
my_range = range(95, 0, -5)
for luku in my_range:
    luvut.append(luku)

print(f'{luvut}')