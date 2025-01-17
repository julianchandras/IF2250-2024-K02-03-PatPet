from PyQt5.QtWidgets import QApplication,QScrollArea,QFrame, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTimeEdit, QPushButton, QTableWidget,QGroupBox, QGridLayout, QMessageBox
from PyQt5.QtCore import Qt,pyqtSignal, QTime, QDate
from components.calendarInput import CalendarInput
from components.customQLine import CustomLineEdit
from components.customComboBox import CustomComboBox
from components.customSchedule import CustomSchedule
from datetime import date
from utils.font import *
from utils.screensize import *

class AddActivityView(QWidget):
    add_activity_signal = pyqtSignal(str, date,  str, str, date, int, int)
    navigate_to_update = pyqtSignal(int)
    

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
        main_content_widget.setStyleSheet('background-color: #C0E9DF; border:none;')

        title_label = QLabel('Jadwal', self)
        title_label.setStyleSheet('color: #1A646B; font-weight: 900;')
        title_label.setFont(set_font("bold",24))
        title_label.setFixedHeight(int(getHeight() * 0.05))
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
        jenis_aktivitas_hewan_label = QLabel('Jenis Aktivitas Hewan')
        tanggal_aktivitas_label = QLabel('Tanggal Aktivitas')
        tanggal_akhir_pengulangan_label = QLabel("Tanggal Akhir Pengulangan")
        jam_mulai_label = QLabel("Jam Mulai")
        jam_akhir_label = QLabel("Jam Selesai")
        banyak_pengulangan_label = QLabel("Interval Pengulangan")
        
        for label in [pilihan_hewan_label,jenis_aktivitas_hewan_label,tanggal_aktivitas_label,tanggal_akhir_pengulangan_label,jam_mulai_label,jam_akhir_label,banyak_pengulangan_label]:
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
        self.tanggal_aktivitas = CalendarInput()
        self.tanggal_akhir_ulang_input = CalendarInput()

        # Banyak pengulangan
        self.banyak_pengulangan_input = CustomLineEdit()

        # Create button
        self.tambah_button = QPushButton('Tambah')
        self.tambah_button.setStyleSheet("""
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
        if (getHeight() > 1080):
            self.tambah_button.setFixedHeight(int(getHeight() * 0.05))
            activity_entry_box.setFixedHeight(int(screen_geometry.height() * 0.225))
        else:
            self.tambah_button.setFixedHeight(int(getHeight() * 0.04))

        self.tambah_button.setFont(set_font("bold",12))
        self.tambah_button.clicked.connect(self.add_activity)

        # Create grid layout
        activity_entry_box_layout.addWidget(pilihan_hewan_label, 0, 0, 1,2)
        activity_entry_box_layout.addWidget(jenis_aktivitas_hewan_label, 0, 2, 1, 2)
        activity_entry_box_layout.addWidget(banyak_pengulangan_label,0,4, 1,2 )

        activity_entry_box_layout.addWidget(self.pilihan_hewan, 1, 0, 1,2)
        activity_entry_box_layout.addWidget(self.jenis_aktivitas_input, 1, 2, 1, 2)
        activity_entry_box_layout.addWidget(self.banyak_pengulangan_input,1,4, 1,2)

        activity_entry_box_layout.addWidget(tanggal_aktivitas_label,2,0,1,2)
        activity_entry_box_layout.addWidget(jam_mulai_label,2,2)
        activity_entry_box_layout.addWidget(jam_akhir_label,2,3)
        activity_entry_box_layout.addWidget(tanggal_akhir_pengulangan_label,2,4,1,2)

        
        activity_entry_box_layout.addWidget(self.tanggal_aktivitas,3,0,1,2)
        activity_entry_box_layout.addWidget(self.jam_mulai_input,3,2)
        activity_entry_box_layout.addWidget(self.jam_akhir_input,3,3 )
        activity_entry_box_layout.addWidget(self.tanggal_akhir_ulang_input,3,4,1,2)

        
        activity_entry_box_layout.addWidget(self.tambah_button,4,4,1,2)
        

        main_content_layout.addWidget(activity_entry_box)


        
        self.activity_table = QWidget()
        self.activity_table_layout = QVBoxLayout(self.activity_table)
        self.activity_table.setStyleSheet("""
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

        self.calendar.activity_clicked.connect(self.navigate_to_update_activity)

    def set_activities(self,activities):
        temp = {}
        for activity in activities:
            activity_id, detail, date_str, start_time, end_time, _, animal, _ = activity
            
            if date_str not in temp:
                temp[date_str] = []
            temp[date_str].append((activity_id,start_time, end_time, animal, detail[:15]))
        self.calendar.set_activities(temp)

    
    def set_pets(self, pets):
        self.pilihan_hewan.addItems(pets)

    def navigate_to_update_activity(self, activity_id):
        self.navigate_to_update.emit(activity_id)

    def add_activity(self):

        if not self.validate_inputs():
            return
        

        pet_id = self.pilihan_hewan.combo_box.currentData()
        activity_name = self.jenis_aktivitas_input.text()
        activity_date = self.tanggal_aktivitas.calendar.selectedDate().toPyDate()
        start_time = self.jam_mulai_input.time().toString()
        end_time = self.jam_akhir_input.time().toString()
        repetition_end = self.tanggal_akhir_ulang_input.calendar.selectedDate()
        if repetition_end.isNull():
            repetition_end = None
        else:
            repetition_end = repetition_end.toPyDate()

        repetition_hop_str = self.banyak_pengulangan_input.text()
        if repetition_hop_str:
            repetition_hop = int(repetition_hop_str)
        else:
            repetition_hop = -1
        self.add_activity_signal.emit(activity_name, activity_date,start_time, end_time, repetition_end, repetition_hop, pet_id)
    
    def validate_inputs(self):
        if self.pilihan_hewan.combo_box.currentIndex() == -1:
            self.show_error_message("Please select an animal.")
            return False

        if not self.jenis_aktivitas_input.text().strip():
            self.show_error_message("Activity name cannot be empty.")
            return False

        if self.tanggal_aktivitas.calendar.selectedDate().isNull():
            self.show_error_message("Please select an activity date.")
            return False

        if self.jam_mulai_input.time() >= self.jam_akhir_input.time():
            self.show_error_message("Start time must be earlier than end time.")
            return False

        if not self.banyak_pengulangan_input.text() == "" and not self.banyak_pengulangan_input.text().isdigit():
            self.show_error_message("Repetition must be a number")
            return False
        return True

    def clear_input(self):
        self.jenis_aktivitas_input.clear()
        self.banyak_pengulangan_input.clear()

        self.tanggal_aktivitas.calendar.setSelectedDate(QDate(date.today()))
        self.tanggal_aktivitas.line_edit.clear()
        self.tanggal_aktivitas.line_edit.setPlaceholderText("Click to select date")
        self.jam_mulai_input.setTime(QTime(0,0))
        self.jam_akhir_input.setTime(QTime(0,0))
        self.tanggal_akhir_ulang_input.calendar.setSelectedDate(QDate(date.today()))
        self.tanggal_akhir_ulang_input.line_edit.clear()
        self.tanggal_akhir_ulang_input.line_edit.setPlaceholderText("Click to select a date")
        self.pilihan_hewan.combo_box.setCurrentIndex(-1)
        self.pilihan_hewan.combo_box.setEditText('Pilih hewan')

    def show_error_message(self, message):
        QMessageBox.warning(self, "Input Error", message, QMessageBox.Ok)

    