from PyQt6.QtWidgets import QFontComboBox,QDateEdit,QListWidget,QMessageBox,QHBoxLayout,QVBoxLayout,QWidget,QApplication,QRadioButton,QLabel,QLayout,QPushButton,QLineEdit,QCheckBox,QComboBox
import sys
import datetime

class ToDoList(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TO DO LIST APPLICATION")
        self.setGeometry(100,100,200,200)

        self.name_label=QLabel("Name: ")
        self.name_input=QLineEdit()

        self.deadline_label=QLabel("Deadline: ")
        self.deadline_input=QDateEdit()

        self.content_label=QLabel("Task: ")
        self.content_input=QLineEdit()

        self.tasks={}

        layout=QVBoxLayout()

        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.deadline_label)
        layout.addWidget(self.deadline_input)
        layout.addWidget(self.content_label)
        layout.addWidget(self.content_input)

        self.create_button=QPushButton("CREATE")
        self.update_button=QPushButton("UPDATE")
        self.track_button=QPushButton("TRACK")

        btn_layout=QHBoxLayout()
        btn_layout.addWidget(self.create_button)
        btn_layout.addWidget(self.update_button)
        btn_layout.addWidget(self.track_button)
        self.setLayout(layout)
        layout.addLayout(btn_layout)

        self.create_button.clicked.connect(self.name)
        self.update_button.clicked.connect(self.updating)
        self.track_button.clicked.connect(self.tracking)

    def name(self):
        name=self.name_input.text().strip()
        deadline=self.deadline_input.date().toString("dd-mm-yy")
        content=self.content_input.text().strip()

        if not name:
            QMessageBox.warning(self,"Error","Please Enter a name to proceed")
            return
        else:
            self.tasks[name]={"name": name,"Deadline": deadline,"Content": content}
            QMessageBox.information(self,"Success",f"Name {name} has been added")
    
    def updating(self):
        name=self.name_input.text().strip()
        deadline=self.deadline_input.date().toString("dd-mm-yy")
        content=self.content_input.text().strip()

        if not name:
            QMessageBox.warning(self,"Error","Please Enter a name to proceed")
            return
        else:
            self.tasks={"name": name,"Deadline": deadline,"Content": content}
            QMessageBox.information(self,"Success",f"Name {name} has been updated")

    def tracking(self):
        self.tasks.clear()
        for name, info in self.tasks.items():
            self.tasks(f"{name} — Deadline: {info['Deadline']} — {info['Content']}")
    
    def completed(self):
        self.tasks.clear()
app=QApplication(sys.argv)
window=ToDoList()
window.show()
sys.exit(app.exec())