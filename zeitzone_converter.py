# Import necessary libraries
from datetime import datetime
from pytz import timezone, common_timezones
from PyQt5 import QtWidgets, QtCore

# Define the ZeitzoneConverter class
class ZeitzoneConverter(QtWidgets.QWidget):

    # Initialize the class
    def __init__(self):

        # Call the parent constructor
        super().__init__()

        # Set the window title and geometry
        self.setWindowTitle("Zeitzonen-Konverter")
        self.setGeometry(100, 100, 400, 300)

        # Set the standard timezone to 'Europe/Berlin'
        self.standard_tz = timezone('Europe/Berlin')

        # Create a label for the standard timezone dropdown
        standard_tz_label = QtWidgets.QLabel("Standard-Zeitzone:")

        # Create a dropdown for the standard timezone
        self.standard_tz_dropdown = QtWidgets.QComboBox()
        self.standard_tz_dropdown.addItems(common_timezones)
        self.standard_tz_dropdown.setCurrentText('Europe/Berlin')

        # Create a label for the selected timezone dropdown
        selected_tz_label = QtWidgets.QLabel("Zweite Zeitzone:")

        # Create a dropdown for the selected timezone
        self.selected_tz_dropdown = QtWidgets.QComboBox()
        self.selected_tz_dropdown.addItems(common_timezones)
        self.selected_tz_dropdown.setCurrentText('UTC')

        # Create labels for the current time and the selected time
        self.time_label = QtWidgets.QLabel("")
        self.selected_time_label = QtWidgets.QLabel("")

        # Create a button to update the time
        update_btn = QtWidgets.QPushButton("Aktualisieren")
        update_btn.clicked.connect(self.update_time)

        # Create a vertical layout and add the elements to it
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(standard_tz_label)
        layout.addWidget(self.standard_tz_dropdown)
        layout.addWidget(selected_tz_label)
        layout.addWidget(self.selected_tz_dropdown)
        layout.addWidget(self.time_label)
        layout.addWidget(self.selected_time_label)
        layout.addWidget(update_btn)

        # Set the layout for the widget
        self.setLayout(layout)

        # Call the update_time method to initialize the time labels
        self.update_time()

    # Define the update_time method to update the time labels
    def update_time(self):

        # Get the current time in the standard timezone
        current_time = datetime.now(self.standard_tz)

        # Set the text of the time label to the current time in the standard timezone
        self.time_label.setText(current_time.strftime('%d.%m.%Y %H:%M:%S'))

        # Get the selected timezone from the dropdown
        selected_tz = timezone(self.selected_tz_dropdown.currentText())

        # Convert the current time to the selected timezone
        selected_time = current_time.astimezone(selected_tz)

        # Set the text of the selected time label to the converted time
        self.selected_time_label.setText(selected_time.strftime('%d.%m.%Y %H:%M:%S'))

        # Set a timer to call the update_time method again in 1000 milliseconds (1 second)
        QtCore.QTimer.singleShot(1000, self.update_time)

# If the script is being run directly, create an instance of the ZeitzoneConverter class and show it
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    converter = ZeitzoneConverter()
    converter.show()

    # Start the event loop
    sys.exit(app.exec_())
