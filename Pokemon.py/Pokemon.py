class Pokemon:
    def __init__(self, nom, niveau, type1, type2=None):
        self.nom = nom
        self.niveau = niveau
        self.type1 = type1
        self.type2 = type2
        self.points_de_vie = 100
        self.puissance_attaque = 10 * niveau
        self.defense = 0

    def attaquer(self, autre_pokemon):
        degats = self.puissance_attaque - autre_pokemon.defense
        autre_pokemon.points_de_vie -= degats

    def __str__(self):
        return f"{self.nom} (niveau {self.niveau})"
    # Création de deux Pokémon
pikachu = Pokemon("Pikachu", 5, "Electrique")
carapuce = Pokemon("Carapuce", 5, "Eau")

# Affichage des informations des Pokémon
print(pikachu)
print(carapuce)

# Pikachu attaque Carapuce
pikachu.attaquer(carapuce)

# Affichage des points de vie de Carapuce après l'attaque
print(f"Points de vie de Carapuce : {carapuce.points_de_vie}")