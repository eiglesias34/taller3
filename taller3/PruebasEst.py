import unittest
from Taller3Est import *


class TestEst(unittest.TestCase):
    
    def testReservas(self):
        formato = '%H:%M'
        
        est = Estacionamiento()
        reservas =[]
        horaIni = datetime.strptime("06:00", formato)
        horaFin = datetime.strptime("07:00", formato)
        self.assertEqual(est.verificarDisponibilidad(reservas,horaIni,horaFin), True)

