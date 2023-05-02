import random
import json

class Pokemon:
    def __init__(self, nom, niveau, type1, type2=None):
        self.__nom = nom
        self.niveau = niveau
        self.type1 = type1
        self.type2 = type2
        self.__points_de_vie = 100
        self.puissance_attaque = 10 * niveau
        self.defense = 0

    def attaquer(self, autre_pokemon):
        degats = self.puissance_attaque - autre_pokemon.defense
        autre_pokemon.__points_de_vie -= degats

    def __str__(self):
        return f"{self.__nom} (niveau {self.niveau})"

    def afficher_informations(self):
        print(f"Nom : {self.__nom}")
        print(f"Points de vie : {self.__points_de_vie}")
        print(f"Défense : {self.defense}")
        print(f"Puissance d'attaque : {self.puissance_attaque}")

    def sauvegarder_dans_pokedex(self):
        with open("pokedex.json", "w+") as f:
try:
    with open("pokedex.json", "w+") as f:
        pokedex = json.load(f)

except (FileNotFoundError, json.decoder.JSONDecodeError):
    
    with open("pokedex.json", "w+") as f:
        json.dump({}, f)    
        pokedex = json.load(f)
                
        if self.__nom not in pokedex:
            pokedex[self.__nom] = {
                "type1": self.type1,
                "type2": self.type2,
                "points_de_vie": self.__points_de_vie,
                "puissance_attaque": self.puissance_attaque,
                "defense": self.defense
            }

            with open("pokedex.json", "w+") as f:
                json.dump(pokedex, f)

class Normal(Pokemon):
    def __init__(self, nom, niveau, type1, type2=None):
        super().__init__(nom, niveau, type1, type2)
        self.__points_de_vie += 20

class Feu(Pokemon):
    def __init__(self, nom, niveau, type1, type2=None):
        super().__init__(nom, niveau, type1, type2)
        self.puissance_attaque += 10

class Eau(Pokemon):
    def __init__(self, nom, niveau, type1, type2=None):
        super().__init__(nom, niveau, type1, type2)
        self.defense += 10

class Terre(Pokemon):
    def __init__(self, nom, niveau,type1,type2=None):
        super().__init__(nom,niveau,type1,type2)
        self.__points_de_vie += 10
        self.defense += 5

class Combat:
    def __init__(self,pokemon1,pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def verifier_vie(self):
        if self.pokemon1.points_de_vie <= 0:
            return False
        elif self.pokemon2.points_de_vie <= 0:
            return False
        else:
            return True

    def vainqueur(self):
        if self.pokemon1.points_de_vie <= 0:
            return f"{self.pokemon2.nom} a gagné le combat !"
        elif self.pokemon2.points_de_vie <= 0:
            return f"{self.pokemon1.nom} a gagné le combat !"

    def attaque_aleatoire(self,pokemon):
      if random.randint(0,1) == 1:
          return True
      else:
          return False

    def ajuster_degats(self,pokemon_attaquant,pokemon_defenseur):
      if pokemon_attaquant.type1 == "Feu" and pokemon_defenseur.type1 == "Eau":
          return pokemon_attaquant.puissance_attaque * 0.5
      elif pokemon_attaquant.type1 == "Eau" and pokemon_defenseur.type1 == "Feu":
          return pokemon_attaquant.puissance_attaque * 2
      elif pokemon_attaquant.type1 == "Feu" and pokemon_defenseur.type1 == "Terre":
          return pokemon_attaquant.puissance_attaque * 2
      elif pokemon_attaquant.type1 == "Terre" and pokemon_defenseur.type1 == "Feu":
          return pokemon_attaquant.puissance_attaque * 0.5
      # Création de deux Pokémon
pikachu = Feu("Pikachu", 5, "Feu")
carapuce = Eau("Carapuce", 5, "Eau")

# Affichage des informations des Pokémon
pikachu.afficher_informations()
carapuce.afficher_informations()

# Sauvegarde des Pokémon dans le Pokédex
pikachu.sauvegarder_dans_pokedex()
carapuce.sauvegarder_dans_pokedex()

# Création d'un combat entre Pikachu et Carapuce
combat = Combat(pikachu, carapuce)

# Boucle de combat
while combat.verifier_vie():
    # Pikachu attaque Carapuce
    if combat.attaque_aleatoire(pikachu):
        degats = combat.ajuster_degats(pikachu, carapuce)
        carapuce.points_de_vie -= degats
        print(f"{pikachu.nom} attaque {carapuce.nom} et inflige {degats} points de dégâts !")
    else:
        print(f"{pikachu.nom} rate son attaque !")

    # Vérification si Carapuce est KO
    if not combat.verifier_vie():
        print(combat.vainqueur())
        break

    # Carapuce attaque Pikachu
    if combat.attaque_aleatoire(carapuce):
        degats = combat.ajuster_degats(carapuce, pikachu)
        pikachu.points_de_vie -= degats
        print(f"{carapuce.nom} attaque {pikachu.nom} et inflige {degats} points de dégâts !")
    else:
        print(f"{carapuce.nom} rate son attaque !")

    # Vérification si Pikachu est KO
    if not combat.verifier_vie():
        print(combat.vainqueur())
        break