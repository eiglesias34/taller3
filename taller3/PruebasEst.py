import unittest
from Taller3Est import *


class TestEst(unittest.TestCase):
    
    def testReservas(self):
        
        formato = '%H:%M'
        
        verificarDisponibilidad()
