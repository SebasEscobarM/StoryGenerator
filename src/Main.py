import sys
from PyQt5 import QtWidgets
from ui.main_window import Ui_MainWindow, NotificationDialog, NounChangeDialog, FinalWindow, CustomInputDialog
from model.Automaton import Automaton
from model.Grammar import Grammar
import random


class HistoryGeneratorApp(QtWidgets.QMainWindow):
    singleton: 'HistoryGeneratorApp' = None
    def __init__(self, automaton, grammar):
        super().__init__()
        self.rollback = False
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.nod = automaton
        self.grammar = grammar
        self.states = []
        self.path = ""

        self.ui.confirmationButton.clicked.connect(self.handle_confirmation)
        self.ui.menuOptions.addAction(
            "Personalizar nombres en la historia", self.show_noun_change_dialog
        )
        self.init_config()
        self.show()

    def init_config(self):
        dialog = CustomInputDialog(self)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            name = dialog.get_name()
            if(dialog.result == "custom"):
                self.run_custom_game(name)
            else:
                self.run_random_game(name)
        else:
            self.load_info(list(self.nod.to_dict().keys())[0])
        
    def run_random_game(self, user_name):
        if user_name != "":
                self.nod.modify_name("Protagonista", user_name.capitalize())
        self.path = self.grammar.generate_rd_story()
        self.set_up_full_story()

    def run_custom_game(self, user_name):
        if user_name != "":
                self.nod.modify_name("Protagonista", user_name.capitalize())
        self.load_info(list(self.nod.to_dict().keys())[0])

    def set_up_full_story(self):
        self.ui.menubar.setVisible(False)
        self.ui = FinalWindow()
        self.ui.setupUi(self)
        story, urls = self.get_story_from_path()
        self.ui.add_elements(story, urls)
        self.ui.volver_button.clicked.connect(self.restart)
        self.ui.salir_button.clicked.connect(self.exit_program)

    def exit_program(self):
        # Close the current application window
        self.close()
    
    def restart(self):
        self.close()
        self.restart_program()
        
    @staticmethod
    def restart_program():
        automaton = Automaton()
        grammar = Grammar()
        HistoryGeneratorApp.singleton = HistoryGeneratorApp(automaton, grammar)
    

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
                    f"assets/images/Fin {self.nod.get_index_of_final_state(current_state.value)+1}/{random.randint(1,4)}.jpg"
                )
        return decisions, urls

    def show_noun_change_dialog(self):
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
        choice = None
        choice = self.verify_answer(response.replace(" ", "_"), node_options)

        if choice is None:
            self.ui.set_answer("")
            noti = NotificationDialog("!Atención! opción no válida \n recuerda escribir en el recuadro de respuesta")
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
            self.ui.set_photo_A(url_A)
            self.ui.set_photo_B(url_B)
            self.ui.set_answer("")
            nod_dict = self.nod.to_dict()
            self.ui.set_current_state(current_state.value)
            print("[Escena actual] \n", current_state)
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
                print("------------Has escogido ", option.value.replace("_", " "),"------------")
                return option
            n = n + 1
        return None

    def get_img_url(self, current_state_index):
        return (
            f"assets/images/Punto {current_state_index}/a/{random.randint(1,4)}.jpg",
            f"assets/images/Punto {current_state_index}/b/{random.randint(1,4)}.jpg",
        )
    
stylesheet = """
    HistoryGeneratorApp {
        background-image: url("assets/images/bg/bg3.png");
        background-repeat: no-repeat; 
        background-position: center;
    }

    HistoryGeneratorApp FinalWindow {
        background-color: #000;
    }

    FinalWindow {
        background-color: #000;
    }
"""

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    HistoryGeneratorApp.restart_program()
    sys.exit(app.exec_())
