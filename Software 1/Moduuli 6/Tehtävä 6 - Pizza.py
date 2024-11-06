import math

pizza1_price = float(input("Syötä ensimmäisen pizzan hinta:\n"))
pizza1_diameter = float(input("Syötä ensimmäisen pizzan halkaisija (cm):\n"))
pizza2_price = float(input("Syötä toisen pizzan hinta:\n"))
pizza2_diameter = float(input("Syötä toisen pizzan halkaisija (cm):\n"))

def calc_pizza_price(pizza_diameter, pizza_price):
    radius = pizza_diameter / 2
    area = math.pi * radius ** 2
    price = pizza_price / area
    price_squarem = price * 10000   #   m^2
    return price_squarem


pizza1_price1 = calc_pizza_price(pizza1_price, pizza1_diameter)
pizza2_price2 = calc_pizza_price(pizza2_price, pizza2_diameter)

if pizza1_price1 > pizza2_price2:
    print("Ensimmäinen syöttämäsi pizza on parempi vastine rahallesi!")
elif pizza1_price1 < pizza2_price2:
    print("Toinen syöttämäsi pizza on parempi vastine rahallesi!")
else:
    print("Syöttämäsi pizzat ovat molemmat yhtä hyviä!")
    print(f"{pizza1_price1} and {pizza2_price2}")







