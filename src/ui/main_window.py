# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(692, 480)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
       
        self.photoA = QtWidgets.QLabel(self.centralwidget)
        self.photoA.setGeometry(QtCore.QRect(75, 40, 221, 221))
        self.photoA.setText("")

        self.photoA.setScaledContents(True)
        self.photoA.setObjectName("photoA")
        self.set_up_photo(self.photoA)

        # photoB
        self.photoB = QtWidgets.QLabel(self.centralwidget)
        self.photoB.setGeometry(QtCore.QRect(395, 40, 221, 221))
        self.photoB.setText("")

        self.photoB.setScaledContents(True)
        self.photoB.setObjectName("photoB")
        self.set_up_photo(self.photoB)
        self.label_A = QtWidgets.QLabel(self.centralwidget)
        self.label_A.setGeometry(QtCore.QRect(40, 280, 291, 31))
        self.label_B = QtWidgets.QLabel(self.centralwidget)
        self.label_B.setGeometry(QtCore.QRect(360, 280, 291, 31))
        self.label_A.setMinimumHeight(60)
        self.label_B.setAlignment(QtCore.Qt.AlignCenter)
        self.label_B.setMinimumHeight(60)
        self.label_A.setAlignment(QtCore.Qt.AlignCenter)
        self.set_up_label(self.label_A)
        self.set_up_label(self.label_B)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(230, 350, 241, 40))
        self.textEdit.setToolTip("")
        self.textEdit.setAccessibleName("")
        self.textEdit.setAccessibleDescription("")
        self.textEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit.setPlaceholderText("Ingresa palabras clave o todo el texo de tu camino a seguir")
        self.textEdit.setObjectName("textEdit")
        self.set_up_text_edit(self.textEdit)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 611, 27))
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.set_up_state_label(self.label)

        # Confirmation Button
        self.confirmationButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmationButton.setGeometry(QtCore.QRect(294, 398, 111, 41))
        self.confirmationButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.confirmationButton.setObjectName("confirmationButton")
        self.set_up_button(self.confirmationButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 692, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stories Generator"))
        self.label_A.setText(_translate("MainWindow", "Option A text of the story"))
        self.label_B.setText(_translate("MainWindow", "Option B text of the story"))
        self.label.setText(_translate("MainWindow", "State Name"))
        self.confirmationButton.setText(_translate("MainWindow", "Adelante!"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))

    def set_up_text_edit(self, text_edit):
        text_edit.setStyleSheet(
            """
            background-color: #DFA97C;  
            color: #3C0F0C;
            border: 1px solid #3C0F0C;
            """
        )
        font_path = "assets/fonts/PixelifySans-VariableFont_wght.ttf"  # Replace with the actual path to your font file
        undertale_font = QtGui.QFontDatabase.addApplicationFont(font_path)

        if undertale_font != -1:
            font_family = QtGui.QFontDatabase.applicationFontFamilies(undertale_font)[0]

            # Create a QFont with the Undertale-like font family
            undertale_like_font = QtGui.QFont(font_family, 10)  # Adjust the size as needed
            
            # Set the QFont for the QLabel
            text_edit.setFont(undertale_like_font)

    def set_up_button(self, button):
        button.setStyleSheet(
            """
            background-color: #3C0F0C;  
            color: #DFA97C;                   
            text-align: center;
            border: 2px solid #DFA97C;
            border-radius: 5px;
            height: 20px;
            """
        )
        font_path = "assets/fonts/PixelifySans-VariableFont_wght.ttf"  # Replace with the actual path to your font file
        undertale_font = QtGui.QFontDatabase.addApplicationFont(font_path)

        if undertale_font != -1:
            font_family = QtGui.QFontDatabase.applicationFontFamilies(undertale_font)[0]

            # Create a QFont with the Undertale-like font family
            undertale_like_font = QtGui.QFont(font_family, 14)  # Adjust the size as needed
            
            # Set the QFont for the QLabel
            button.setFont(undertale_like_font)
        

    def set_up_state_label(self, label):
        label.setStyleSheet(
            "background-color: #3C0F0C; "  # Set background color
            "color: #DFA97C; "                   # Set text color
            "text-align: center;"
            "border: 2px solid #DFA97C;"
            "border-radius: 10px;"
            "height: 20px;"
        )

         # Create a QFont with a monospaced font family
        font_path = "assets/fonts/PixelifySans-VariableFont_wght.ttf"  # Replace with the actual path to your font file
        undertale_font = QtGui.QFontDatabase.addApplicationFont(font_path)

        if undertale_font != -1:
            font_family = QtGui.QFontDatabase.applicationFontFamilies(undertale_font)[0]

            # Create a QFont with the Undertale-like font family
            undertale_like_font = QtGui.QFont(font_family, 14)  # Adjust the size as needed
            undertale_like_font.setBold(True)
            # Set the QFont for the QLabel
            label.setFont(undertale_like_font)
        label.setWordWrap(True)

    def set_up_label(self, label):
        label.setStyleSheet(
            "background-color: black; "  # Set background color
            "color: white; "                   # Set text color
            "text-align: center;"
            "border: 2px solid #fff;"
            "border-radius: 5px;"
        )

         # Create a QFont with a monospaced font family
        font_path = "assets/fonts/PixelifySans-VariableFont_wght.ttf"  # Replace with the actual path to your font file
        undertale_font = QtGui.QFontDatabase.addApplicationFont(font_path)

        if undertale_font != -1:
            font_family = QtGui.QFontDatabase.applicationFontFamilies(undertale_font)[0]

            # Create a QFont with the Undertale-like font family
            undertale_like_font = QtGui.QFont(font_family, 11)  # Adjust the size as needed

            # Set the QFont for the QLabel
            label.setFont(undertale_like_font)
        label.setWordWrap(True)

    def set_up_photo(self, photo):
        photo.setStyleSheet(
            "border: 4px solid #000;"
        )

    def set_label_A(self, text):
        self.label_A.setText(text)

    def set_label_B(self, text):
        self.label_B.setText(text)

    def get_label_A(self):
        return self.label_A.text()

    def get_label_B(self):
        return self.label_B.text()

    def get_answer(self):
        return self.textEdit.toPlainText()

    def set_answer(self, text):
        self.textEdit.setPlainText(text)

    def set_current_state(self, text):
        self.label.setText(text)

    def get_current_state(self):
        return self.label.text()

    def set_photo_A(self, image_url):
        pixmap = QtGui.QPixmap(image_url)
        self.photoA.setPixmap(pixmap)

    def set_photo_B(self, image_url):
        pixmap = QtGui.QPixmap(image_url)
        self.photoB.setPixmap(pixmap)



class NotificationDialog(QtWidgets.QDialog):
    def __init__(self, message):
        super().__init__()

        self.setWindowTitle("Notification")
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        label = QtWidgets.QLabel(message, self)
        layout.addWidget(label)

        ok_button = QtWidgets.QPushButton("OK", self)
        ok_button.clicked.connect(self.accept)
        layout.addWidget(ok_button)


def show_notification(message):
    dialog = NotificationDialog(message)
    dialog.exec_()


class NounChangeDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Change Nouns")
        self.initUI()

    def initUI(self):
        layout = QtWidgets.QVBoxLayout()

        # Add a ComboBox for noun selection
        self.noun_selection = QtWidgets.QComboBox(self)

        # Add more items for other nouns as needed
        layout.addWidget(self.noun_selection)

        # Add an input field for the new noun name
        self.new_noun_name_input = QtWidgets.QLineEdit(self)
        self.new_noun_name_input.setPlaceholderText("Nuevo nombre")
        layout.addWidget(self.new_noun_name_input)

        # Create Save and Cancel buttons
        button_box = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Save | QtWidgets.QDialogButtonBox.Cancel, self
        )
        button_box.accepted.connect(self.save_changes)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

        self.setLayout(layout)

    def set_up_selections(self, names):
        for pk in names:
            self.noun_selection.addItem(pk)

    def set_text_value(self, current, names_dict):
        self.new_noun_name_input.setText(names_dict[current])

    def save_changes(self):
        # Retrieve values from ComboBox and input field
        selected_noun = self.noun_selection.currentText()
        new_noun_name = self.new_noun_name_input.text()
        # Update the story with the selected noun and new name
        self.accept()


from PyQt5.QtWidgets import (
    QVBoxLayout,
    QLabel,
)


class Pruebita(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(692, 469)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)

        self.setup_styles(MainWindow)
        self.volver_button = QtWidgets.QPushButton("Volver a jugar")
        self.volver_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.salir_button = QtWidgets.QPushButton("Salir")
        self.salir_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.set_up_restart_button(self.volver_button)
        self.set_up_exit_button(self.salir_button)
        # Create a scroll area
        self.scrollArea = QtWidgets.QScrollArea(MainWindow)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 692, 469))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)

        # Create a container widget for the central widget
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 692, 469))

        # Set your existing central widget as the content of the scroll area
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        MainWindow.setCentralWidget(self.scrollArea)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setup_styles(self, window):
        stylesheet = """
            background-image: url("assets/images/bg/bg7.png");
            background-repeat: no-repeat; 
            background-position: center;
            
        """
        window.setStyleSheet(stylesheet)

    def add_elements(self, story, urls):
        # Create a QVBoxLayout for the content widget
        content_layout = QVBoxLayout(self.scrollAreaWidgetContents)
        label = QLabel("Disfruta de la historia aleatoria... ¡Y continúa explorando!")
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.set_up_state_label(label)
        content_layout.addWidget(label)

        # Create and add labels to the content layout in a loop
        for i in range(len(story)):
            label = QLabel(story[i])
            label.setFixedWidth(512)
            self.set_up_label(label)
            content_layout.addWidget(label)

            # Descargar la imagen desde la URL y mostrarla
            pixmap = QtGui.QPixmap(urls[i])

            # Redimensionar la imagen a 512x512
            pixmap = pixmap.scaled(512, 512)
            
            # Crear una etiqueta para mostrar la imagen
            image_label = QLabel()
            image_label.setPixmap(pixmap)
            self.set_up_image(image_label)
            
            # Set the label's size to match the image size
            image_label.setFixedSize(pixmap.size())
            content_layout.addWidget(image_label)

        # Crear un contenedor horizontal para los botones
        buttons_layout = QtWidgets.QHBoxLayout()

        # Agregar botones al contenedor horizontal de los botones

        buttons_layout.addWidget(self.volver_button)
        buttons_layout.addWidget(self.salir_button)

        content_layout.addLayout(buttons_layout)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "Recopilación de la historia")
        )

    def set_up_restart_button(self, button):
        button.setStyleSheet(
            """
            padding: 10px;
            background: #3C0F0C;  
            color: #DFA97C;                   
            text-align: center;
            border: 2px solid #DFA97C;
            border-radius: 5px;
            height: 20px;
            """
        )
        font_path = "assets/fonts/PixelifySans-VariableFont_wght.ttf"  # Replace with the actual path to your font file
        undertale_font = QtGui.QFontDatabase.addApplicationFont(font_path)

        if undertale_font != -1:
            font_family = QtGui.QFontDatabase.applicationFontFamilies(undertale_font)[0]

            # Create a QFont with the Undertale-like font family
            undertale_like_font = QtGui.QFont(font_family, 14)  # Adjust the size as needed
            
            # Set the QFont for the QLabel
            button.setFont(undertale_like_font)

    def set_up_exit_button(self, button):
        button.setStyleSheet(
            """
            padding: 10px;
            background: #2B0504;  
            color: #DFA97C;                   
            text-align: center;
            border: 2px solid #DFA97C;
            border-radius: 5px;
            height: 20px;
            """
        )
        font_path = "assets/fonts/PixelifySans-VariableFont_wght.ttf"  # Replace with the actual path to your font file
        undertale_font = QtGui.QFontDatabase.addApplicationFont(font_path)

        if undertale_font != -1:
            font_family = QtGui.QFontDatabase.applicationFontFamilies(undertale_font)[0]

            # Create a QFont with the Undertale-like font family
            undertale_like_font = QtGui.QFont(font_family, 14)  # Adjust the size as needed
            
            # Set the QFont for the QLabel
            button.setFont(undertale_like_font)

    def set_up_state_label(self, label):
        label.setStyleSheet(
            "background: #3C0F0C; "  # Set background color
            "color: #DFA97C; "                   # Set text color
            "text-align: center;"
            "border: 2px solid #DFA97C;"
            "border-radius: 10px;"
            "height: 20px;"
        )

         # Create a QFont with a monospaced font family
        font_path = "assets/fonts/PixelifySans-VariableFont_wght.ttf"  # Replace with the actual path to your font file
        undertale_font = QtGui.QFontDatabase.addApplicationFont(font_path)

        if undertale_font != -1:
            font_family = QtGui.QFontDatabase.applicationFontFamilies(undertale_font)[0]

            # Create a QFont with the Undertale-like font family
            undertale_like_font = QtGui.QFont(font_family, 14)  # Adjust the size as needed
            undertale_like_font.setBold(True)
            # Set the QFont for the QLabel
            label.setFont(undertale_like_font)
        label.setWordWrap(True)

    def set_up_image(self, image):
        image.setStyleSheet(
            "border: 4px solid #000;"
        )

    def set_up_label(self, label):
        label.setStyleSheet(
            "padding: 15px;"
            "background: black; "  # Set background color
            "color: white; "                   # Set text color
            "text-align: center;"
            "border: 2px solid #fff;"
            "border-radius: 5px;"
        )

         # Create a QFont with a monospaced font family
        font_path = "assets/fonts/PixelifySans-VariableFont_wght.ttf"  # Replace with the actual path to your font file
        undertale_font = QtGui.QFontDatabase.addApplicationFont(font_path)

        if undertale_font != -1:
            font_family = QtGui.QFontDatabase.applicationFontFamilies(undertale_font)[0]

            # Create a QFont with the Undertale-like font family
            undertale_like_font = QtGui.QFont(font_family, 11)  # Adjust the size as needed

            # Set the QFont for the QLabel
            label.setFont(undertale_like_font)
        label.setWordWrap(True)

class CustomInputDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Change Nouns")
        self.initUI()

    def initUI(self):
        layout = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel("¡Ponle un nombre al protagonista!\n(O usa el nombre por defecto):")
        self.set_up_label(label)
        self.text_input = QtWidgets.QLineEdit()
        self.text_input.setPlaceholderText("Silvanus es el nombre por defecto")
        self.text_input.setMinimumHeight(40)
        self.set_up_text_edit(self.text_input)
        self.custom_button = QtWidgets.QPushButton("Escoge tus caminos")
        self.random_button = QtWidgets.QPushButton("Genera una aleatoria")
        

        self.custom_button.clicked.connect(self.handle_custom)
        self.custom_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.set_up_custom_buttom(self.custom_button)
        self.random_button.clicked.connect(self.handle_random)
        self.random_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.set_up_random_buttom(self.random_button)

        layout.addWidget(label)
        layout.addWidget(self.text_input)
        layout.addWidget(self.custom_button)
        layout.addWidget(self.random_button)

        self.setLayout(layout)

    def get_name(self):
        return self.text_input.text()
    
    def handle_custom(self):
        self.result = "custom"
        self.accept()
    
    def handle_random(self):
        self.result = "random"
        self.accept()

    def set_up_text_edit(self, text_edit):
        text_edit.setStyleSheet(
            """
            color: #3C0F0C;
            border: 1px solid #3C0F0C;
            """
        )
        font_path = "assets/fonts/PixelifySans-VariableFont_wght.ttf"  # Replace with the actual path to your font file
        undertale_font = QtGui.QFontDatabase.addApplicationFont(font_path)

        if undertale_font != -1:
            font_family = QtGui.QFontDatabase.applicationFontFamilies(undertale_font)[0]

            # Create a QFont with the Undertale-like font family
            undertale_like_font = QtGui.QFont(font_family, 10)  # Adjust the size as needed
            
            # Set the QFont for the QLabel
            text_edit.setFont(undertale_like_font)

    def set_up_custom_buttom(self, button):
        button.setStyleSheet(
            """
            padding: 10px;
            background: #BA9656;
            color: #2B0504;                   
            text-align: center;
            border: 2px solid #2B0504;
            border-radius: 5px;
            height: 20px;
            """
        )
        font_path = "assets/fonts/PixelifySans-VariableFont_wght.ttf"  # Replace with the actual path to your font file
        undertale_font = QtGui.QFontDatabase.addApplicationFont(font_path)

        if undertale_font != -1:
            font_family = QtGui.QFontDatabase.applicationFontFamilies(undertale_font)[0]

            # Create a QFont with the Undertale-like font family
            undertale_like_font = QtGui.QFont(font_family, 11)  # Adjust the size as needed
            
            # Set the QFont for the QLabel
            button.setFont(undertale_like_font)

    def set_up_random_buttom(self, button):
        button.setStyleSheet(
            """
            background: #2B0504;
            color: #BA9656;                    
            text-align: center;
            border: 2px solid #BA9656;
            border-radius: 5px;
            height: 20px;
            """
        )
        font_path = "assets/fonts/PixelifySans-VariableFont_wght.ttf"  # Replace with the actual path to your font file
        undertale_font = QtGui.QFontDatabase.addApplicationFont(font_path)

        if undertale_font != -1:
            font_family = QtGui.QFontDatabase.applicationFontFamilies(undertale_font)[0]

            # Create a QFont with the Undertale-like font family
            undertale_like_font = QtGui.QFont(font_family, 11)  # Adjust the size as needed
            
            # Set the QFont for the QLabel
            button.setFont(undertale_like_font)

    def set_up_label(self, label):
        label.setStyleSheet(
            "padding: 15px;"
            "color: #000; "                   # Set text color
            "text-align: center;"
            "border-bottom: 1px solid #000;"
            "border-top: 1px solid #000;"
        )
        # Create a QFont with a monospaced font family
        font_path = "assets/fonts/PixelifySans-VariableFont_wght.ttf"  # Replace with the actual path to your font file
        undertale_font = QtGui.QFontDatabase.addApplicationFont(font_path)

        if undertale_font != -1:
            font_family = QtGui.QFontDatabase.applicationFontFamilies(undertale_font)[0]

            # Create a QFont with the Undertale-like font family
            undertale_like_font = QtGui.QFont(font_family, 11)  # Adjust the size as needed

            # Set the QFont for the QLabel
            label.setFont(undertale_like_font)
        label.setWordWrap(True)
    