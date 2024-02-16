class Dia:

    def __init__(self, anyo = 1970, mes = 1, dia = 1):

        self.anyo = anyo
        self.mes = mes
        self.dia = dia

    def info(self):

        return f"{self.dia} de {self.obtener_mes()} del {self.anyo}"  # :02d ??

    def obtener_mes(self):  

        dicc_meses = {

            1: 'Enero',
            2: 'Febrero',
            3: 'Marzo',
            4: 'Abril',
            5: 'Mayo',
            6: 'Junio',
            7: 'Julio',
            8: 'Agosto',
            9: 'Septiembre',
            10: 'Octubre',
            11: 'Noviembre',
            12: 'Diciembre'

        }

        return dicc_meses.get(self.mes, "Mes no valido")

    def anyo_bisiesto(self):

        bisiesto = False

        if self.anyo % 4 == 0:
            bisiesto = True
            if self.anyo % 4 == 0 and self.anyo % 100 == 0:
                bisiesto = False
                if self.anyo % 4 == 0 and self.anyo % 100 == 0 and self.anyo % 400 == 0:
                    bisiesto = True

        return bisiesto

    
    def validar_fecha(self):

        dias_por_mes = {
            1: 31,
            2: 29,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

        if not (1 <= self.mes <= 12):
            raise ValueError("Fecha no valida (mes fuera de rango)")

        elif self.dia < 1 or self.dia > dias_por_mes.get(self.mes):
            raise ValueError("Fecha no valida (dia fuera de rango)")

        elif self.anyo < 1:
            raise ValueError("Fecha no valida (anyo fuera de rango)")

        elif self.anyo_bisiesto() == False and self.mes == 2 and self.dia == 29:
            raise ValueError("Fecha no valida (Anyo no bisiesto, dia no valido)")
        
        else:
            return True

    def zeller(self):
        '''
        13: 'Enero',
        14: 'Febrero',
        3: 'Marzo',
        4: 'Abril',
        5: 'Mayo',
        6: 'Junio',
        7: 'Julio',
        8: 'Agosto',
        9: 'Septiembre',
        10: 'Octubre',
        11: 'Noviembre',
        12: 'Diciembre'
        '''

        mes = self.mes
        anyo = self.anyo
        dia = self.dia

        if anyo > 2000:
            dia -= 1

        if mes == 1 or mes == 2:
            mes += 12
            anyo -= 1


        A = anyo % 100
        B = anyo // 100
        C = 2 - B + B // 4
        D = A // 4
        E = 13 * (mes + 1) // 5
        F = A + C + D + E + dia
        G = F % 7
 

        dicc_dias_semana = {
            
            0: 'Sabado',
            1: 'Domingo',
            2: 'Lunes',
            3: 'Martes',
            4: 'Miercoles',
            5: 'Jueves',
            6: 'Viernes',
        }

        return dicc_dias_semana[G]
        
        #f"El dia de la semana en la fecha {self.dia} del {self.mes} del {self.anyo} es {dicc_dias_semana[G]}"
        
            

