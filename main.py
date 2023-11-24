from view import main_window, app, notes_list, add_note_button #імпорт з папки view
import json
from PyQt5.QtWidgets import QInputDialog
notes = ['klvsjlvf', 'hsvdhuosvd', 'jvdfv']
def add_note():
    note_name, ok = QInputDialog().getText(main_window, 'Додати замітку', 'Назва замітки')
    if ok:
        notes.append(note_name)
        notes_list.clear()
        notes_list.addItems(notes)
# notes = ['fhvdahvdjivji', 'dlvdv']
# notes_list.addItems(notes) #добавляє фрази з класу до другого квадратика

with open('jsin.json', 'w', encoding='UTF-8') as f:
    # notes = json.load(f)
    # notes_list.addItems(notes)
    json.dump({}, f)

add_note_button.clicked.connect(add_note)
main_window.setWindowTitle('Розумні замітки')
main_window.show() #відображення віконечка
app.exec_() #не дозволяє закрити програму до моменту
