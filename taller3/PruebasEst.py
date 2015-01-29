import unittest
from Taller3Est import *


class TestEst(unittest.TestCase):
    
    def testReservas(self):
        formato = '%H:%M'
        
        est = Estacionamiento()
        
        #Frontera: Primera reservacion
        reservas = [[6,-1],[9,1]]
        horaIni = datetime.strptime("06:00", formato)
        horaFin = datetime.strptime("09:00", formato)
        self.assertEqual(est.verificarDisponibilidad(reservas,horaIni,horaFin), True)
        
        #Frontera: Maximo de reservas posibles en un intervalo
        reservas =[ [6,-1], [6,-1], [6,-1], [6,-1], [6,-1], [6,-1], [6,-1], [6,-1], [6,-1], [6,-1], 
                [9,1], [9,1], [9,1], [9,1],[9,1],[9,1],[9,1],[9,1],[9,1],[9,1]]
        horaIni = datetime.strptime("06:00", formato)
        horaFin = datetime.strptime("09:00", formato)
        self.assertEqual(est.verificarDisponibilidad(reservas,horaIni,horaFin), False)
