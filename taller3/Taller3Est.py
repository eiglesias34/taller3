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
        cont = 0;
        mejor = 0;
        hayPuesto = True
        mejorInicio = reservas[0]
        mejorFin = reservas[1]
        pos = 2;    

        while cont >= mejor:
            if mejorInicio[1] == -1:
                cont += 1
                mejor += 1
                if mejorFin[1] == -1:
                    mejorInicio = mejorFin
                    mejorFin = reservas[pos]
                    pos += 1
                else:
                    cont -= 1

        if mejor >= self.__capacidad:

            if ((horaFin.hour == mejorInicio[0]) or (horaIni.hour == mejorFin[0])):
                hayPuesto = True
            else:
                hayPuesto = False
        
        if hayPuesto:
            self.reservaciones.append([horaIni.hour,horaFin.hour])

        return hayPuesto        
    
# Funcion que escoge los intervalos a considerar en el algoritmo de Marzullo y los
# ordena. No toma en cuenta aquellos que estan en la frontera del intervalo de la nueva
# reservacion que se quiere agregar.
def dividir(seq,horaIni,horaFin):
    inicio = []
    fin = []
    i = 0
    while i < len(seq):
        if (seq[i][0] <= horaIni < seq[i][1]) or (seq[i][0] < horaFin <= seq[i][1]):
            inicio.append([seq[i][0],-1])
            fin.append([seq[i][1],1])
        i+=1
    return inicio,fin
    
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
            horaFin = raw_input("Introduzca hora de la finalizacion de la reservacion (hh:mm): ")
            horaFin = datetime.strptime(str(horaFin), formato)
            if ((horaFin.minute == 0) and (est.getHoraMinReserva() < horaFin.hour <= est.getHoraMaxReserva()) and (horaFin.hour > horaIni.hour)):
                break;
            else:
                print("Hora invalida.")
                
        if len(est.reservaciones) == 0:
            est.reservaciones.append([horaIni.hour,horaFin.hour])
            print("Se realizo una reservacion exitosa")
        else:
            ri,rf = dividir(reservas)
            ri.sort()
            rf.sort()
            reservas = ri + rf
            
            if reservas != []: 
                if (est.verificarDisponibilidad(reservas, horaIni, horaFin)):
                    print("Se realizo una reservacion exitosa")
                else:
                    print("No se puede realizar la reserva solicitada")
            else:
                est.reservaciones.append([horaIni.hour,horaFin.hour])
                print("Se realizo una reservacion exitosa")

        while True:
            continuar = raw_input("Desea hacer otra reservacion? (si/no): ")
            if (continuar != "si") and (continuar != "no"):
                print("Valor invalido.")
            else:
                break

        if continuar == "no":
            break