from datetime import datetime,timedelta

class Estacionamiento:
    def __init__(self):
        self.__capacidad = 10
        self.__horaMinReserva = 6
        self.__horaMaxReserva = 18
        self.reservaciones = []
        
           
    def getCapacidad(self):
        return self.__capacidad

    def getHoraMinReserva(self):
        return self.__horaMinReserva

    def getHoraMaxReserva(self):
        return self.__horaMaxReserva

    # Algoritmo de Marzullo
    def verificarDisponibilidad(self, reservas, horaIni, horaFin):
        return True
    
if __name__ == '__main__':
    est = Estacionamiento()
    reservas = []
    formato = '%H:%M'
    
