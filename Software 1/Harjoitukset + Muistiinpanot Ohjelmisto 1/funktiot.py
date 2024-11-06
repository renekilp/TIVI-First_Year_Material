#   yksinkertainen funktio ei palauta mitään
def do_something():
    print("tee jotain")
    print("tee jotain muuta")


do_something()

print("jotain muuta koodia")

do_something()

#parametrisoitu funktio
def calculate_numbsers(calc_type, num1, num2): #järjestys!
    #   print(f'{num1 + num2}')
    if calc_type == "add":
        return num1 + num2
    #   funktio loppuu heti, kun se pelauttaa jotain
    elif calc_type == "multiply":
        return num1 * num2
    return "No such calculation type!"


sum_of_numbers = calculate_numbsers("add",2,3) #järjestys!
print(f'Summa: {sum_of_numbers}')
print(f'Tulo: {calculate_numbsers('multiply',2,3)}')

#   lista parametrina

def calculate_numbsers_list(calc_type, numbers):
    if calc_type == "add":
        numbers_sum = 0
        for num in numbers:
            numbers_sum += num
        return numbers_sum
    #   funktio loppuu heti, kun se pelauttaa jotain
    elif calc_type == "multiply":
        result = 1
        for num in numbers:
            result = result * num
        return result
    return "No such calculation type!"

sum_of_numbers = calculate_numbsers_list("add",[1, 2, 3, 4])
print(f'Summa: {sum_of_numbers}')
print(f'Tulo: {calculate_numbsers_list("multiply",[1,2,3,4])}')

#   lista parametrina (viittaus/ referenssi)

inventory = ["Kynä", "kumi"]

def add_stuff(item, new_inventory):
    new_inventory.append(item)
    print(f"Reppuun lisättiin {item}")
    return new_inventory

updated_inventory = add_stuff("tietokone", inventory)

inventory.append("hiiri")

print(inventory)
print(updated_inventory)
updated_inventory.append("kuulakynä")   #   viittaa/ referoi juuri alkuperäiseen invenataarioon
print(inventory)

#   materiaaliesimerrki primitiiviarvon avulla

def vaihda(kaupunki):
    kaupunki = "Vantaa"
    print("Funktiossa lopuksi " + kaupunki)
    return

kaupunki = "Helsinki"
print("Pääohjelmassa olisi alussa " + kaupunki)
vaihda(kaupunki)
print("Pääohjelmassa kaupunki: "+ kaupunki)
#   primitiiviarvon lopullinen arvo pysyy samana

#   nimitetyt parametrit

def calc_v2(num1, num2, calc_type = "add"):
    if calc_type == "add":
        return num1 + num2
    elif calc_type == "multiply":
        return num1 * num2

result = calc_v2(1, 2)
print(result)
result = calc_v2(num2=2, num1=4, calc_type="multiply") #    järjestyksen muutos
print(result)

#   satunnainen määrä parametrejä

def list_numbers(*parameters):
    #   parameters sisältää kaikki annetut parametrien arvot yhtenä monikkona
    #   ("kiinteä" lista)
    return parameters

list_numbers(1,2,3,4,5,6,7,8)
print(list_numbers(2,5,7,"kuutonen"))


