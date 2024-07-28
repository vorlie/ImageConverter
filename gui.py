from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget,
    QLineEdit, QFileDialog, QComboBox, QCheckBox, QMessageBox, QHBoxLayout, QSpacerItem, QSizePolicy)
from PyQt5.QtGui import QIcon, QCursor, QPixmap
from PyQt5.QtCore import Qt, QTimer
import sys, qdarktheme, os
from module.image_processing import convert_image

icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")

class ImagePreviewWindow(QWidget):
    def __init__(self, pixmap):
        super().__init__()
        self.setWindowTitle("Image Preview")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        self.setMinimumSize(300, 200)
        self.setMaximumSize(1920, 1080)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.image_label = QLabel()
        self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.image_label)
        self.set_pixmap(pixmap)

    def set_pixmap(self, pixmap):
        self.pixmap = pixmap
        self.update_image()

    def update_image(self):
        if self.pixmap:
            scaled_pixmap = self.pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image_label.setPixmap(scaled_pixmap)
            self.image_label.setFixedSize(scaled_pixmap.size()) 

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_image()

class ImageConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Converter")
        self.setFixedSize(400, 310)

        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        self.file_path = None
        self.preview_window = None

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        self.controls_widget = QWidget()
        controls_layout = QVBoxLayout()
        controls_layout.setSpacing(5)
        controls_layout.setContentsMargins(5, 5, 5, 5)
        self.controls_widget.setLayout(controls_layout)
        main_layout.addWidget(self.controls_widget)

        self.selected_file_label = QLabel("No file selected")
        self.selected_file_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        controls_layout.addWidget(self.selected_file_label)

        select_button = QPushButton("Select File")
        select_button.setFixedWidth(150)
        select_button.setCursor(QCursor(Qt.PointingHandCursor))
        select_button.clicked.connect(self.select_file)
        controls_layout.addWidget(select_button)

        self.conversion_format = QComboBox()
        self.conversion_format.setCursor(QCursor(Qt.PointingHandCursor))
        self.conversion_format.setFixedWidth(150)
        self.conversion_format.addItems(["JPEG", "WebP", "PNG", "GIF", "TIFF", "BMP"])
        controls_layout.addWidget(self.conversion_format)

        self.resize_checkbox = QCheckBox("Resize?")
        self.resize_checkbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.resize_checkbox.stateChanged.connect(self.toggle_resize_fields)
        controls_layout.addWidget(self.resize_checkbox)

        size_layout = QVBoxLayout()
        size_layout.setSpacing(5)
        size_layout.setContentsMargins(0, 0, 0, 0) 

        self.width_input = QLineEdit()
        self.height_input = QLineEdit()
        self.width_input.setFixedWidth(150)
        self.height_input.setFixedWidth(150)
        width_label = QLabel("Max Width:")
        height_label = QLabel("Max Height:")
        width_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        height_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        size_layout.addWidget(width_label)
        size_layout.addWidget(self.width_input)
        size_layout.addWidget(height_label)
        size_layout.addWidget(self.height_input)

        controls_layout.addLayout(size_layout)

        self.convert_button = QPushButton("Convert")
        self.convert_button.setFixedWidth(100)
        self.convert_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.convert_button.clicked.connect(self.convert_image)
        controls_layout.addWidget(self.convert_button)
        
        preview_button = QPushButton("Preview")
        preview_button.setFixedWidth(100)
        preview_button.setCursor(QCursor(Qt.PointingHandCursor))
        preview_button.clicked.connect(self.display_image_preview)
        controls_layout.addWidget(preview_button)
        
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        controls_layout.addItem(spacer)

        self.resize_timer = QTimer()
        self.resize_timer.setSingleShot(True)
        self.resize_timer.timeout.connect(self.update_image_preview_size)

        self.toggle_resize_fields()

    def toggle_resize_fields(self):
        if self.resize_checkbox.isChecked():
            self.width_input.setEnabled(True)
            self.height_input.setEnabled(True)
        else:
            self.width_input.setEnabled(False)
            self.height_input.setEnabled(False)

    def select_file(self):
        options = QFileDialog.Options()
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Select Image File", "", "Images (*.png *.jpg *.jpeg *.webp *.gif *.tiff *.bmp);;All Files (*)", options=options)
        if self.file_path:
            filename = os.path.basename(self.file_path)
            self.selected_file_label.setText(f"Selected File: {filename}")
            self.conversion_format.setEnabled(True)
            self.resize_checkbox.setEnabled(True)
            self.convert_button.setEnabled(True)
            self.display_image_preview()

    def display_image_preview(self):
        if not self.file_path:
            return
        pixmap = QPixmap(self.file_path)
        if self.resize_checkbox.isChecked():
            width = self.width_input.text()
            height = self.height_input.text()
            try:
                max_width = int(width)
                max_height = int(height)
                scaled_pixmap = pixmap.scaled(max_width, max_height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            except ValueError:
                scaled_pixmap = pixmap
        else:
            scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        if self.preview_window:
            self.preview_window.close()
        self.preview_window = ImagePreviewWindow(scaled_pixmap)
        self.preview_window.set_pixmap(scaled_pixmap)
        self.preview_window.show()

    def convert_image(self):
        if not self.file_path:
            self.show_message("Error", "No file selected. Please select a file to convert.")
            return
        conversion_choice = self.conversion_format.currentText()
        if not conversion_choice:
            self.show_message("Error", "Please select a file format.")
            return

        format_mapping = {
            "JPEG": "jpeg",
            "WebP": "webp",
            "PNG": "png",
            "GIF": "gif",
            "TIFF": "tiff",
            "BMP": "bmp"
        }
        output_format = format_mapping.get(conversion_choice)

        if output_format:
            max_width = None
            max_height = None

            if self.resize_checkbox.isChecked():
                try:
                    max_width = int(self.width_input.text())
                    max_height = int(self.height_input.text())
                except ValueError:
                    self.show_message("Error", "Invalid width or height.")
                    return

            try:
                convert_image(self.file_path, output_format, max_width, max_height)
                self.show_message("Success", "File converted successfully.")
            except Exception as e:
                self.show_message("Error", f"An error occurred: {str(e)}")
        else:
            self.show_message("Error", "Invalid conversion choice. Please select a conversion format.")

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowIcon(QIcon(icon_path))
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

    def resizeEvent(self, event):
        self.resize_timer.start(100)
        super().resizeEvent(event)

    def update_image_preview_size(self):
        if self.preview_window and not self.preview_window.isMinimized():
            pixmap = QPixmap(self.file_path)
            scaled_pixmap = pixmap.scaled(self.preview_window.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.preview_window.set_pixmap(scaled_pixmap)

if __name__ == "__main__":
    qdarktheme.enable_hi_dpi()
    app = QApplication(sys.argv)
    qdarktheme.setup_theme(custom_colors={"primary": "#b76aff"})
    window = ImageConverterApp()
    window.show()
    sys.exit(app.exec_())
