from model.Automaton import Automaton


def main():
    nod = Automaton()
    regex = nod.to_regex()

    print(
        regex.accepts(
            [
                "Buscar refugio en el bosque de las Sombras".replace(" ", "_"),
                "Construir una choza".replace(" ", "_"),
                "Accionar una extraña palanca en una palmera".replace(" ", "_"),
            ]
        )
    )

    print(
        regex.accepts(
            [
                "Buscar refugio en el bosque de las Sombras".replace(" ", "_"),
                "Construir una choza".replace(" ", "_"),
                "Encontrar pistas sobre el tesoro".replace(" ", "_"),
                "Explorar las ruinas de noche".replace(" ", "_"),
            ]
        )
    )

    print(
        regex.accepts(
            [
                "Buscar refugio en el bosque de las Sombras".replace(" ", "_"),
                "Construir una choza".replace(" ", "_"),
                "Encontrar pistas sobre el tesoro".replace(" ", "_"),
                "Explorar las ruinas de día".replace(" ", "_"),
            ]
        )
    )

    nod_dict = nod.to_dict()
    keys = list(nod_dict.keys())
    current_state = keys[0]

    while True:
        print("------------Escenario---------- \n", current_state)
        node_options = nod_dict[current_state]
        break_flag = False
        choice = None
        while choice == None:
            options_to_show = [
                option.value.replace("_", " ") for option in list(node_options.keys())
            ]
            response = input(options_to_show)
            if response.lower() in ["salir", "exit"]:
                break_flag = True
                break
            choice = verify_answers(nod, response.replace(" ", "_"), node_options)
            if choice == None:
                print("Has escogido una opción no válida\n")
        if break_flag:
            break
        current_state = node_options[choice.value]
        if nod.is_final_state(current_state):
            print(current_state)
            break


def verify_answers(nod,response, options):
    regex = nod.regular_expressions
    for option in options:
        print(option)
        print(regex[option])
        if(regex[option].match(response)):
            print("Has escogido ", option.value.replace("_"," "))
            return option
    return None


if __name__ == "__main__":
    main()
