from Modulos_Acme.Registros import*
import json

def Calculo_Nomina():
    print("""
    ===========================================
                    ---ACME---
                  Calcular Nomina
    ===========================================
        """)
    print()

    salario_minimo = 1000000
    id = input("Digite numero de identificacion del trabajador al que desea calcular nomina:\n ")

    try:
        with open("registros.json", "r") as file:
            listregistros = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        listregistros = {}

    if id in listregistros:
        print()
        print("El Trabajador al que quiere calcular la nomina es: ", listregistros[id])
        print()

        if id not in listregistros:
            print("No se pudo encontrar al trabajador con ese ID...")
            return
        
        #sorry ticher me quede en el punto 3 :(

    # for trabajador in trabajador :
    #     salario = trabajador["salario"]
    #     salud = salario * 0.04
    #     pension = salario * 0.04
    #     transporte = 0

    # if salario < salario_minimo * 2:
