import unittest
from Taller3Est import *


class TestEst(unittest.TestCase):
    
    def testReservas(self):
        formato = '%H:%M'
        
        est = Estacionamiento()
        
        #Frontera: Primera reservacion
        est.reservaciones = [[6,9]]    
        horaIni = datetime.strptime("06:00", formato)
        horaFin = datetime.strptime("09:00", formato)
        self.assertEqual(est.verificarDisponibilidad(horaIni.hour,horaFin.hour), True)
        
