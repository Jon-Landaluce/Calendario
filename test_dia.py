from class_dia import Dia


def test_crear_fecha_valores_por_defecto():

    crear_fecha = Dia()

    assert crear_fecha.dia == 1
    assert crear_fecha.mes == 1
    assert crear_fecha.anyo == 1970
    assert crear_fecha.info() == "Jueves, 1 de Enero del 1970"


def test_crear_fecha_valores_especificos():

    crear_fecha = Dia(1970, 4, 7)

    assert crear_fecha.dia == 7
    assert crear_fecha.mes == 4
    assert crear_fecha.anyo == 1970
    assert crear_fecha.info() == "Martes, 7 de Abril del 1970"


def test_validar_fecha_bisiesta():

    # Test anyo bisiesto
    crear_fecha = Dia(2004, 1, 1)
    assert crear_fecha.anyo_bisiesto() == True

    # Test anyo no bisiesto
    crear_fecha = Dia(2003, 1, 1)
    assert crear_fecha.anyo_bisiesto() == False


def test_validar_fecha():

    # Dias max Enero
    crear_fecha = Dia(1999, 1, 31)
    assert crear_fecha.validar_fecha() == True

    # Dias max Febrero No Bisiesto
    crear_fecha = Dia(1999, 2, 28)
    assert crear_fecha.anyo_bisiesto() == False
    assert crear_fecha.validar_fecha() == True

    # Dias max Febrero Bisiesto
    crear_fecha = Dia(2004, 2, 29)
    assert crear_fecha.anyo_bisiesto() == True
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
    assert crear_fecha.info() == 'Jueves, 1 de Enero del 1970'

    crear_fecha = Dia(1999, 1, 19)
    assert crear_fecha.info() == 'Martes, 19 de Enero del 1999'

    crear_fecha = Dia(2000, 3, 19)
    assert crear_fecha.info() == 'Domingo, 19 de Marzo del 2000'

    crear_fecha = Dia(2022, 1, 19)
    assert crear_fecha.info() == 'Miercoles, 19 de Enero del 2022'

    # Test año bisiesto
    crear_fecha = Dia(2004, 2, 29)
    assert crear_fecha.info() == 'Domingo, 29 de Febrero del 2004'

    crear_fecha = Dia(1900, 8, 25)
    assert crear_fecha.info() == 'Sabado, 25 de Agosto del 1900'

    crear_fecha = Dia(2080, 3, 15)
    assert crear_fecha.info() == 'Viernes, 15 de Marzo del 2080'



    

