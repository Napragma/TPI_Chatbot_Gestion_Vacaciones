# Alumna: Cóceres Natalia
#TpI - Gestión de Vacaciones
# =============================================================================
# BASE DE DATOS DE LA EMPRESA 
# =============================================================================

empleados = {
    "1001": {"nombre": "Natalia Cóceres", "dias_por_gozar": 15},
    "1002": {"nombre": "Diego Perez", "dias_por_gozar": 7},
    "1003": {"nombre": "Sofia Lucero", "dias_por_gozar": 20}
}

solicitudes = {}
contador_tramites = 500
# GESTIÓN DE ESTADOS: Diccionario para registrar la memoria del proceso
estados_usuarios = {}

def actualizar_estado(legajo, paso_bpmn):
    """Guarda el estado actual del usuario en el proceso."""
    estados_usuarios[legajo] = paso_bpmn

def buscar_empleado(legajo_ingresado):
    """Busca si el legajo existe en el sistema."""
    
    if legajo_ingresado in empleados:
        return True
    else:
        print("El legajo no existe. Podés registrarlo con la opción 2.")
        return False

def validar_fecha(texto):
    """Valida formato DD/MM/AAAA"""
    try:
        if "/" not in texto:
            print("\n[BOT] Error: Formato incorrecto. Usá barras. Ejemplo: 15/06/2026")
            return None
            
        partes = texto.split("/")
        if len(partes) != 3:
            print("\n[BOT] Error: La fecha debe tener tres partes (dia/mes/anio).")
            return None
            
        dia = int(partes[0])
        mes = int(partes[1])
        anio = int(partes[2])
        
        if mes < 1 or mes > 12 or dia < 1 or dia > 31 or anio < 2026 or anio > 2030:
            print("\n[BOT] Error: Fecha inválida o año fuera de rango (2026-2030).")
            return None
            
        # Validar los meses que tienen 30 días
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia > 30:
                print("\n[BOT] Error: Este mes tiene un máximo de 30 días.")
                return None
                
         # Validar Febrero - Cálculo de bisiesto para el rango 2026-2030)
        if mes == 2:
            if anio == 2028:
                limite_febrero = 29
            else:
                limite_febrero = 28
                
            if dia > limite_febrero:
                print("\n[BOT] Error: Febrero tiene un máximo de", limite_febrero, "días.")
                        
        return [dia, mes, anio]
        
    except ValueError:
        print("\n[BOT] Error: La fecha debe contener solo números enteros entre las barras.")
        return None

def fecha_a_texto(fecha_lista):
    """Pasa la lista [dia, mes, anio] a un texto legible."""
    return str(fecha_lista[0]) + "/" + str(fecha_lista[1]) + "/" + str(fecha_lista[2])

def cargar_empleado():
    """Permite registrar un nuevo empleado"""
    
    print("\n--- REGISTRAR NUEVO EMPLEADO ---")
    nuevo_legajo = input("Ingresá el número de legajo para registrar: ").strip()
    
    if nuevo_legajo in empleados:
        print("Error: Ese número de legajo ya está registrado.")
        return

    nombre = input("Ingresá el nombre completo del empleado: ")
    
    try:
        dias_ingresados = input("Ingresá los días de Licencia Anual Ordinaria por gozar: ")
        inicial_por_gozar = int(dias_ingresados)
    except ValueError:
        print("Error: Los días deben ser un número entero.")
        return

    empleados[nuevo_legajo] = {"nombre": nombre, "dias_por_gozar": inicial_por_gozar}
    print(f"\nEmpleado {nombre} registrado con el legajo {nuevo_legajo}.")

def solicitar_vacaciones(legajo):
    """Flujo guiado para cargar las fechas de las vacaciones."""
    
    emp = empleados[legajo]
    print("\n--- NUEVA SOLICITUD DE VACACIONES ---")
    
    actualizar_estado(legajo, "Ingreso fecha de inicio")

    fecha_inicio = None
    while fecha_inicio is None:
        entrada_inicio = input("Ingresá la fecha de inicio (DD/MM/AAAA): ")
        fecha_inicio = validar_fecha(entrada_inicio)

    actualizar_estado(legajo, "Ingreso fecha de fin") 

    fecha_fin = None
    while fecha_fin is None:
        entrada_fin = input("Ingresá la fecha de fin (DD/MM/AAAA): ")
        fecha_fin = validar_fecha(entrada_fin)
    
    actualizar_estado(legajo, "Ingresando cantidad de días")
    
    try:
        dias_ingresados = input("Ingresar la cantidad de días: ")
        dias_totales = int(dias_ingresados)
    except ValueError:
        print("Error: Tenés que ingresar la cantidad de días en números enteros.")
        return

    actualizar_estado(legajo, "Revisando días disponibles")

    disponibles_actuales = emp["dias_por_gozar"]
    if dias_totales > disponibles_actuales:
        print("No tenés días suficientes. Tus días disponibles son:", disponibles_actuales)
        return

    global contador_tramites
    contador_tramites = contador_tramites + 1
    id_tramite = str(contador_tramites)
    
    solicitudes[id_tramite] = {
        "id": id_tramite,
        "legajo": legajo,
        "nombre": emp["nombre"],
        "inicio": fecha_a_texto(fecha_inicio),
        "fin": fecha_a_texto(fecha_fin),
        "dias": dias_totales,
        "estado": "PENDIENTE"
    }
    
    print("\n[BOT] ¡Trámite creado! Código de solicitud:", id_tramite)
    print("Estado actual: PENDIENTE (Esperando aprobación)")
    
    actualizar_estado(legajo, "Esperando autorización")

    print("\n--- CONSULTA DE AUTORIZACIONES ---")
    print("1. Aprobar solicitud")
    print("2. Rechazar solicitud")
    decision = input("Seleccione una opción: ").strip()
    
    if decision == "1":
        solicitudes[id_tramite]["estado"] = "APROBADA"
        empleados[legajo]["dias_por_gozar"] = empleados[legajo]["dias_por_gozar"] - dias_totales
        print("\nResultado: Solicitud Aprobada. Días descontados de la Licencia Anual.")
    elif decision == "2":
        solicitudes[id_tramite]["estado"] = "RECHAZADA"
        print("\nResultado: Solicitud Rechazada.")
    else:
        solicitudes[id_tramite]["estado"] = "PENDIENTE DE REVISIÓN"
        print("\nOpción inválida. La solicitud quedó en estado pendiente.")
    actualizar_estado(legajo, "en el menú principal")

def consultar_saldo(legajo):
    """Busca en el diccionario los días de vacaciones que le quedan al empleado"""
   
    print("\n--- REVISIÓN DE LICENCIA ANUAL ---")
    print("Empleado:", empleados[legajo]["nombre"])
    print("Saldo de vacaciones:", empleados[legajo]["dias_por_gozar"])

# =============================================================================
# MENÚ PRINCIPAL 
# =============================================================================

def menu_principal(legajo):
    actualizar_estado(legajo, "en el menu principal")
    continuar = True
    while continuar:
        print("\n--- MENÚ DE AUTOGESTION ---")
        print("1. Solicitar vacaciones")
        print("2. Consultar saldo de vaciones disponibles")
        print("3. Cerrar sesión")
        
        opcion = input("Elegí una opción: ")
        if opcion == "1":
            solicitar_vacaciones(legajo)
        elif opcion == "2":
            consultar_saldo(legajo)
        elif opcion == "3":
            print("Cerrando sesión. Volviendo al inicio.")
            continuar = False
        else:
            print("Opción inválida. Ingresá 1, 2 o 3.")

def main():
    ejecutar = True
    while ejecutar:
        print("\n--- MENU DEL ASISTENTE VIRTUAL ---")
        print("Legajos ya registrados para probar: 1001, 1002 o 1003")
        print("1. Iniciar sesión con legajo")
        print("2. Registrar un nuevo empleado")
        print("3. Salir del sistema")
        print("---------------------------------------")
        
        opcion_inicio = input("Elegí una opción: ").strip()
        if opcion_inicio == "1":
            legajo_usuario = input("\nIngresá tu número de legajo para iniciar: ").strip()
            if buscar_empleado(legajo_usuario):
                menu_principal(legajo_usuario)
        elif opcion_inicio == "2":
            cargar_empleado()
        elif opcion_inicio == "3":
            print("Saliendo del sistema")
            ejecutar = False
        else:
            print("Opción inválida. Elegí 1, 2 o 3.")

main()
