from class_dia import Dia


def test_crear_fecha_valores_por_defecto():

    crear_fecha = Dia()

    assert crear_fecha.dia == 1
    assert crear_fecha.mes == 1
    assert crear_fecha.anyo == 1970
    assert crear_fecha.info() == "1 de Enero del 1970"


def test_crear_fecha_valores_asignados():

    crear_fecha = Dia(1970, 4, 7)

    assert crear_fecha.dia == 7
    assert crear_fecha.mes == 4
    assert crear_fecha.anyo == 1970
    assert crear_fecha.info() == "7 de Abril del 1970"


def test_validar_fecha_bisiesta():

    crear_fecha = Dia(2004, 1, 1)
    assert crear_fecha.anyo_bisiesto() == True


def test_validar_fecha():


    # Dias max Enero
    crear_fecha = Dia(1999, 1, 31)
    assert crear_fecha.validar_fecha() == True

    # Dias max Febrero No Bisiesto
    crear_fecha = Dia(1999, 2, 28)
    assert crear_fecha.validar_fecha() == True

    # Dias max Febrero Bisiesto
    crear_fecha = Dia(2004, 2, 29)
    assert crear_fecha.validar_fecha() == True
    
    # Dias max Marzo
    crear_fecha = Dia(1999, 3, 31)
    assert crear_fecha.validar_fecha() == True

    # Dias max Abril
    crear_fecha = Dia(1999, 4, 30)
    assert crear_fecha.validar_fecha() == True

    # Dias max Mayo
    crear_fecha = Dia(1999, 5, 31)
    assert crear_fecha.validar_fecha() == True

    # Dias max Junio
    crear_fecha = Dia(1999, 6, 30)
    assert crear_fecha.validar_fecha() == True

    # Dias max Julio
    crear_fecha = Dia(1999, 7, 31)
    assert crear_fecha.validar_fecha() == True

    # Dias max Agosto
    crear_fecha = Dia(1999, 8, 31)
    assert crear_fecha.validar_fecha() == True

    # Dias max Septiembre
    crear_fecha = Dia(1999, 9, 30)
    assert crear_fecha.validar_fecha() == True

    # Dias max Octubre
    crear_fecha = Dia(1999, 10, 31)
    assert crear_fecha.validar_fecha() == True

    # Dias max Noviembre
    crear_fecha = Dia(1999, 11, 30)
    assert crear_fecha.validar_fecha() == True

    # Dias max Diciembre
    crear_fecha = Dia(1999, 12, 31)
    assert crear_fecha.validar_fecha() == True


def test_zeller():

    crear_fecha = Dia(1970, 1, 1)
    assert crear_fecha.zeller() == 'Jueves'

    crear_fecha = Dia(1970, 2, 1)
    assert crear_fecha.zeller() == 'Domingo'

    crear_fecha = Dia(1970, 3, 1)
    assert crear_fecha.zeller() == 'Domingo'

    crear_fecha = Dia(1970, 4, 1)
    assert crear_fecha.zeller() == 'Miercoles'

    crear_fecha = Dia(1970, 5, 1)
    assert crear_fecha.zeller() == 'Viernes'

    crear_fecha = Dia(1970, 6, 1)
    assert crear_fecha.zeller() == 'Lunes'

    crear_fecha = Dia(1970, 7, 1)
    assert crear_fecha.zeller() == 'Miercoles'

    crear_fecha = Dia(1970, 8, 1)
    assert crear_fecha.zeller() == 'Sabado'

    crear_fecha = Dia(1970, 9, 1)
    assert crear_fecha.zeller() == 'Martes'

    crear_fecha = Dia(1970, 10, 1)
    assert crear_fecha.zeller() == 'Jueves'

    crear_fecha = Dia(1970, 11, 1)
    assert crear_fecha.zeller() == 'Domingo'

    crear_fecha = Dia(1970, 12, 1)
    assert crear_fecha.zeller() == 'Martes'

    crear_fecha = Dia(1999, 1, 19)
    assert crear_fecha.zeller() == 'Martes'

    crear_fecha = Dia(2000, 1, 19)
    assert crear_fecha.zeller() == 'Miercoles'

    crear_fecha = Dia(2022, 1, 19)
    assert crear_fecha.zeller() == 'Miercoles'

