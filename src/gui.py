from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QFileDialog, QMessageBox, QHBoxLayout, QSizePolicy
from toggle_switch import ToggleSwitch
from create_project_structure import *

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Directory Structure Creator'
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(800, 600)
        
        layout = QVBoxLayout()
        
        # Root directory selection
        self.root_dir_label = QLabel("Select root directory:")
        layout.addWidget(self.root_dir_label)
        
        self.root_dir_button = QPushButton("Browse")
        self.root_dir_button.clicked.connect(self.browse_directory)
        layout.addWidget(self.root_dir_button)
        
        self.root_dir_path = QLineEdit(self)
        layout.addWidget(self.root_dir_path)
        
        # Mode selection switch
        self.mode_switch_label = QLabel("Toggle for File Upload or Text Input")
        layout.addWidget(self.mode_switch_label)
        
        self.mode_switch = ToggleSwitch(self)
        self.mode_switch.clicked.connect(self.toggle_mode)
        layout.addWidget(self.mode_switch)
        
        # Structure input
        self.structure_label = QLabel("Enter structure:")
        layout.addWidget(self.structure_label)
        
        self.structure_text = QTextEdit(self)
        layout.addWidget(self.structure_text)
        
        # Upload button
        self.upload_button = QPushButton("Upload File")
        self.upload_button.clicked.connect(self.upload_file)
        layout.addWidget(self.upload_button)
        
        # Create structure button
        self.create_button = QPushButton("Create Structure")
        self.create_button.clicked.connect(self.create_structure)
        layout.addWidget(self.create_button)
        
        self.setLayout(layout)
        
        # Set initial mode to Text Input
        self.toggle_mode()
        
    def browse_directory(self):
        dir_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if dir_path:
            self.root_dir_path.setText(dir_path)
    
    def upload_file(self):
        file_path = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")[0]
        if file_path:
            self.file_path = file_path
    
    def toggle_mode(self):
        if self.mode_switch.isChecked():
            self.structure_label.hide()
            self.structure_text.hide()
            self.upload_button.show()
        else:
            self.structure_label.show()
            self.structure_text.show()
            self.upload_button.hide()
    
    def create_structure(self):
        root_dir = self.root_dir_path.text()
        
        if not root_dir:
            QMessageBox.critical(self, "Error", "Please select a root directory.")
            return
        
        try:
            if self.mode_switch.isChecked():
                if not hasattr(self, 'file_path') or not self.file_path:
                    QMessageBox.critical(self, "Error", "Please upload a file.")
                    return
                create_structure_from_file(self.file_path, root=root_dir)
            else:
                structure = self.structure_text.toPlainText().strip()
                if not structure:
                    QMessageBox.critical(self, "Error", "Please enter a structure.")
                    return
                create_structure(structure, root=root_dir)
            
            QMessageBox.information(self, "Success", "Directory structure created successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")