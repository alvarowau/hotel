import markdown2
from PySide6.QtCore import QFile, QTextStream
from PySide6.QtWidgets import (
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)


class ReadMeController(QWidget):
    """Controlador para cargar y mostrar el archivo README.md en un QTextBrowser.

    Este controlador se encarga de leer un archivo README.md, convertir su contenido
    de Markdown a HTML utilizando la librería `markdown2`, y mostrar el resultado
    en un widget `QTextBrowser`.  Esto permite visualizar archivos README en
    formato Markdown dentro de la aplicación.
    """

    def __init__(self, parent=None):
        """Inicializa el controlador ReadMeController.

        Crea una instancia de `ReadMeController`, inicializa el widget base `QWidget`
        y configura la interfaz de usuario, que consiste en un `QTextBrowser`
        para mostrar el contenido del README.

        Args:
            parent (QWidget, optional): Widget padre del controlador. Por defecto None.
        """
        super().__init__(parent)
        self.text_browser = QTextBrowser(self)

        # Configurar el layout y añadir el QTextBrowser
        layout = QVBoxLayout(self)  # Aquí se usa QVBoxLayout
        layout.addWidget(self.text_browser)

        self.setLayout(layout)

    def load_readme(self, file_path: str):
        """Carga el archivo README.md, lo convierte a HTML y lo muestra en el QTextBrowser.

        Intenta abrir el archivo especificado por `file_path`, lee su contenido como texto,
        convierte el contenido de Markdown a HTML utilizando `markdown2.markdown()`,
        y finalmente, establece el contenido HTML en el `QTextBrowser` para su visualización.
        Si ocurre un error al abrir o leer el archivo, muestra un mensaje de error en el
        `QTextBrowser`.

        Args:
            file_path (str): Ruta al archivo README.md que se desea cargar y mostrar.

        Raises:
            FileNotFoundError: Si el archivo especificado en `file_path` no existe o no se puede abrir.
            markdown2.MarkdownError: Si hay un error al procesar el contenido Markdown (aunque
                                     `markdown2.markdown()` generalmente maneja errores de forma robusta).

        """
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
