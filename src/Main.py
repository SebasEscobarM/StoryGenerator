import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.main_window import Ui_MainWindow, NotificationDialog, NounChangeDialog, Pruebita
from model.Automaton import Automaton
from model.Grammar import Grammar
import random


class HistoryGeneratorApp(QtWidgets.QMainWindow):
    def __init__(self, automaton, grammar):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.nod = automaton
        self.grammar = grammar
        self.states = []
        self.path = ""


        print(self.nod.names["Protagonista"])
        # Create a dialog to set the user's name
        user_name, ok = QtWidgets.QInputDialog.getText(
            self,
            "Personaliza la historia",
            "¡Ponle un nombre al protagonista!\n (O usa el nombre por defecto):",
        )
        if ok:
            if user_name != "":
                self.nod.modify_name("Protagonista", user_name.capitalize())

        self.ui.confirmationButton.clicked.connect(self.handle_confirmation)
        self.ui.menuOptions.addAction(
            "Personalizar nombres en la historia", self.show_noun_change_dialog
        )

        self.load_info(list(self.nod.to_dict().keys())[0])

    def set_up_full_story(self):
        self.ui = Pruebita()
        self.ui.setupUi(self)
        story, urls = self.get_story_from_path()
        self.ui.add_elements(story, urls)

    def get_story_from_path(self):
        decisions = []
        urls = []
        nod_dict = self.nod.to_dict()
        current_state = list(nod_dict.keys())[0]

        answer = None
        for char in self.path:
            self.states.append(self.nod.get_index_of_state(current_state.value))
            url_A, url_B = self.get_img_url(self.nod.states.index(current_state) + 1)
            if char == "a":
                answer = list(nod_dict[current_state].keys())[0]
                decisions.append(answer.value.replace("_", " "))
                urls.append(url_A)
            else:
                answer = list(nod_dict[current_state].keys())[1]
                decisions.append(answer.value.replace("_", " "))
                urls.append(url_B)
            node_options = nod_dict[current_state]
            current_state = node_options[answer]

        decisions.append(current_state.value)
        self.states.append(self.nod.get_index_of_final_state(current_state.value))
        urls.append(
                    f"https://github.com/Juank114Gonzalez/TI1-CyED3-Imgs/blob/master/Fin%20{self.nod.get_index_of_final_state(current_state.value)+1}/{random.randint(1,4)}.jpg?raw=true"
                )
        return decisions, urls

    def show_noun_change_dialog(self):
        print("desde cambio de nombre: ", self.ui.get_current_state())
        index_of_current_state = self.nod.get_index_of_state(
            self.ui.get_current_state()
        )

        def update_text_field():
            dialog.set_text_value(dialog.noun_selection.currentText(), self.nod.names)

        dialog = NounChangeDialog(self)
        dialog.set_up_selections(self.nod.names.keys())
        dialog.noun_selection.currentTextChanged.connect(
            update_text_field
        )  # verificar si hay cambios en la Combo Box
        dialog.set_text_value(dialog.noun_selection.currentText(), self.nod.names)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            selected_noun = dialog.noun_selection.currentText()
            new_noun_name = dialog.new_noun_name_input.text()
            self.nod.modify_name(selected_noun, new_noun_name.capitalize())
            self.update_text_fields(self.nod.states[index_of_current_state])

    def update_text_fields(self, current_state):
        nod_dict = self.nod.to_dict()
        self.ui.set_current_state(current_state.value)
        node_options = nod_dict[current_state]
        options_to_show = [
            option.value.replace("_", " ") for option in list(node_options.keys())
        ]
        self.ui.set_label_A(options_to_show[0])
        self.ui.set_label_B(options_to_show[1])

    def handle_confirmation(self):
        nod_dict = self.nod.to_dict()
        node_options = nod_dict[self.nod.get_state(self.ui.get_current_state())]
        response = self.ui.get_answer()
        print(response)
        choice = None
        choice = self.verify_answer(response.replace(" ", "_"), node_options)

        if choice is None:
            self.ui.set_answer("")
            noti = NotificationDialog("!Atención! opción no válida")
            noti.exec_()
        else:
            current_state = node_options[choice.value]  # siguiente nodo

            if self.nod.is_final_state(current_state):
                self.states.append(
                    self.nod.get_index_of_final_state(current_state.value)
                )
                self.set_up_full_story()
            else:
                self.states.append(self.nod.get_index_of_state(current_state.value))
                self.load_info(current_state)

    def load_info(self, current_state):
        if not self.nod.is_final_state(current_state):
            url_A, url_B = self.get_img_url(self.nod.states.index(current_state) + 1)
            # self.ui.set_photo_A(url_A)
            # self.ui.set_photo_B(url_B)
            self.ui.set_answer("")
            nod_dict = self.nod.to_dict()
            self.ui.set_current_state(current_state.value)
            print("------------Escenario---------- \n", current_state)
            node_options = nod_dict[current_state]
            options_to_show = [
                option.value.replace("_", " ") for option in list(node_options.keys())
            ]
            self.ui.set_label_A(options_to_show[0])
            self.ui.set_label_B(options_to_show[1])

    def verify_answer(self, response, options):
        regex = self.nod.regular_expressions
        n = 0
        for option in options:
            if regex[option].match(
                response
            ):  # esta es la respuesta del usuario (N=0 o n=1)
                if n == 0:
                    self.path += "a"
                else:
                    self.path += "b"
                print("Has escogido ", option.value.replace("_", " "))
                return option
            n = n + 1
        return None

    def get_img_url(self, current_state_index):
        return (
            f"https://github.com/Juank114Gonzalez/TI1-CyED3-Imgs/blob/master/Punto%20{current_state_index}/a/{random.randint(1,4)}.jpg?raw=true",
            f"https://github.com/Juank114Gonzalez/TI1-CyED3-Imgs/blob/master/Punto%20{current_state_index}/b/{random.randint(1,4)}.jpg?raw=true",
        )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    automaton = Automaton()
    grammar = Grammar()
    window = HistoryGeneratorApp(automaton, grammar)
    window.show()
    sys.exit(app.exec_())
