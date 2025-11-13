import csv

#Validacion numero para Archivo CSV
def convertir_entero(valor):
    if valor is None:
        return None
    valor = str(valor).strip()
    if valor.isdigit():
        return int(valor)
    return None

#Validacion para pedir numero MENU
def pedir_entero(mensaje):
    valor = input(mensaje).strip()
    if valor == '':
        return None
    if valor.isdigit():
        return int(valor)
    else:
        print("Debe ingresar solo números enteros.")
        return pedir_entero(mensaje)

#Carga y validación del CSV
def cargar_paises_desde_csv(ruta):
    paises = []
    errores = []
    with open(ruta, encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        fila_num = 1
        for fila in lector:
            fila_num += 1
            nombre = fila.get('nombre', '').strip()
            poblacion = convertir_entero(fila.get('poblacion', ''))
            superficie = convertir_entero(fila.get('superficie', ''))
            continente = fila.get('continente', '').strip()

            if nombre == '':
                errores.append(f"Fila {fila_num}: nombre vacío.")
                continue

            if poblacion is None:
                errores.append(f"Fila {fila_num} ({nombre}): población inválida.")
                continue

            if superficie is None:
                errores.append(f"Fila {fila_num} ({nombre}): superficie inválida.")
                continue

            if continente == '':
                errores.append(f"Fila {fila_num} ({nombre}): continente vacío.")
                continue

            paises.append({
                'nombre': nombre,
                'poblacion': poblacion,
                'superficie': superficie,
                'continente': continente
            })
    return paises, errores

# Búsquedas y filtros
def buscar_por_nombre(paises, termino):
    termino = termino.lower().strip()
    resultado = []
    for p in paises:
        if termino == p['nombre'].lower(): 
            resultado.append(p)
    return resultado


def filtrar_por_continente(paises, continente):
    continente = continente.lower().strip()
    resultado = []
    for p in paises:
        if p['continente'].lower() == continente:
            resultado.append(p)
    return resultado

def filtrar_por_poblacion(paises, min_p=None, max_p=None):
    resultado = []
    for p in paises:
        if (min_p is None or p['poblacion'] >= min_p) and (max_p is None or p['poblacion'] <= max_p):
            resultado.append(p)
    return resultado

def filtrar_por_superficie(paises, min_s=None, max_s=None):
    resultado = []
    for p in paises:
        if (min_s is None or p['superficie'] >= min_s) and (max_s is None or p['superficie'] <= max_s):
            resultado.append(p)
    return resultado

#Ordenar
def ordenar_paises(paises, clave, descendente=False):
    if clave == 'nombre':
        for i in range(len(paises) - 1):
            for j in range(i + 1, len(paises)):
                if descendente:
                    if paises[i]['nombre'].lower() < paises[j]['nombre'].lower():
                        paises[i], paises[j] = paises[j], paises[i]
                else:
                    if paises[i]['nombre'].lower() > paises[j]['nombre'].lower():
                        paises[i], paises[j] = paises[j], paises[i]
    elif clave == 'poblacion':
        for i in range(len(paises) - 1):
            for j in range(i + 1, len(paises)):
                if descendente:
                    if paises[i]['poblacion'] < paises[j]['poblacion']:
                        paises[i], paises[j] = paises[j], paises[i]
                else:
                    if paises[i]['poblacion'] > paises[j]['poblacion']:
                        paises[i], paises[j] = paises[j], paises[i]
    elif clave == 'superficie':
        for i in range(len(paises) - 1):
            for j in range(i + 1, len(paises)):
                if descendente:
                    if paises[i]['superficie'] < paises[j]['superficie']:
                        paises[i], paises[j] = paises[j], paises[i]
                else:
                    if paises[i]['superficie'] > paises[j]['superficie']:
                        paises[i], paises[j] = paises[j], paises[i]
    return paises

#Estadísticas
def pais_mayor_menor_poblacion(paises):
    if len(paises) == 0:
        return None, None
    mayor = paises[0]
    menor = paises[0]
    for p in paises:
        if p['poblacion'] > mayor['poblacion']:
            mayor = p
        if p['poblacion'] < menor['poblacion']:
            menor = p
    return mayor, menor

def promedio_poblacion(paises):
    if len(paises) == 0:
        return 0
    total = 0
    for p in paises:
        total += p['poblacion']
    return total / len(paises)

def promedio_superficie(paises):
    if len(paises) == 0:
        return 0
    total = 0
    for p in paises:
        total += p['superficie']
    return total / len(paises)

def cantidad_por_continente(paises):
    conteo = {}
    for p in paises:
        cont = p['continente']
        if cont in conteo:
            conteo[cont] += 1
        else:
            conteo[cont] = 1
    return conteo


#Mostrar
def mostrar_pais(p):
    return f"{p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km² | Continente: {p['continente']}"

def listar_paises(paises):
    if len(paises) == 0:
        print("No se encontraron resultados.")
    else:
        for i, p in enumerate(paises, start=1):
            print(f"{i}. {mostrar_pais(p)}")

#Main
def main():
    ruta = input("Ingrese el nombre del archivo CSV: ").strip()
    paises, errores = cargar_paises_desde_csv(ruta)
    if len(errores) > 0:
        print("Errores encontrados:")
        for e in errores:
            print(" -", e)
    print(f"\n{len(paises)} países cargados correctamente.\n")

    opcion = ''
    while opcion != '0':
        print("\n    MENÚ PRINCIPAL    ")
        print("1. Buscar país por nombre")
        print("2. Filtrar por continente")
        print("3. Filtrar por población")
        print("4. Filtrar por superficie")
        print("5. Ordenar países")
        print("6. Mostrar estadísticas")
        print("7. Mostrar todos")
        print("0. Salir")

        opcion = input("Seleccione una opción: \n").strip()

        # Validacion Menu
        if not opcion.isdigit():
            print("No ingrese texto, ingrese un número del 0 al 7.")
            continue  

        opcion_num = int(opcion)
        
        # Opciones
        if opcion == '1':
            nombre = input("Ingrese nombre: ")
            resultados = buscar_por_nombre(paises, nombre)
            listar_paises(resultados)

        elif opcion == '2':
            cont = input("Ingrese continente: ")
            resultados = filtrar_por_continente(paises, cont)
            listar_paises(resultados)

        elif opcion == '3':
            print("Rango de población :")
            min_p = pedir_entero("Mínimo: ")
            max_p = pedir_entero("Máximo: ")
            resultados = filtrar_por_poblacion(paises, min_p, max_p)
            listar_paises(resultados)

        elif opcion == '4':
            print("Rango de superficie:")
            min_s = pedir_entero("Mínimo: ")
            max_s = pedir_entero("Máximo: ")
            resultados = filtrar_por_superficie(paises, min_s, max_s)
            listar_paises(resultados)

        elif opcion == '5':
            print("1. Nombre ascendente\n2. Nombre descendente\n3. Población ascendente\n4. Población descendente\n5. Superficie ascendente\n6. Superficie descendente")
            sub = input("Seleccione opción: ").strip()
            if sub == '1':
                ordenar_paises(paises, 'nombre', False)
            elif sub == '2':
                ordenar_paises(paises, 'nombre', True)
            elif sub == '3':
                ordenar_paises(paises, 'poblacion', False)
            elif sub == '4':
                ordenar_paises(paises, 'poblacion', True)
            elif sub == '5':
                ordenar_paises(paises, 'superficie', False)
            elif sub == '6':
                ordenar_paises(paises, 'superficie', True)
            listar_paises(paises)

        elif opcion == '6':
            mayor, menor = pais_mayor_menor_poblacion(paises)
            print("\n--- ESTADÍSTICAS ---")
            if mayor and menor:
                print("País con mayor población:", mostrar_pais(mayor))
                print("País con menor población:", mostrar_pais(menor))
            print(f"Promedio de población: {promedio_poblacion(paises):.2f}")
            print(f"Promedio de superficie: {promedio_superficie(paises):.2f} km²")
            print("Cantidad por continente:")
            conteo = cantidad_por_continente(paises)
            for c, n in conteo.items():
                print(f" - {c}: {n}")

        elif opcion == '7':
            listar_paises(paises)
        elif not opcion.isdigit():
            print("No ingrese texto, ingrese un número del 0 al 7.")
            continue 
        elif opcion_num < 0 or opcion_num > 7:
            print("Ingreso un número que no está en el menú.")
            continue

        elif opcion == '0':
            print("Programa finalizado. ¡Hasta luego!")
            break

        o

main()
