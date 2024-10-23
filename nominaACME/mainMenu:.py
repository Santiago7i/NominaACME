from Modulos_Acme.Registros import*
from Modulos_Acme.Nomina import*


while True:
    print("""
    =============================================
                    ---ACME---        
                 GESTION DE NOMINA
    =============================================

    1. Registrar Empleados.
    2. Registrar Inasistencias.
    3. Registrar Bonos extra-legales.                    
    4. Calculo de Nomina. 
    0. Salir  
        """)
    option = (input("Digite la opcion deseada: \n"))
    match option:
        case "1":
            Registro_empleados()

        case "2":
            Registro_inasistencias()

        case "3":
            Registro_Bonos()

        case "4":
            pass

        case "0":
            print()
            print("Gracias por preferirnos, ¡Hasta pronto!") 
            break
        case _:
            print()
            print("Digite correctamente la opcion..")