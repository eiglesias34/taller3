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
    formato = '%H:%M'
    reservas = []
    
    while True:    
        while True:
            horaIni = raw_input("Introduzca hora del inicio de la reservacion (hh:mm): ")
            horaIni = datetime.strptime(str(horaIni), formato)
            if ((horaIni.minute == 0) and (est.getHoraMinReserva() <= horaIni.hour < est.getHoraMaxReserva())):
                break;
            else:
                print("Hora invalida.")

        while True:
            hf = raw_input("Introduzca hora de la finalizacion de la reservacion (hh:mm): ")
            hf = datetime.strptime(str(hf), formato)
            if ((hf.minute == 0) and (est.getHoraMinReserva() < hf.hour <= est.getHoraMaxReserva()) and (hf.hour > horaIni.hour)):
                break;
            else:
                print("Hora invalida.")
                
        if len(est.reservaciones) == 0:
            est.reservaciones.append([horaIni.hour,hf.hour])
            print("Se realizo una reservacion exitosa")
        else:
            if reservas != []: 
                if (est.verificarDisponibilidad(reservas, horaIni, hf)):
                    print("Se realizo una reservacion exitosa")
                else:
                    print("No se puede realizar la reserva solicitada")
            else:
                est.reservaciones.append([horaIni.hour,hf.hour])
                print("Se realizo una reservacion exitosa")

        while True:
            continuar = raw_input("Desea hacer otra reservacion? (si/no): ")
            if (continuar != "si") and (continuar != "no"):
                print("Valor invalido.")
            else:
                break

        if continuar == "no":
            break