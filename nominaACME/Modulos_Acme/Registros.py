
import json
import datetime


def Registro_empleados():
    print("""
    =============================================
                    ---ACME---
                Registro de Empleados
    =============================================
        """)
    print()

    try:
        with open("registros.json", "r") as file:
            listregistros = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        listregistros = {}

    while True:
        id = input("Digite numero de identificacion: ").strip()
        if id:
            break
        print()
        print("Su numero de identificacion no puede estar vacio...")
    while True:
        print()
        name = input("Digite su nombre: ").strip()
        if name:
            break
        print()
        print("Su nombre no puede estar vacio...")
    while True:
        print()
        cargo= input("Digite su cargo: ").strip()
        if cargo:
            break
        print()
        print("Su cargo no puede estar vacio...")
    while True:
            print()
            money_str = input("Digite su salario: ").strip()
            if money_str.isdigit():
                salario = int(money_str)
                break
            print("Debe ingresar un valor numerico valido para la cantidad...")
    listregistros[id] = {
        "Nombre": name,
        "Cargo": cargo,
        "Salario": salario
    }
    with open("registros.json", "w") as file:
        json.dump(listregistros, file, indent=4)
    print()
    print("¡Empleado Registrado con exito!")

def Registro_inasistencias():
    print("""
    =============================================
                    ---ACME---
                Registro de Inasistencias
    =============================================
        """)
    print()
    id = input("Digite numero de identificacion del trabajador al que desea aplicar una inasistencia :\n ")

    try:
        with open("registros.json", "r") as file:
            listregistros = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        listregistros = {}

    if id in listregistros:
        print()
        print("El Trabajador al que quiere aplicar inasistencia es: ", listregistros[id])
        print()

        if id not in listregistros:
            print("No se pudo encontrar al trabajador con ese ID...")
            return

        while True:
            print()
            inasistencias = input("Digite el numero de inasistencias que el tuvo: ").strip()
            if inasistencias.isdigit():
                inasistencia = int(inasistencias)
                break
            print("Debe ingresar un valor numerico valido para las inasistencias...")

        if id not in listregistros:
            listregistros[id] = []

        listregistros[id] = {
                "Inasistencias": inasistencia,
                "fecha": str(datetime.datetime.today())
            } 

        with open("Inasistencias.json", "w") as file:
            json.dump(listregistros, file, indent=4) 

        print()
        print("¡Se Registro la Inasistencias!")

    else:
        print()
        print("No se encontro al trabajador...")    

def Registro_Bonos():
    print("""
    ============================================
                    ---ACME---
              ¡Registro de Bonos Extra!
    ============================================
        """)
    print()
    id = input("Digite numero de identificacion del trabajador al que desea aplicar un bono:\n ")

    try:
        with open("registros.json", "r") as file:
            listregistros = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        listregistros = {}

    if id in listregistros:
        print()
        print("El Trabajador al que quiere aplicar el bono es: ", listregistros[id])
        print()

        if id not in listregistros:
            print("No se pudo encontrar al trabajador con ese ID...")
            return
        
    while True:
        print()
        fecha = input("Digite fecha en la que quiere aplicar el bono: ").strip()
        if fecha:
            break
        print()
        print("La fecha no puede estar vacia...")

    while True:
        print()
        money = input("Digite el valor del bono: ").strip()
        if money.isdigit():
            valor = int(money)
            break
        print("Debe ingresar un valor numerico valido para el bono...")  

    while True:
        print()
        concepto = input("Digite un concepto para el bono: ").strip()
        if concepto:
            break
        print()
        print("El concepto no puede estar vacia...")


    bonosfile = f"{valor}bonos.json" 
    try:
        with open(bonosfile, "r") as file:
            listregistros = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        listregistros = {} 

    bonos = fecha, money, concepto            
    

    if id not in listregistros:
        listregistros[id] = []

    listregistros[id] = {
        "fecha": fecha,
        "valor": float(valor),
        "concepto": concepto
    }

    with open("Bonos.json", "w") as file:
            json.dump(bonos, file, indent=4) 
    print()
    print("¡Se Registro el Bono!")         

    