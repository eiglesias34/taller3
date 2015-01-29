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
        
        #Esquina: Tratar de realizar una reserva donde el intervalo esta lleno
        reservas =[[6,-1],[6,-1],[6,-1],[6,-1],[6,-1],[6,-1],[6,-1],[6,-1],[6,-1],[6,-1],
                   [9,-1],[9,-1],[9,-1],[9,-1],[9,-1],[9,-1],[9,-1],[9,-1],[9,-1],[9,-1],
                   [9,1],[9,1],[9,1],[9,1],[9,1],[9,1],[9,1],[9,1],[9,1],[9,1],
                   [10,1],[10,1],[10,1],[10,1],[10,1],[10,1],[10,1],[10,1],[10,1],[10,1]]
        horaIni = datetime.strptime("07:00", formato)
        horaFin = datetime.strptime("18:00", formato)
        self.assertEqual(est.verificarDisponibilidad(reservas,horaIni,horaFin), False)
        
        #Esquina: Tratar de realizar una reserva donde el intervalo esta lleno
        reservas =[[6,-1],[6,-1],[6,-1],[6,-1],[6,-1],[6,-1],[6,-1],[6,-1],[6,-1],
                   [9,-1],[9,-1],[9,-1],[9,-1],[9,-1],[9,-1],[9,-1],[9,-1],[9,-1],[9,-1],
                   [9,1],[9,1],[9,1],[9,1],[9,1],[9,1],[9,1],[9,1],[9,1],[9,1],
                   [10,1],[10,1],[10,1],[10,1],[10,1],[10,1],[10,1],[10,1],[10,1],[10,1]]
        horaIni = datetime.strptime("08:00", formato)
        horaFin = datetime.strptime("10:00", formato)
        self.assertEqual(est.verificarDisponibilidad(reservas,horaIni,horaFin), False)

        #Frontera: Tratar de realizar una reserva teniendo el estacionamiento
        #          lleno.
        reservas = [[6,-1], [6,-1], [6,-1], [6,-1], [6,-1], [6,-1], [6,-1], [6,-1], [6,-1], [6,-1],
                    [18,1], [18,1], [18,1], [18,1], [18,1], [18,1], [18,1], [18,1], [18,1], [18,1]]
        horaIni = datetime.strptime("06:00", formato)
        horaFin = datetime.strptime("18:00", formato)
        self.assertEqual(est.verificarDisponibilidad(reservas,horaIni,horaFin), False)
        
        #Malicia: Comienzan unas reservas a las 13:00 y una nueva termina cuando empiezan estas. 
        reservas =[[12,-1],[12,-1],[12,-1],[12,-1],[12,-1],[13,-1],[13,-1],[13,-1],[13,-1],[13,-1],
                   [14,1],[14,1],[14,1],[14,1],[14,1],[15,1],[15,1],[15,1],[15,1],[15,1]]
        horaIni = datetime.strptime("10:00", formato)
        horaFin = datetime.strptime("13:00", formato)
        self.assertEqual(est.verificarDisponibilidad(reservas,horaIni,horaFin), True)
        
        #Esquina: Ingresar reservacion hora minima despues de varias reservaciones
        #         que terminen en hora maxima
        reservas =[[6,-1],[7,-1],[8,-1],[9,-1],[10,-1],[11,-1],[12,-1],[13,-1],[14,-1],[15,-1],
                   [9,1],[10,1],[11,1],[12,1],[13,1],[14,1],[15,1],[16,1],[17,1],[18,1]]
        horaIni = datetime.strptime("06:00", formato)
        horaFin = datetime.strptime("09:00", formato)
        self.assertEqual(est.verificarDisponibilidad(reservas,horaIni,horaFin), True)
        
        #Esquina, Frontera y Malicia: 10 carros reservan por la mitad del dia (06:00 - 12:00) y otros 
        #                            10 reservan por el resto del dia (12:00 - 18:00); luego otro carro trata
        #                            de reservar por una hora de 11:00 a 12:00. (FALLA)
        reservas = [[6,-1], [6,-1], [6,-1], [6,-1], [6,-1], [6,-1], [6,-1], [6,-1], [6,-1], [6,-1],
                    [12,-1], [12,-1], [12,-1], [12,-1], [12,-1], [12,-1], [12,-1], [12,-1], [12,-1],
                    [12,1], [12,1], [12,1], [12,1], [12,1], [12,1], [12,1], [12,1], [12,1], [12,1],
                    [18,1], [18,1], [18,1], [18,1], [18,1], [18,1], [18,1], [18,1], [18,1], [18,1]]
        horaIni = datetime.strptime("11:00", formato)
        horaFin = datetime.strptime("12:00", formato)
        self.assertEqual(est.verificarDisponibilidad(reservas,horaIni,horaFin), False)