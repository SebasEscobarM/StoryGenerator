from model.Automaton import Automaton

def main():
    nod = Automaton()
    regex = nod.to_regex()
    
    print(regex.accepts([
        "Buscar refugio en el bosque de las Sombras".replace(" ", "_"),
        "Construir una choza".replace(" ", "_"),
        "Accionar una extraña palanca en una palmera".replace(" ", "_")
        ]))
    
    print(regex.accepts([
        "Buscar refugio en el bosque de las Sombras".replace(" ", "_"),
        "Construir una choza".replace(" ", "_"),
        "Encontrar pistas sobre el tesoro".replace(" ", "_"),
        "Explorar las ruinas de noche".replace(" ", "_")
        ]))
    
    print(regex.accepts([
        "Buscar refugio en el bosque de las Sombras".replace(" ", "_"),
        "Construir una choza".replace(" ", "_"),
        "Encontrar pistas sobre el tesoro".replace(" ", "_"),
        "Explorar las ruinas de día".replace(" ", "_")
        ]))
    


if __name__ == "__main__":
    main()