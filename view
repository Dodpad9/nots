from PyQt5.QtWidgets import QWidget, QPushButton, QListWidget, QTextEdit, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel #імпорт потрібних імпортів
from app import app
main_window = QWidget() #Головне вікно
text_layout = QVBoxLayout() #Лінія тексту
menu_layout = QVBoxLayout()
# menu_layout2 = QVBoxLayout()
main_layout = QHBoxLayout()
main_layout2 = QHBoxLayout()
text_editor = QTextEdit() #водити в лінію текст
text_layout.addWidget(text_editor) #прикріплення тексту к лінії
notes_Label = QLabel('Список заміток')
notes_list = QListWidget()
menu_layout.addWidget(notes_Label)


text_button_Layout = QHBoxLayout()
add_note_button = QPushButton('створити замітку')
remove_note_button = QPushButton('Видалити замітку')
text_button_Layout.addWidget(add_note_button)
text_button_Layout.addWidget(remove_note_button)
teges_list = QListWidget()
menu_layout.addWidget(notes_list)
menu_layout.addLayout(text_button_Layout)
save_note_button = QPushButton('Зберегти')
menu_layout.addWidget(save_note_button)
menu_layout.addWidget(teges_list)
tag_name_input = QLineEdit()
tag_name_input.setPlaceholderText('Введіть текст...')
menu_layout.addWidget(tag_name_input)

tegs_button_Layout = QHBoxLayout()
pin_to_note = QPushButton('створити замітку')
unpin_from_note = QPushButton('Видалити замітку')
text_button_Layout.addWidget(pin_to_note)
text_button_Layout.addWidget(unpin_from_note)

menu_layout.addLayout(text_button_Layout)
menu_layout.addLayout(tegs_button_Layout)
search_note_button = QPushButton('пошук замітки по тегу')
menu_layout.addWidget(search_note_button)


main_layout.addLayout(text_layout)
# main_layout.addLayout(menu_layout2)
main_layout.addLayout(menu_layout)
main_window.setLayout(main_layout)