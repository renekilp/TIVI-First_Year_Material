""""
#   esitellään luokka
class Player:
    pass


p1 = Player()
p2 = Player()
p3 = Player()

#   p4 viittaa samaan olioon kuin p1
p4 = p1

p1.name = "Player 1"


print(p1)
print(p4.name)
"""


class Player:
    #   staattinen eli luokkamuuttuja (arvo jaetaan olioiden kesken)
    player_count = 0

    def __init__(self, name, start_location="Suomi"):   # start_location= "Suomi" jos halutaan kaikille sama lähtö
        #   self viittaa aina olioon itseenä
        Player.player_count = Player.player_count + 1
        print(f"Luodaan uusi pelaaja! Pelaajia on nyt {Player.player_count} kappaletta")
        self.name = name
        self.score = 0
        self.level = 1
        self.location = start_location

    def move_to_location(self, target):
        self.location = target
        print(f"Pelaajan {self.name} uusi sijainti on {target}")

    def upgrade_level(self):
        self.level = self.level + 1

    def add_score(self):
        self.score += self.level * 10

    def print_info(self):
        print(f"{self.name}, {self.score}, {self.location}")


p1 = Player("John", "Springfield")
p2 = Player("Jane", "Mordor")
p3 = Player("Mary", "Boston")

#   staattisiin muuttujiin viitataan luokan nimen avulla
print(Player.player_count)

p2.move_to_location("Shire")
p2.add_score()
p2.upgrade_level()



#   Yleensä huono tapa muuttaa olion ominaisuuksia suuren ulkopuolella
#   p2.score = 16

print(f"{p1.name}'s score is {p1.score}\nThe location is {p1.location}\nThe player level is {p1.level}")
print(f"{p2.name}'s score is {p2.score}\nThe location is {p2.location}\nThe player level is {p2.level}")

p1.print_info()
#   Olio
players = []
#   Sijoitetaan viittaukset
players.append(Player("Aku"))
players.append(Player("Roope"))
players.append(Player("Hessu"))
players.append(Player("Tupu"))

#   listan käsittely loopissa kuin ennenkin

for p in players:
    p.print_info()
    p.add_score()
for p in players:
    p.print_info()


class Player:
    def __init__(self, name, race):
        self.name = name
        self.race = race

    def __repr__(self):
        return f"Tämän söpön pelaajan nimi on:\n{self.name}\nja hänen rotunsa on:\n{self.race} 😘"


player1 = Player("Onni Monni", "Hobitti")
player2 = Player("Joni Poni", "Haltija")

print(player1)
print(player2)