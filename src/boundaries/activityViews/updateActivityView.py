from PyQt5.QtWidgets import QApplication, QFrame, QScrollArea, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTimeEdit, QPushButton, QTableWidget,QGroupBox, QGridLayout, QMessageBox
from PyQt5.QtCore import Qt,pyqtSignal, QTime, QDate
from components.calendarInput import CalendarInput
from components.customQLine import CustomLineEdit
from components.customComboBox import CustomComboBox
from components.customSchedule import CustomSchedule
from datetime import date, datetime
from utils.font import *
from utils.screensize import *

class UpdateActivityView(QWidget):

    update_activity_signal = pyqtSignal(int, str, date,  str,str, int)
    delete_activity_signal = pyqtSignal(int)
    navigate_to_update = pyqtSignal(int)
    cancel_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        screen_geometry = QApplication.desktop().availableGeometry()

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)

        # Main area
        main_content_widget = QWidget(self)  # Create a widget to contain the main content
        main_content_layout = QVBoxLayout(main_content_widget)
        main_content_layout.setContentsMargins(115, 42, 115, 50)

        # Set background color for the main content widget
        main_content_widget.setStyleSheet('background-color: #C0E9DF; border:none')

        title_label = QLabel('Edit Jadwal', self)
        title_label.setStyleSheet('color: #1A646B; font-weight: 900;')
        title_label.setFont(set_font("bold",24))
        title_label.setFixedHeight(70)
        main_content_layout.addWidget(title_label)
        
        line_frame = QFrame(self)
        line_frame.setFrameShape(QFrame.HLine)
        line_frame.setFrameShadow(QFrame.Sunken)
        line_frame.setLineWidth(2)
        line_frame.setMidLineWidth(4)
        line_frame.setStyleSheet("border: 2px solid #1A646B;")
        line_frame.setContentsMargins(0, 0, 0, 30)

        main_content_layout.addWidget(line_frame)

        # Create a QGroupBox
        activity_entry_box = QGroupBox('', self)
        activity_entry_box.setFixedHeight(int(screen_geometry.height() * 0.25))
        activity_entry_box.setStyleSheet("background-color: white; border-radius: 8px;")

        # Create a QGridLayout for the QGroupBox
        activity_entry_box_layout = QGridLayout(activity_entry_box)
        activity_entry_box.setLayout(activity_entry_box_layout)

        # Create labels
        pilihan_hewan_label = QLabel('Pilihan Hewan')
        jenis_aktivitas_hewan_label = QLabel('Jenis Aktivitas Hewan: ')
        tanggal_mulai_label = QLabel('Tanggal Mulai:')
        jam_mulai_label = QLabel("Jam Mulai")
        jam_akhir_label = QLabel("Jam Selesai")
        
        for label in [pilihan_hewan_label,jenis_aktivitas_hewan_label,tanggal_mulai_label,jam_akhir_label,jam_mulai_label]:
            label.setStyleSheet("font-weight:bold;margin:0px;")
            if (getHeight() > 1080):
                label.setFont(set_font("bold",12))
            else:
                label.setFont(set_font("bold",10))

        # Pilih hewan
        self.pilihan_hewan = CustomComboBox()


        # Jenis Aktivtias
        self.jenis_aktivitas_input = CustomLineEdit()
        

        # Jam Mulai
        self.jam_mulai_input = QTimeEdit()
        self.jam_mulai_input.setDisplayFormat("HH:mm")
        self.jam_mulai_input.setFont(set_font("regular",12))

        # Jam akhir
        self.jam_akhir_input = QTimeEdit()
        self.jam_akhir_input.setDisplayFormat("HH:mm")
        self.jam_akhir_input.setFont(set_font("regular",12))

        if (getHeight() > 1080):
            self.jam_mulai_input.setStyleSheet("QTimeEdit { border-radius: 8px; border:2px solid #D4D4D4; padding: 8px;}")
            self.jam_akhir_input.setStyleSheet("QTimeEdit { border-radius: 8px; border: 2px solid #D4D4D4; padding:8px;}")
        else:
            self.jam_mulai_input.setStyleSheet("QTimeEdit { border-radius: 8px; border:2px solid #D4D4D4; padding: 5px;}")
            self.jam_akhir_input.setStyleSheet("QTimeEdit { border-radius: 8px; border: 2px solid #D4D4D4; padding:5px;}")

        # Tanggal
        self.tanggal_mulai_input = CalendarInput()

        # Create button
        self.ubah_button = QPushButton('Ubah')
        self.ubah_button.setStyleSheet("""
            QPushButton {
                background-color: #1A646B;
                font-weight: bold;
                border-radius: 8px;
                color : white;
                
            }

            QPushButton:hover {
                background-color: #6E9DA1;
            }
        """)

        self.hapus_button = QPushButton('Hapus')
        self.hapus_button.setStyleSheet("""
            QPushButton {
                background-color: #F277AD;
                font-weight: bold;
                border-radius: 8px;
                color : white;
                
            }

            QPushButton:hover {
                background-color: #F8B8D4;
            }
        """)

        self.cancel_button = QPushButton('Batal')
        self.cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #FF0000;
                font-weight: bold;
                border-radius: 8px;
                color: white;
            }
            QPushButton:hover {
                background-color: #FF6666;
            }
        """)

        for button in [self.cancel_button,self.ubah_button,self.hapus_button]:
            button.setFont(set_font("bold",12))
            button.setFixedHeight(int(getHeight() * 0.04))

        if (getHeight() > 1080):
            self.ubah_button.setFixedHeight(int(getHeight() * 0.05))
            self.cancel_button.setFixedHeight(int(getHeight() * 0.05))
            self.hapus_button.setFixedHeight(int(getHeight() * 0.05))
            activity_entry_box.setFixedHeight(int(screen_geometry.height() * 0.25))
        # Create grid layout
        activity_entry_box_layout.addWidget(pilihan_hewan_label, 0, 0, 1, 2)
        activity_entry_box_layout.addWidget(jenis_aktivitas_hewan_label, 0, 2, 1, 2)
        
        activity_entry_box_layout.addWidget(self.pilihan_hewan,1,0,1,2)
        activity_entry_box_layout.addWidget(self.jenis_aktivitas_input,1,2,1,2)

        activity_entry_box_layout.addWidget(tanggal_mulai_label,2,0,1,2)
        activity_entry_box_layout.addWidget(jam_mulai_label,2,2)
        activity_entry_box_layout.addWidget(jam_akhir_label,2,3)
        
        activity_entry_box_layout.addWidget(self.tanggal_mulai_input,3,0,1,2)
        activity_entry_box_layout.addWidget(self.jam_mulai_input,3,2)
        activity_entry_box_layout.addWidget(self.jam_akhir_input,3,3)
        
        activity_entry_box_layout.addWidget(self.ubah_button,3,4)
        activity_entry_box_layout.addWidget(self.hapus_button,3,5)
        activity_entry_box_layout.addWidget(self.cancel_button,4,5)
        

        main_content_layout.addWidget(activity_entry_box)


    
        self.activity_table = QWidget()
        self.activity_table_layout = QVBoxLayout(self.activity_table)
        self.activity_table.setStyleSheet("""
            font-size: 14px; 
            border:none; 
            border-radius: 10px; 
            background-color: white;
        """)

        self.calendar = CustomSchedule()
        self.activity_table_layout.addWidget(self.calendar)
        self.activity_table.setContentsMargins(0, 0, 0, 0)
        
        main_content_layout.addWidget(self.activity_table)
        # Wrap the main content widget with a QScrollArea
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)  # Set scrollbar policy

        # Set the main content widget as the scroll area's widget
        scroll_area.setWidget(main_content_widget)
        scroll_area.setStyleSheet('''
            QScrollBar:vertical {
                border: none;
                background: #f0f0f0;
                width: 10px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: #c0c0c0;
                min-height: 20px;
            }
            QScrollBar::handle:vertical:hover {
                background: #a0a0a0;
            }
            QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
            QScrollBar::add-line:vertical {
                border: none;
                background: none;
            }
            QScrollBar:horizontal {
                border: none;
                background: #f0f0f0;
                height: 10px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:horizontal {
                background: #c0c0c0;
                min-width: 20px;
            }
            QScrollBar::handle:horizontal:hover {
                background: #a0a0a0;
            }
            QScrollBar::sub-line:horizontal {
                border: none;
                background: none;
            }
            QScrollBar::add-line:horizontal {
                border: none;
                background: none;
            }
        ''')


        main_layout.addWidget(scroll_area) 
        self.setLayout(main_layout)
        self.ubah_button.clicked.connect(self.update_activity)
        self.hapus_button.clicked.connect(self.delete_activity)
        self.cancel_button.clicked.connect(self.cancel_update)
        self.calendar.activity_clicked.connect(self.navigate_to_update_activity)

    
    def set_pets(self,pets):
        self.pilihan_hewan.addItems(pets)


    def set_activities(self,activities):
        temp = {}
        for activity in activities:
            activity_id, detail, date_str, start_time, end_time, _, animal, _ = activity
            
            if date_str not in temp:
                temp[date_str] = []
            temp[date_str].append((activity_id,start_time, end_time, animal, detail[:15]))
        self.calendar.set_activities(temp)

    def set_activity_details(self,activity):


        self.activity_id = activity[0]
        self.jenis_aktivitas_input.setText(activity[1])
        date_parts = activity[2].split('-')
        year, month, day = map(int, date_parts)
        selected_date = QDate(year, month, day)
        
        self.tanggal_mulai_input.calendar.setSelectedDate(selected_date)
        self.tanggal_mulai_input.line_edit.setPlaceholderText(activity[2])
        
        jam_mulai = datetime.strptime(activity[3], "%H:%M:%S")
        jam_akhir = datetime.strptime(activity[4], "%H:%M:%S")

        jam_mulai_hour = jam_mulai.hour
        jam_mulai_minute = jam_mulai.minute
        jam_akhir_hour = jam_akhir.hour
        jam_akhir_minute = jam_akhir.minute


        self.jam_mulai_input.setTime(QTime(jam_mulai_hour, jam_mulai_minute))

        self.jam_akhir_input.setTime(QTime(jam_akhir_hour, jam_akhir_minute))
        
        self.pilihan_hewan.combo_box.setCurrentText(activity[6])
        self.pilihan_hewan.combo_box.setCurrentIndex(self.pilihan_hewan.combo_box.findText(activity[6]))

    def navigate_to_update_activity(self, activity_id):
        self.navigate_to_update.emit(activity_id)

    def update_activity(self):
        activity_id = self.activity_id
        pet_id = self.pilihan_hewan.combo_box.currentData()
        activity_name = self.jenis_aktivitas_input.text()
        start_date = self.tanggal_mulai_input.calendar.selectedDate().toPyDate()
        start_time = self.jam_mulai_input.time().toString()
        end_time = self.jam_akhir_input.time().toString()
        
        ## Validate

        if not self.validate_inputs():
            return
       
        self.update_activity_signal.emit(activity_id, activity_name, start_date,start_time, end_time,pet_id)

    def delete_activity(self):
        self.delete_activity_signal.emit(self.activity_id)
        
    def cancel_update(self):
        self.cancel_signal.emit()
    
    def validate_inputs(self):
        if self.pilihan_hewan.combo_box.currentIndex() == -1:
            self.show_error_message("Please select an animal.")
            return False

        if not self.jenis_aktivitas_input.text().strip():
            self.show_error_message("Activity name cannot be empty.")
            return False

        if self.tanggal_mulai_input.calendar.selectedDate().isNull():
            self.show_error_message("Please select an activity date.")
            return False

        if self.jam_mulai_input.time() >= self.jam_akhir_input.time():
            self.show_error_message("Start time must be earlier than end time.")
            return False

        return True
    
    def show_error_message(self, message):
        QMessageBox.warning(self, "Input Error", message, QMessageBox.Ok)