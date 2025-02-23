estilo_tabla = """
            QTableView {
                background-color: #121212;  /* Fondo oscuro */
                color: #e0e0e0;  /* Texto en gris claro */
                border: 1px solid #333;  /* Borde sutil */
                font-size: 14px;
                selection-background-color: #6200ee;  /* Color de selección */
                selection-color: white;  /* Color de texto en la selección */
                alternate-background-color: #333;  /* Fondo alternativo para filas */
            }
            QTableView::item {
                padding: 10px;
                border-bottom: 1px solid #444;  /* Línea separadora entre filas */
            }
            QTableView::item:selected {
                background-color: #6200ee;  /* Fondo de selección */
                color: white;  /* Texto blanco cuando se selecciona */
            }
            QHeaderView::section {
                background-color: #333;  /* Fondo del encabezado */
                color: #ffffff;  /* Texto blanco en el encabezado */
                padding: 8px;
                font-weight: bold;
                border: none;
            }
            QHeaderView::section:horizontal {
                border-bottom: 1px solid #444;  /* Línea separadora en encabezado */
            }
            QTableCornerButton::section {
                background-color: #121212;  /* Fondo del botón de la esquina */
                border: none;
            }
        """
