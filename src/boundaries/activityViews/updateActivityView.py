from PyQt5.QtWidgets import QApplication, QFrame, QScrollArea, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTimeEdit, QPushButton, QTableWidget,QGroupBox, QGridLayout
from PyQt5.QtCore import Qt,pyqtSignal
from components.calendarInput import CalendarInput
from components.customQLine import CustomLineEdit
from components.customComboBox import CustomComboBox
from components.customSchedule import CustomSchedule
from datetime import date

class UpdateActivityView(QWidget):

    update_activity_signal = pyqtSignal(int, str, date,  str,str, int)
    delete_activity_signal = pyqtSignal(int)

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

        title_label = QLabel('Jadwal', self)
        title_label.setStyleSheet('font-size: 48px; color: #1A646B; font-weight: bold;')
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
        activity_entry_box.setFixedHeight(int(screen_geometry.height() * 0.2))
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
        
        # Pilih hewan
        self.pilihan_hewan = CustomComboBox()

        # Masukin pilihan hewan
        

        # Jenis Aktivtias
        self.jenis_aktivitas_input = CustomLineEdit()
        

        # Jam Mulai
        self.jam_mulai_input = QTimeEdit()
        self.jam_mulai_input.setDisplayFormat("HH:mm")
        self.jam_mulai_input.setStyleSheet("QTimeEdit { border-radius: 8px; }")

        # Jam akhir
        self.jam_akhir_input = QTimeEdit()
        self.jam_akhir_input.setDisplayFormat("HH:mm")
        self.jam_akhir_input.setStyleSheet("QTimeEdit { border-radius: 8px; }")

        # Tanggal
        self.tanggal_mulai_input = CalendarInput()

        # Create button
        self.ubah_button = QPushButton('Ubah')
        self.ubah_button.setStyleSheet("""
            QPushButton {
                background-color: #1A646B;
                font-weight: bold;
                border-radius: 8px;
                padding: 20px 5px;
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
                padding: 20px 5px;
                color : white;
                
            }

            QPushButton:hover {
                background-color: #F8B8D4;
            }
        """)

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

      

    def update_activity(self):
        activity_id = self.activity_id
        pet_id = self.pilihan_hewan.combo_box.currentData()
        activity_name = self.jenis_aktivitas_input.text()
        start_date = self.tanggal_mulai_input.calendar.selectedDate().toPyDate()
        start_time = self.jam_mulai_input.time().toString()
        end_time = self.jam_akhir_input.time().toString()
       
        self.update_activity_signal.emit(activity_id, activity_name, start_date,start_time, end_time,pet_id)

    def delete_activity(self):
        self.delete_activity_signal.emit(self.activity_id)
        
        
            
    