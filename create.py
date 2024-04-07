import csv

data_rosarito_tijuana = [
    ['Nombre', 'Edo.', 'Carretera', 'Long.(km)', 'Tiempo(Hrs)', 'Caseta o puente', 'Motocicleta', 'Camión 3 ejes', 'Camión 4 ejes', 'Camión 5 ejes', 'Camión 6 ejes', 'Camión 7 ejes', 'Camión 8 ejes', 'Camión 9 ejes', 'Automóvil', 'Automóvil remolque 1 eje', 'Automóvil remolque 2 eje', 'Pick Ups', 'Autobus 2 ejes', 'Autobus 3 ejes', 'Autobus 4 ejes', 'Camión 2 ejes'],
    ['Rosarito - Entronque Rosarito', 'BCN', 'Mex 001', 1.915, '00:01', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['Entronque Rosarito - Tijuana', 'BCN', 'Mex 001D', 27.153, '00:16', 'Playas de Tijuana', 22.0, 94.0, 114.0, 114.0, 130.0, 130.0, 130.0, 130.0, 44.0, 67.0, 90.0, 44.0, 94.0, 94.0, 94.0, 94.0],
    ['Totales', '', '', 29.070, '00:18', '', 22.0, 94.0, 114.0, 114.0, 130.0, 130.0, 130.0, 130.0, 44.0, 67.0, 90.0, 44.0, 94.0, 94.0, 94.0, 94.0]
]

data_rosarito_tecate = [
    ['Nombre', 'Edo.', 'Carretera', 'Long.(km)', 'Tiempo(Hrs)', 'Caseta o puente', 'Motocicleta', 'Camión 3 ejes', 'Camión 4 ejes', 'Camión 5 ejes', 'Camión 6 ejes', 'Camión 7 ejes', 'Camión 8 ejes', 'Camión 9 ejes', 'Automóvil', 'Automóvil remolque 1 eje', 'Automóvil remolque 2 eje', 'Pick Ups', 'Autobus 2 ejes', 'Autobus 3 ejes', 'Autobus 4 ejes', 'Camión 2 ejes'],
    ['Rosarito - Entronque Tijuana', 'BCN', 'Mex 001', 49.234, '00:31', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['Ent. Tijuana - Libramiento de Tecate (Ent. Esperanza)', 'BCN', 'Mex 002D', 22.220, '00:13', 'Tijuana', 75.0, 291.0, 291.0, 417.0, 417.0, 534.0, 534.0, 534.0, 151.0, 227.0, 303.0, 151.0, 224.0, 224.0, 224.0, 224.0],
    ['Libramiento de Tecate (Ent. Esperanza) - Tecate', 'BCN', 'Zona Urbana', 2.841, '00:04', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['Totales', '', '', 74.300, '00:49', '', 75.0, 291.0, 291.0, 417.0, 417.0, 534.0, 534.0, 534.0, 151.0, 227.0, 303.0, 151.0, 224.0, 224.0, 224.0, 224.0]
]

with open('ros_tij.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data_rosarito_tijuana)

with open('ros_tec.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data_rosarito_tecate)
