import csv

data_tijuana_tecate = [
    ['Nombre', 'Edo.', 'Carretera', 'Long.(km)', 'Tiempo(Hrs)', 'Caseta o puente', 'Motocicleta', 'Camión 3 ejes', 'Camión 4 ejes', 'Camión 5 ejes', 'Camión 6 ejes', 'Camión 7 ejes', 'Camión 8 ejes', 'Camión 9 ejes', 'Automóvil', 'Automóvil remolque 1 eje', 'Automóvil remolque 2 eje', 'Pick Ups', 'Autobus 2 ejes', 'Autobus 3 ejes', 'Autobus 4 ejes', 'Camión 2 ejes'],
    ['Tijuana - Entronque Tijuana', 'BCN', 'Mex 001D', 19.891, '00:19', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['Ent. Tijuana - Libramiento de Tecate (Ent. Esperanza)', 'BCN', 'Mex 002D', 22.220, '00:13', 'Tijuana', 75.0, 291.0, 291.0, 417.0, 417.0, 534.0, 534.0, 534.0, 151.0, 227.0, 303.0, 151.0, 224.0, 224.0, 224.0, 224.0],
    ['Libramiento de Tecate (Ent. Esperanza) - Tecate', 'BCN', 'Zona Urbana', 2.841, '00:04', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['Totales', '', '', 44.960, '00:37', '', 75.0, 291.0, 291.0, 417.0, 417.0, 534.0, 534.0, 534.0, 151.0, 227.0, 303.0, 151.0, 224.0, 224.0, 224.0, 224.0]
]

with open('tij_tec.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data_tijuana_tecate)
