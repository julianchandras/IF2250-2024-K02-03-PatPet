from PyQt5.QtWidgets import QScrollArea,QFrame, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTimeEdit, QPushButton, QTableWidget,QGroupBox, QGridLayout
from PyQt5.QtCore import Qt,pyqtSignal
from components.calendarInput import CalendarInput
from components.customQLine import CustomLineEdit
from components.customComboBox import CustomComboBox
from components.customSchedule import CustomSchedule
from datetime import datetime


class AddActivityView(QWidget):
    add_activity_signal = pyqtSignal(str, datetime, datetime, int)
    navigate_to_update = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # self.activites = {}
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)

        # Main area
        main_content_widget = QWidget(self)  # Create a widget to contain the main content
        main_content_layout = QVBoxLayout(main_content_widget)
        main_content_layout.setContentsMargins(115, 42, 115, 50)

        # Set background color for the main content widget
        main_content_widget.setStyleSheet('background-color: #C0E9DF;')

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
        activity_entry_box.setFixedHeight(500)
        activity_entry_box.setStyleSheet("background-color: white; border-radius: 8px;")

        # Create a QGridLayout for the QGroupBox
        activity_entry_box_layout = QGridLayout(activity_entry_box)
        activity_entry_box.setLayout(activity_entry_box_layout)

        # Create labels
        pilihan_hewan_label = QLabel('Pilihan Hewan')
        jenis_aktivitas_hewan_label = QLabel('Jenis Aktivitas Hewan: ')
        tanggal_mulai_label = QLabel('Tanggal Mulai:')
        tanggal_akhir_label = QLabel('Tanggal Selesai:')
        tanggal_mulai_pengulangan_label = QLabel("Tanggal Mulai Pengulangan")
        tanggal_akhir_pengulangan_label = QLabel("Tanggal Akhir Pengulangan")
        jam_mulai_label = QLabel("Jam Mulai")
        jam_akhir_label = QLabel("Jam Selesai")
        banyak_pengulangan_label = QLabel("Banyaknya Pengulangan")
        
        # Pilih hewan
        self.pilihan_hewan = CustomComboBox()

        # Masukin pilihan hewan
        for i in range(3):
            self.pilihan_hewan.addItems([f"{i}"])

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
        self.tanggal_akhir_input = CalendarInput()
        self.tanggal_mulai_ulang_input = CalendarInput()
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
                padding: 20px 5px;
                color : white;
                
            }

            QPushButton:hover {
                background-color: #6E9DA1;
            }
        """)

        # Create grid layout
        activity_entry_box_layout.addWidget(pilihan_hewan_label, 0, 0, 1, 2)
        activity_entry_box_layout.addWidget(jenis_aktivitas_hewan_label, 0, 2, 1, 2)
        activity_entry_box_layout.addWidget(self.pilihan_hewan,1,0)
        activity_entry_box_layout.addWidget(self.jenis_aktivitas_input,1,2)

        activity_entry_box_layout.addWidget(tanggal_mulai_label,2,0)
        activity_entry_box_layout.addWidget(jam_mulai_label,2,1)
        activity_entry_box_layout.addWidget(tanggal_mulai_pengulangan_label,2,2)
        activity_entry_box_layout.addWidget(banyak_pengulangan_label,2,3)
        
        activity_entry_box_layout.addWidget(self.tanggal_mulai_input,3,0)
        activity_entry_box_layout.addWidget(self.jam_mulai_input,3,1)
        activity_entry_box_layout.addWidget(self.tanggal_mulai_ulang_input,3,2)
        activity_entry_box_layout.addWidget(self.banyak_pengulangan_input,3,3)

        activity_entry_box_layout.addWidget(tanggal_akhir_label,4,0)
        activity_entry_box_layout.addWidget(jam_akhir_label,4,1)
        activity_entry_box_layout.addWidget(tanggal_akhir_pengulangan_label,4,2)

        activity_entry_box_layout.addWidget(self.tanggal_akhir_input,5,0)
        activity_entry_box_layout.addWidget(self.jam_akhir_input,5,1)
        activity_entry_box_layout.addWidget(self.tanggal_akhir_ulang_input,5,2)
        
        activity_entry_box_layout.addWidget(self.tambah_button,6,3)
        

        main_content_layout.addWidget(activity_entry_box)


        activities = {
            "2024-05-10": [("09:00", "Bella"), ("10:30", "Max")],
            "2024-05-11": [("11:00", "Charlie"), ("14:00", "Luna mafhjdsakgkjvsduyhrelukjtygdgvjyhkjrdsv yhgksjquicldiwe4ksyh fgiewu"),("15:00", "NUNU"),("16:00", "NEOWOOF"), ("17:00", "Jultara"), ("18:00","macamaca")],
            "2024-05-12": [("09:30", "Rocky")],
            "2024-05-15": [("12:00", "Buddy"), ("16:00", "Lucy")]
        }
        self.activity_table = QWidget()
        self.activity_table_layout = QVBoxLayout(self.activity_table)
        self.activity_table.setStyleSheet("""
            font-size: 14px; 
            border:none; 
            border-radius: 10px; 
            background-color: white;
        """)

        self.calendar = CustomSchedule()
        self.calendar.set_activities(activities)
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

    def set_activities(self,activities):
        pass

        

        
    