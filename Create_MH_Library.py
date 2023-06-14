import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox, QAction
import lib_transfer as lt

'''
Create Mass Hunter library for quantifiaction from MassOmics library summary file and MCF library in Agilent Library edit format. 
'''

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        

    def initUI(self):
        self.setWindowTitle('Mass Hunter Library Creator')
        self.resize(480,320)

        mass_hunter_label = QLabel('Mass Hunter Library File (.mslibrary.xml)', self)
        mass_hunter_label.resize(300,30)
        mass_hunter_label.move(30, 30)

        self.mass_hunter_input = QLineEdit(self)
        self.mass_hunter_input.move(30, 60)
        self.mass_hunter_input.resize(260, 30)

        mass_hunter_browse = QPushButton('Browse', self)
        mass_hunter_browse.move(300, 60)
        mass_hunter_browse.clicked.connect(self.browse_mass_hunter)

        mass_omic_label = QLabel('Mass Omic Library Summary (.csv)', self)
        mass_omic_label.resize(300,30)
        mass_omic_label.move(30, 100)        

        self.mass_omic_input = QLineEdit(self)
        self.mass_omic_input.move(30, 130)
        self.mass_omic_input.resize(260, 30)

        mass_omic_browse = QPushButton('Browse', self)
        mass_omic_browse.move(300, 130)
        mass_omic_browse.clicked.connect(self.browse_mass_omic)

        output_label = QLabel('Output library file (.mslibrary.xml)', self)
        output_label.resize(300,30)
        output_label.move(30, 170)

        self.output_file_input = QLineEdit(self)
        self.output_file_input.move(30, 200)
        self.output_file_input.resize(260, 30)

        out_file_browse = QPushButton('Browse', self)
        out_file_browse.move(300, 200)
        out_file_browse.clicked.connect(self.browse_output_file)

        create_library = QPushButton('Create Library', self)
        create_library.move(30, 240)
        create_library.clicked.connect(self.create_library)

                # Create the help menu
        self.help_menu = self.menuBar().addMenu("Help")

        # Create the about action
        self.about_action = QAction("About", self)
        self.about_action.triggered.connect(self.show_about_message)

        # Add the about action to the help menu
        self.help_menu.addAction(self.about_action)

        self.show()

    def show_about_message(self):
        QMessageBox.about(self, "About", "MassHunter Library creator for MassOmics.\n Tony Chen\n 2023\nhttps://github.com/boloson/OmicHelper")
        # # Create a QMessageBox object
        # msg_box = QMessageBox()

        # # Set the message text
        # msg_box.setText("This is a sample PyQt5 application.")

        # # Show the message box
        # msg_box.show()


    def browse_mass_hunter(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Mass Hunter Library File", "",
                                                   "All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            self.mass_hunter_input.setText(file_name)

    def browse_mass_omic(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Mass Omic Library Summary", "",
                                                   "All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            self.mass_omic_input.setText(file_name)

    def browse_output_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getSaveFileName(self, 'Output Mass Hunter library', '', 'All Files (*);; MS library (*.mslibrary.xml)', options=options)

        if file_name:
            if not file_name.endswith("mslibrary.xml"):
                file_name = file_name+".mslibrary.xml"
            self.output_file_input.setText(file_name)

    def add_suffix(self, file_name):
        file_name = self.output_file_input.text()
        if not file_name.endswith('.mslibrary.xml'):
            file_name = file_name + '.mslibrary.xml'
        return file_name
    

    def create_library(self):
        # print(self.mass_hunter_input.text())
        mass_hunter_lib = self.mass_hunter_input.text()
        summary_report = self.mass_omic_input.text()
        output_file = self.add_suffix(self.output_file_input.text())

        try:
            lt.create_library_from_summary(mass_hunter_lib, summary_report, output_file)
            QMessageBox.information(self, 'Success', 'A Mass Hunter library was successfully created at the location: {}'.format(output_file))
        except Exception as e:
            QMessageBox.warning(self, 'Error', str(e)) 

            

app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())
