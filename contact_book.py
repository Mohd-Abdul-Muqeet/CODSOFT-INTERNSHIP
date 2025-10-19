import sys
from PyQt6.QtWidgets import QListWidget,QMessageBox,QHBoxLayout,QVBoxLayout,QWidget,QApplication,QRadioButton,QLabel,QLayout,QPushButton,QLineEdit,QCheckBox,QComboBox

class ContactApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CONTACT BOOK")
        self.setGeometry(100,100,500,500)

        self.contacts={}

        self.name_label=QLabel("Name: ")
        self.name_input=QLineEdit()

        self.phone_label=QLabel("Phone no: ")
        self.phone_input=QLineEdit()

        self.email_label=QLabel("Email: ")
        self.email_input=QLineEdit()

        self.address_label=QLabel("Adress: ")
        self.address_input=QLineEdit()

        self.add_button=QPushButton("Add Contact: ")
        self.update_button=QPushButton("Update Contact: ")
        self.delete_button=QPushButton("Delete Contact: ")
        self.view_button=QPushButton("View All contacts: ")
        self.search_button=QPushButton("Search a Contact: ")

        self.contact_list=QListWidget()

        layout=QVBoxLayout()

        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.address_label)
        layout.addWidget(self.address_input)

        btn_layout=QHBoxLayout()
        btn_layout.addWidget(self.add_button)
        btn_layout.addWidget(self.update_button)
        btn_layout.addWidget(self.delete_button)
        layout.addLayout(btn_layout)

        layout.addWidget(self.search_button)
        layout.addWidget(self.view_button)
        layout.addWidget(self.contact_list)

        self.setLayout(layout)

        self.add_button.clicked.connect(self.add_contact)
        self.update_button.clicked.connect(self.update_contact)
        self.delete_button.clicked.connect(self.delete_contact)
        self.search_button.clicked.connect(self.search_contact)
        self.view_button.clicked.connect(self.view_contacts)

    def add_contact(self):
        name=self.name_input.text().strip()
        phone=self.phone_input.text().strip()
        email=self.email_input.text().strip()
        adress=self.address_input.text().strip()

        if not name or not phone:
            QMessageBox.warning(self,"Error","Name and Phone are required")
            return
        
        self.contacts[name] = {"phone": phone,"email": email,"address": adress,}
        QMessageBox.information(self,"Success",f"Contact '{name}' added!")
        self.clear_inputs()
        self.view_contacts()

    def clear_inputs(self):
        self.name_input.clear()
        self.phone_input.clear()
        self.email_input.clear()
        self.address_input.clear()
    
    def view_contacts(self):
        self.contact_list.clear()
        for name, info in self.contacts.items():
            self.contact_list.addItem(f"{name} - {info['phone']}")

    def search_contact(self):
        term = self.name_input.text().strip()
        self.contact_list.clear()
        found = False
        for name, info in self.contacts.items():
            if term.lower() in name.lower() or term in info["phone"] or term in info["email"] or term in info["address"]:
                self.contact_list.addItem(f"{name} - {info['phone']},{info['email']},{info['address']}")
                found = True
        if not found:
            QMessageBox.information(self, "Search Result", "No contacts found!")

    def update_contact(self):
        print("Update button clicked")  
        name = self.name_input.text().strip()
        if name not in self.contacts:
            QMessageBox.warning(self, "Error", "Contact not found!")
            return
        self.contacts[name]["phone"] = self.phone_input.text().strip()
        self.contacts[name]["email"] = self.email_input.text().strip()
        self.contacts[name]["address"] = self.address_input.text().strip()
        QMessageBox.information(self, "Success", f"Contact '{name}' updated!")
        self.clear_inputs()
        self.view_contacts()

    def delete_contact(self):
        name = self.name_input.text().strip()
        if name in self.contacts:
            del self.contacts[name]
            QMessageBox.information(self, "Deleted", f"Contact '{name}' deleted!")
            self.clear_inputs()
            self.view_contacts()
        else:
            QMessageBox.warning(self, "Error", "Contact not found!")

app=QApplication(sys.argv)
window=ContactApp()
window.show()
sys.exit(app.exec())