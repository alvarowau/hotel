import markdown2
from PySide6.QtCore import QFile, QTextStream
from PySide6.QtWidgets import (
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)


class ReadMeController(QWidget):
    """Controlador para cargar y mostrar el archivo README.md en un QTextBrowser."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.text_browser = QTextBrowser(self)

        # Configurar el layout y añadir el QTextBrowser
        layout = QVBoxLayout(self)  # Aquí se usa QVBoxLayout
        layout.addWidget(self.text_browser)

        self.setLayout(layout)

    def load_readme(self, file_path: str):
        """Carga el archivo README.md, lo convierte a HTML y lo muestra en el QTextBrowser."""
        file = QFile(file_path)
        if file.open(QFile.ReadOnly | QFile.Text):  # type: ignore
            text_stream = QTextStream(file)
            content = text_stream.readAll()

            # Convertir el contenido Markdown a HTML
            html_content = markdown2.markdown(content)

            # Mostrar el HTML en el QTextBrowser
            self.text_browser.setHtml(html_content)
            file.close()
        else:
            self.text_browser.setPlainText("No se pudo cargar el archivo README.")
