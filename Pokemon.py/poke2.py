from Pokemon  import Pokemon

def combat(pokemon1, pokemon2):
    while pokemon1.points_de_vie > 0 and pokemon2.points_de_vie > 0:
        # Pokémon 1 attaque Pokémon 2
        pokemon1.attaquer(pokemon2)
        print(f"{pokemon1.nom} attaque {pokemon2.nom} !")
        print(f"Points de vie de {pokemon2.nom} : {pokemon2.points_de_vie}")

        # Vérification si Pokémon 2 est KO
        if pokemon2.points_de_vie <= 0:
            print(f"{pokemon1.nom} gagne le combat !")
            return

        # Pokémon 2 attaque Pokémon 1
        pokemon2.attaquer(pokemon1)
        print(f"{pokemon2.nom} attaque {pokemon1.nom} !")
        print(f"Points de vie de {pokemon1.nom} : {pokemon1.points_de_vie}")

        # Vérification si Pokémon 1 est KO
        if pokemon1.points_de_vie <= 0:
            print(f"{pokemon2.nom} gagne le combat !")
            return
        def combat(pokemon1, pokemon2):
         while pokemon1.points_de_vie > 0 and pokemon2.points_de_vie > 0:
        # Pokémon 1 attaque Pokémon 2
           pokemon1.attaquer(pokemon2)
        print(f"{pokemon1.nom} attaque {pokemon2.nom} !")
        print(f"Points de vie de {pokemon2.nom} : {pokemon2.points_de_vie}")

        # Vérification si Pokémon 2 est KO
        if pokemon2.points_de_vie <= 0:
            print(f"{pokemon1.nom} gagne le combat !")
            return

        # Pokémon 2 attaque Pokémon 1
        pokemon2.attaquer(pokemon1)
        print(f"{pokemon2.nom} attaque {pokemon1.nom} !")
        print(f"Points de vie de {pokemon1.nom} : {pokemon1.points_de_vie}")

        # Vérification si Pokémon 1 est KO
        if pokemon1.points_de_vie <= 0:
            print(f"{pokemon2.nom} gagne le combat !")
            return
# Création de deux Pokémon
pikachu = Pokemon("Pikachu", 5, "Electrique")
carapuce = Pokemon("Carapuce", 5, "Eau")

# Combat entre Pikachu et Carapuce
combat(pikachu, carapuce)