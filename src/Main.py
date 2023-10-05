import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.main_window import Ui_MainWindow, NotificationDialog, NounChangeDialog
from model.Automaton import Automaton
import random
from multiprocessing import Pool


class HistoryGeneratorApp(QtWidgets.QMainWindow):
    def __init__(self, automaton):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.nod = automaton
        print(self.nod.names["Protagonista"])
        # Create a dialog to set the user's name
        user_name, ok = QtWidgets.QInputDialog.getText(

            self, "Personaliza la historia", "¡Ponle un nombre al protagonista!\n (O usa el nombre por defecto):"
        )   
        if ok:
             if(user_name != ""):
                self.nod.modify_name("Protagonista", user_name.capitalize())

        self.ui.confirmationButton.clicked.connect(self.handle_confirmation)
        self.ui.menuOptions.addAction("Personalizar nombres en la historia", self.show_noun_change_dialog)


        self.load_info(list(self.nod.to_dict().keys())[0])

    def show_noun_change_dialog(self):
        index_of_current_state = self.nod.get_index_of_state(self.ui.get_current_state())
        def update_text_field():
            dialog.set_text_value(dialog.noun_selection.currentText(), self.nod.names)
        dialog = NounChangeDialog(self) 
        dialog.set_up_selections(self.nod.names.keys())
        dialog.noun_selection.currentTextChanged.connect(update_text_field)
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
        options_to_show = [option.value.replace("_"," ") for option in list(node_options.keys())]
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
            noti = NotificationDialog("!Alerta! opción no válida")
            noti.exec_()
        else:
            current_state = node_options[choice.value]  # siguiente nodo
            if self.nod.is_final_state(current_state):
                print(current_state)
            else:
                self.load_info(current_state)

    def load_info(self, current_state):
        if not self.nod.is_final_state(current_state):
            url_A, url_B = self.get_img_url(self.nod.states.index(current_state) + 1)
            self.ui.set_photo_A(url_A)
            self.ui.set_photo_B(url_B)
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
        for option in options:
            print(option)
            print(regex[option])
            if regex[option].match(response):
                print("Has escogido ", option.value.replace("_", " "))
                return option
        return None

    def get_img_url(self, current_state_index):
        return (
            f"https://github.com/Juank114Gonzalez/TI1-CyED3-Imgs/blob/master/Punto%20{current_state_index}/a/{random.randint(1,4)}.jpg?raw=true",
            f"https://github.com/Juank114Gonzalez/TI1-CyED3-Imgs/blob/master/Punto%20{current_state_index}/b/{random.randint(1,4)}.jpg?raw=true",
        )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    automaton = Automaton()
    window = HistoryGeneratorApp(automaton)
    window.show()
    sys.exit(app.exec_())
