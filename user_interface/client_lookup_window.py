__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Keith Robles"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount
from PySide6.QtCore import Slot

class ClientLookupWindow(LookupWindow):
    """
    EventHandler Class
    """
    def __init__(self):
        """
        Initializes an instance of ClientLookupWindow
        """
        super().__init__()
        # Loads and Sets Values of client_listing and accounts
        data = load_data()
        self.__client_listing = data[0]
        self.__accounts = data[1]

        # Signals
        self.lookup_button.clicked.connect(self.on_lookup_client)
        #self.client_number_edit.textChanged.connect(self.on_text_changed)
        #self.account_table.cellClicked.connect(self.on_select_account)

    @Slot()
    def on_lookup_client(self) -> None:
        # Obtains Client Information
        try:
            client_number = int(self.client_number_edit.text())
        except ValueError:
            result = QMessageBox.information(self, "Input Error", 
                                             "The client number must be numeric.",
                                             QMessageBox.Ok)
            if result == QMessageBox.Ok:
                self.reset_display()
                return
        try:
            client = self.__client_listing[client_number]
        except KeyError:
            result = QMessageBox.information(self, "Not Found",
                                             "Client number: " +
                                             f"{client_number} not found.",
                                             QMessageBox.Ok)
            if result == QMessageBox.Ok:
                self.reset_display()
                return

        # Display Data to the screen
        self.client_info_label.setText(f"Client Name: {client.first_name} " +
                                       f"{client.last_name}")
        

        for account in self.__accounts.values():
            row_position = self.account_table.rowCount() # Checks for Row Count 
            if account.client_number == client.client_number:
                self.account_table.insertRow(row_position) # Adds new Row
                # Converts each data into a str for setItem
                acc_num = str(account.account_number)
                acc_num_item = QTableWidgetItem(acc_num)
                balance = str(account.balance)
                bal_item = QTableWidgetItem(balance)
                date_created = str(account._date_created)
                d_created_item = QTableWidgetItem(date_created)
                account_type = str(account.__class__.__name__)
                acc_type_item = QTableWidgetItem(account_type)
                # Sets the Item Contents
                self.account_table.setItem(row_position, 0, acc_num_item)
                self.account_table.setItem(row_position, 1, bal_item)
                self.account_table.setItem(row_position, 2, d_created_item)
                self.account_table.setItem(row_position, 3, acc_type_item)
                # Resizes the Columns to fit contents
                self.account_table.resizeColumnsToContents()
    