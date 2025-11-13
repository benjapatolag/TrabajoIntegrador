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
def cargar_paises(archivo_csv):
    paises = []
    errores = []

    with open(archivo_csv, "r", encoding='utf-8-sig') as archivo:
        lector = csv.DictReader(archivo)

        for fila_num, fila in enumerate(lector, start=2):
            nombre = fila.get('nombre', '').strip()
            poblacion = convertir_entero(fila.get('poblacion', '').strip())
            superficie = convertir_entero(fila.get('superficie', '').strip())
            continente = fila.get('continente', '').strip()

            if nombre == '':
                errores.append(f"Fila {fila_num - 1}: nombre vacío.")
                continue

            if poblacion is None:
                errores.append(f"Fila {fila_num - 1} ({nombre or 'sin nombre'}): población inválida.")
                continue

            if superficie is None:
                errores.append(f"Fila {fila_num - 1} ({nombre or 'sin nombre'}): superficie inválida.")
                continue

            if continente == '':
                errores.append(f"Fila {fila_num - 1} ({nombre or 'sin nombre'}): continente vacío.")
                continue

            paises.append({
                'nombre': nombre,
                'poblacion': poblacion,
                'superficie': superficie,
                'continente': continente
            })

    return paises, errores


#Búsquedas y filtros
def buscar_por_nombre(paises, termino):
    reemplazos = str.maketrans("áéíóúÁÉÍÓÚ", "aeiouAEIOU")
    termino = termino.lower().translate(reemplazos).strip()
    resultado = []
    for p in paises:
        nombre = p['nombre'].lower().translate(reemplazos)
        if termino in nombre:
            resultado.append(p)
    return resultado


def filtrar_por_continente(paises, continente):
    reemplazos = str.maketrans("áéíóúÁÉÍÓÚ", "aeiouAEIOU")
    continente = continente.lower().translate(reemplazos).strip()
    resultado = []
    for p in paises:
        cont = p['continente'].lower().translate(reemplazos)
        if cont == continente:
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


#Ordenar paises segun lo elegido
def ordenar_paises(paises, clave, descendente):
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
def estadistica_mayor_o_menor_poblacion(paises):
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

def estadistica_mayor_o_menor_superficie(paises):
    if len(paises) == 0:
        return None, None
    mayor = paises[0]
    menor = paises[0]
    for p in paises:
        if p['superficie'] > mayor['superficie']:
            mayor = p
        if p['superficie'] < menor['superficie']:
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

def cantidad_paises_cont(paises):
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
    while True:
        ruta = input("Ingrese el nombre del archivo CSV: ").strip()
        paises, errores = cargar_paises(ruta)

        if len(errores) > 0:
            print(f"\nErrores encontrados en el archivo: {ruta}")
            for e in errores:
                print(" -", e)
            print("Intente de vuelta\n")
            continue
        else:
            print(f"\nArchivo '{ruta}' cargado correctamente con {len(paises)} países.")
            break  

    opcion = ''
    while opcion != '0':
        print(" ")
        print("    MENÚ PRINCIPAL    ")
        print("1. Buscar país por nombre")
        print("2. Filtrar por continente")
        print("3. Filtrar por población")
        print("4. Filtrar por superficie")
        print("5. Ordenar países")
        print("6. Mostrar estadísticas")
        print("7. Mostrar todos los paises")
        print("0. Salir")
        print(" ")

        opcion = input("Elija una opcion: ").strip()

        #Verificar que sea un dígito
        if not opcion.isdigit():
            print("No ingrese texto, ingrese un número del 0 al 7.")
            continue  

        #Match case para verificar lo elegido
        match opcion:
            case '1':
                nombre = input("\nIngrese nombre: ")
                resultados = buscar_por_nombre(paises, nombre)
                listar_paises(resultados)

            case '2':
                cont = input("\nIngrese continente: ")
                print("")
                resultados = filtrar_por_continente(paises, cont)
                listar_paises(resultados)

            case '3':
                print("\nRango de población :")
                min_p = pedir_entero("Mínimo: ")
                max_p = pedir_entero("Máximo: ")
                print("")
                resultados = filtrar_por_poblacion(paises, min_p, max_p)
                listar_paises(resultados)

            case '4':
                print("\nRango de superficie")
                min_s = pedir_entero("Mínimo: ")
                max_s = pedir_entero("Máximo: ")
                print("")
                resultados = filtrar_por_superficie(paises, min_s, max_s)
                listar_paises(resultados)

            case '5':
                while True:
                    print("\n¿De qué forma lo quiere ordenar?")
                    print("1. Por nombre ascendente")
                    print("2. Por nombre descendente")
                    print("3. Por población ascendente")
                    print("4. Por población descendente")
                    print("5. Por superficie ascendente")
                    print("6. Por superficie descendente")

                    sub = input("Elija una opción: ").strip()
            
                    match sub:
                        case '1':
                            ordenar_paises(paises, 'nombre', False)
                            break  # Sale del while cuando es válido
                        case '2':
                            ordenar_paises(paises, 'nombre', True)
                            break
                        case '3':
                            ordenar_paises(paises, 'poblacion', False)
                            break
                        case '4':
                            ordenar_paises(paises, 'poblacion', True)
                            break
                        case '5':
                            ordenar_paises(paises, 'superficie', False)
                            break
                        case '6':
                            ordenar_paises(paises, 'superficie', True)
                            break
                        case _:
                            print("Opción inválida. Intente nuevamente.")

                print("")
                listar_paises(paises)

            case '6':
                mayor, menor = estadistica_mayor_o_menor_poblacion(paises)
                mas, menos = estadistica_mayor_o_menor_superficie(paises)
                print("\n    ESTADÍSTICAS    \n")
                if mayor and menor:
                    print(f"País con mayor población: {mayor['nombre']} | Población: {mayor['poblacion']}")
                    print(f"País con menor población: {menor['nombre']} | Población: {menor['poblacion']}")
                if mas and menos:
                    print(f"País con mayor superficie: {mas['nombre']} | Superficie: {mas['superficie']}")
                    print(f"País con menor superficie: {menos['nombre']} | Superficie: {menos['superficie']}")
                print(f"Promedio de población: {promedio_poblacion(paises):.2f} en {len(paises)} paises")
                print(f"Promedio de superficie: {promedio_superficie(paises):.2f} km² en {len(paises)} paises")
                print("Cantidad de paises por continente:")
                conteo = cantidad_paises_cont(paises)
                for c, n in conteo.items():
                    print(f" - {c}: {n}")

            case '7':
                print("")
                listar_paises(paises)

            case '0':
                print("\nPrograma finalizado.")

            case _:
                print("Ingreso un número que no está en el menú")

if __name__ == "__main__":
    main()