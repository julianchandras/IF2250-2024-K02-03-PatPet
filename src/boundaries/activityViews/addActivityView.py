from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTimeEdit, QPushButton, QTableWidget,QGroupBox, QGridLayout
from PyQt5.QtGui import QFont


class AddAcitivtyPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        screen_geometry = QApplication.desktop().availableGeometry()

        self.setWindowTitle('Food Entry')
        self.show()

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)

        # Sidebar
        sidebar_width = screen_geometry.width() // 6

        sidebar_widget = QWidget(self)
        sidebar_widget.setFixedWidth(sidebar_width)

        sidebar_layout = QVBoxLayout(sidebar_widget)

        sidebar_label = QLabel('Sidebar', self)
        sidebar_label.setStyleSheet('font-size: 48px; color: #1A646B; font-weight: bold')
        sidebar_label.setFont(QFont('Arial', 14))

        sidebar_layout.addWidget(sidebar_label)

        main_layout.addWidget(sidebar_widget)

        # Main area
        main_content_widget = QWidget(self)  # Create a widget to contain the main content
        main_content_layout = QVBoxLayout(main_content_widget)
        main_content_layout.setContentsMargins(115, 42, 115, 0)

        # Set background color for the main content widget
        main_content_widget.setStyleSheet('background-color: #C0E9DF;')

        title_label = QLabel('Jadwal', self)
        title_label.setStyleSheet('font-size: 48px; color: #1A646B; font-weight: bold;')
        title_label.setContentsMargins(0, 0, 0, 28)
        main_content_layout.addWidget(title_label)


        # Create a QGroupBox
        activity_entry_box = QGroupBox('', self)
        activity_entry_box.setStyleSheet("background-color: white; border-radius: 8px;")

        # Create a QGridLayout for the QGroupBox
        activity_entry_box_layout = QGridLayout(activity_entry_box)
        activity_entry_box.setLayout(activity_entry_box_layout)

        # Create labels
        pilihan_hewan_label = QLabel('Pilihan Hewan')
        jenis_aktivitas_hewan_label = QLabel('Jenis Aktivitas Hewan: ')
        tanggal_mulai_label = QLabel('Tangaal Mulai:')
        tanggal_akhir_label = QLabel('Tanggal Selesai:')
        tanggal_mulai_pengulangan_label = QLabel("Tanggal Mulai Pengulangan")
        tanggal_akhir_pengulangan_label = QLabel("Tanggal Akhir Pengulangan")
        jam_mulai_label = QLabel("Jam Mulai")
        jam_akhir_label = QLabel("Jam Selesai")
        banyak_pengulangan_label = QLabel("Banyaknya Pengulangan")
        
        # Pilih hewan
        self.pilihan_hewan = CustomComboBox()

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
        self.banyak_pengulanagan_input = CustomLineEdit()

        # Create button
        self.button = QPushButton('Button')

        # Create grid layout
        activity_entry_box_layout.addWidget(pilihan_hewan_label, 0, 0, 1, 2)
        activity_entry_box_layout.addWidget(jenis_aktivitas_hewan_label, 0, 2, 1, 2)
        activity_entry_box_layout.addWidget(self.pilihan_hewan,1,0)
        activity_entry_box_layout.addWidget(self.jenis_aktivitas_input,1,1)

        activity_entry_box_layout.addWidget(tanggal_mulai_label,2,0)
        activity_entry_box_layout.addWidget(jam_mulai_label,2,1)
        activity_entry_box_layout.addWidget(tanggal_mulai_pengulangan_label,2,2)
        activity_entry_box_layout.addWidget(banyak_pengulangan_label,2,3)
        
        activity_entry_box_layout.addWidget(self.tanggal_mulai_input,3,0)
        activity_entry_box_layout.addWidget(self.jam_mulai_input,3,1)
        activity_entry_box_layout.addWidget(self.tanggal_akhir_ulang_input,3,2)
        activity_entry_box_layout.addWidget(self.banyak_pengulanagan_input,4,3)

        activity_entry_box_layout.addWidget(tanggal_akhir_label,4,0)
        activity_entry_box_layout.addWidget(jam_akhir_label,4,1)
        activity_entry_box_layout.addWidget(tanggal_akhir_pengulangan_label,4,2)

        activity_entry_box_layout.addWidget(self.tanggal_akhir_input,5,0)
        activity_entry_box_layout.addWidget(self.jam_akhir_input,5,1)
        
        activity_entry_box_layout.addWidget(self.button,6,2)
        



        main_content_layout.addWidget(activity_entry_box)


        self.food_table = QTableWidget(self)
        self.food_table.setStyleSheet('font-size: 14px; border: 1px solid #ccc; border-radius: 5px; background-color: white;')
        main_content_layout.addWidget(self.food_table)

        main_layout.addWidget(main_content_widget)  # Add the main content widget to the main layout

        self.setLayout(main_layout)

        
    