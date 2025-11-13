# Sistema de Gestión de Datos de Países

Trabajo Práctico Integrador - Programación 1  
**Tecnicatura Universitaria en Programación - UTN**

---

## Descripción del Proyecto

Sistema desarrollado en Python para la gestión y análisis de información sobre países. Permite realizar búsquedas, aplicar filtros, ordenar datos y generar estadísticas a partir de un archivo CSV con información de países de todo el mundo.

El programa implementa conceptos fundamentales de programación como listas, diccionarios, funciones, estructuras de control (`match/case`), algoritmos de ordenamiento manual y manejo de archivos CSV.

---

## Integrantes del Equipo

- **Benjamin Lagos** - Estudiante
- **Leandro Rea** - Estudiante

---

## Funcionalidades del Sistema

### 1. Búsqueda por Nombre
Permite buscar países ingresando su nombre completo o parcial. La búsqueda normaliza acentos automáticamente para facilitar la entrada del usuario.

**Ejemplo de uso:**
```
Ingrese nombre: Argent
```

**Resultado:**
```
1. Argentina | Población: 45376763 | Superficie: 2780400 km² | Continente: América
```

---

### 2. Filtrar por Continente
Muestra todos los países pertenecientes a un continente específico. La búsqueda es insensible a mayúsculas y normaliza acentos.

**Continentes disponibles:**
- América
- Europa
- Asia
- África
- Oceanía

**Ejemplo de uso:**
```
Ingrese continente: america
```

**Resultado:**
```
1. Argentina | Población: 45376763 | Superficie: 2780400 km² | Continente: América
2. Brasil | Población: 213993437 | Superficie: 8515767 km² | Continente: América
3. Canadá | Población: 38005238 | Superficie: 9984670 km² | Continente: América
```

---

### 3. Filtrar por Población
Filtra países dentro de un rango de población específico (habitantes). Permite ingresar valores mínimos y máximos.

**Ejemplo de uso:**
```
Rango de población:
Mínimo: 10000000
Máximo: 50000000
```

**Resultado:**
```
1. Argentina | Población: 45376763 | Superficie: 2780400 km² | Continente: América
2. Canadá | Población: 38005238 | Superficie: 9984670 km² | Continente: América
```

---

### 4. Filtrar por Superficie
Filtra países dentro de un rango de superficie en km². Útil para comparar extensión territorial.

**Ejemplo de uso:**
```
Rango de superficie:
Mínimo: 100000
Máximo: 3000000
```

**Resultado:**
```
1. Argentina | Población: 45376763 | Superficie: 2780400 km² | Continente: América
2. Alemania | Población: 83149300 | Superficie: 357022 km² | Continente: Europa
```

---

### 5. Ordenar Países
Ordena la lista completa de países según diferentes criterios, utilizando el algoritmo de ordenamiento Bubble Sort implementado manualmente.

**Opciones de ordenamiento:**
1. Por nombre ascendente (A-Z)
2. Por nombre descendente (Z-A)
3. Por población ascendente (menor a mayor)
4. Por población descendente (mayor a menor)
5. Por superficie ascendente (menor a mayor)
6. Por superficie descendente (mayor a menor)

**Nota:** Si se ingresa una opción inválida, el sistema volverá a solicitar la elección hasta que sea correcta.

---

### 6. Mostrar Estadísticas
Genera un reporte completo con información estadística sobre todos los países cargados.

**Información incluida:**
- País con mayor y menor población
- País con mayor y menor superficie
- Promedio de población mundial
- Promedio de superficie mundial
- Cantidad de países por continente

**Ejemplo de salida:**
```
    ESTADÍSTICAS    

País con mayor población: China | Población: 1439323776
País con menor población: Vaticano | Población: 801
País con mayor superficie: Rusia | Superficie: 17098242
País con menor superficie: Vaticano | Superficie: 0
Promedio de población: 38289605.67 en 195 paises
Promedio de superficie: 773809.25 km² en 195 paises
Cantidad de paises por continente:
 - América: 35
 - Europa: 44
 - Asia: 48
 - África: 54
 - Oceanía: 14
```

---

### 7. Mostrar Todos los Países
Lista todos los países cargados en el sistema con su información completa.

---

## Instalación y Uso

### Requisitos Previos
- Python 3.10 o superior (requerido para `match/case`)
- Módulo `csv` (incluido en la biblioteca estándar de Python)
- Archivo CSV con datos de países

### Estructura de Archivos
```
proyecto/
│
├── main.py          # Archivo principal del programa
├── paises.csv       # Base de datos de países
└── README.md        # Este archivo
```

### Instalación

1. **Clonar o descargar el repositorio:**
```bash
git clone https://github.com/benjapatolag/gestion-paises.git
cd gestion-paises
```

2. **Verificar que el archivo CSV esté en el directorio:**
```bash
ls paises.csv
```

3. **Verificar versión de Python:**
```bash
python --version
# Debe ser Python 3.10 o superior
```

### Ejecución

```bash
python main.py
```

Al iniciar, el programa solicitará el nombre del archivo CSV:

```
Ingrese el nombre del archivo CSV: paises.csv
```

Si el archivo se carga correctamente:
```
Archivo 'paises.csv' cargado correctamente con 195 países.
```

Si hay errores en el archivo, se mostrarán en pantalla y se solicitará reintentar con un archivo válido.

---

## Formato del Archivo CSV

El archivo debe seguir estrictamente el siguiente formato:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
Alemania,83149300,357022,Europa
```

### Especificaciones Técnicas:

| Columna | Tipo | Descripción | Ejemplo |
|---------|------|-------------|---------|
| **nombre** | Texto | Nombre del país | Argentina |
| **poblacion** | Entero | Número de habitantes | 45376763 |
| **superficie** | Entero | Extensión en km² | 2780400 |
| **continente** | Texto | Continente al que pertenece | América |

### Reglas de Validación:
- El archivo debe incluir encabezados
- Todos los campos son obligatorios
- `poblacion` y `superficie` deben ser números enteros
- No se permiten campos vacíos
- Se recomienda encoding UTF-8 con BOM (`utf-8-sig`)

---

## Estructura del Código

### Módulos y Funciones Principales

#### Funciones de Validación
```python
def convertir_entero(valor)
```
Valida y convierte valores de texto a enteros. Retorna `None` si el valor no es válido.

```python
def pedir_entero(mensaje)
```
Solicita entrada numérica al usuario con validación recursiva hasta obtener un valor válido.

---

#### Funciones de Carga de Datos
```python
def cargar_paises(archivo_csv)
```
Lee el archivo CSV, valida cada fila y retorna dos elementos:
- Lista de diccionarios con países válidos
- Lista de errores encontrados durante la carga

---

#### Funciones de Búsqueda y Filtros
```python
def buscar_por_nombre(paises, termino)
```
Busca países cuyo nombre contenga el término ingresado (búsqueda parcial, case-insensitive).

```python
def filtrar_por_continente(paises, continente)
```
Filtra países por continente con comparación exacta normalizada.

```python
def filtrar_por_poblacion(paises, min_p=None, max_p=None)
```
Filtra países dentro de un rango de población. Los parámetros son opcionales.

```python
def filtrar_por_superficie(paises, min_s=None, max_s=None)
```
Filtra países dentro de un rango de superficie. Los parámetros son opcionales.

---

#### Función de Ordenamiento
```python
def ordenar_paises(paises, clave, descendente)
```
Implementa el algoritmo **Bubble Sort** para ordenar la lista de países.
- `clave`: 'nombre', 'poblacion' o 'superficie'
- `descendente`: `True` para orden descendente, `False` para ascendente

**Nota:** Esta función modifica la lista original.

---

#### Funciones de Estadísticas
```python
def estadistica_mayor_o_menor_poblacion(paises)
```
Retorna una tupla con el país de mayor y menor población.

```python
def estadistica_mayor_o_menor_superficie(paises)
```
Retorna una tupla con el país de mayor y menor superficie.

```python
def promedio_poblacion(paises)
```
Calcula el promedio de población de todos los países.

```python
def promedio_superficie(paises)
```
Calcula el promedio de superficie de todos los países.

```python
def cantidad_paises_cont(paises)
```
Retorna un diccionario con el conteo de países por continente.

---

#### Funciones de Visualización
```python
def mostrar_pais(p)
```
Formatea la información de un país en formato legible.

```python
def listar_paises(paises)
```
Muestra una lista numerada de países o un mensaje si está vacía.

---

#### Función Principal
```python
def main()
```
Controla el flujo principal del programa con un bucle `while` y estructura `match/case` para el menú.

---

## Conceptos de Programación Aplicados

### Estructuras de Datos
- **Listas:** Almacenamiento dinámico de la colección de países
- **Diccionarios:** Representación de cada país con claves (`nombre`, `poblacion`, `superficie`, `continente`)
- **Tuplas:** Retorno múltiple en funciones estadísticas

### Control de Flujo
- **Bucles `while`:** Menú principal y submenú de ordenamiento
- **Estructura `match/case`:** Direccionamiento de opciones del menú (Python 3.10+)
- **Bucles `for`:** Recorrido de listas y procesamiento de datos

### Algoritmos Implementados
- **Bubble Sort:** Ordenamiento manual sin usar funciones built-in
- **Búsqueda lineal:** Para filtros y búsquedas en la lista
- **Recorrido de listas:** Cálculo de estadísticas (máximo, mínimo, promedio)

### Programación Estructurada
- **Modularización:** Una función específica por responsabilidad
- **Validación de datos:** Control de errores en entradas y archivos
- **Manejo de archivos:** Lectura de CSV con manejo de encoding

### Normalización de Texto
- **str.maketrans():** Conversión de caracteres acentuados
- **translate():** Aplicación de transformaciones
- **lower():** Comparaciones insensibles a mayúsculas
- **strip():** Eliminación de espacios en blanco

---

## Validaciones Implementadas

El sistema incluye las siguientes validaciones para garantizar robustez:

- Validación de existencia del archivo CSV
- Verificación de formato correcto del archivo
- Control de datos numéricos (población y superficie deben ser enteros)
- Verificación de campos obligatorios no vacíos
- Normalización de acentos en búsquedas y filtros
- Validación de entrada numérica en menús con recursión
- Manejo de búsquedas sin resultados
- Control de opciones inválidas en menús
- Validación de rangos en filtros numéricos

---

## Manejo de Errores

El programa maneja los siguientes escenarios de error:

### Errores en Carga de Archivo
- **Archivo no encontrado:** Mensaje de error indicando qué archivo se intentó abrir
- **Formato inválido:** Se reporta cada fila con problemas específicos
- **Campos vacíos:** Se indica el campo faltante y el número de fila
- **Datos no numéricos:** Se especifica qué campo tiene formato incorrecto

**Ejemplo de reporte de errores:**
```
Errores encontrados en el archivo: paises.csv
 - Fila 5: nombre vacío.
 - Fila 12 (Francia): población inválida.
 - Fila 23 (Italia): superficie inválida.
Intente de vuelta
```

### Errores de Entrada del Usuario
- **Texto en lugar de número:** Solicita reingresar hasta obtener un número
- **Opción de menú inválida:** Muestra mensaje y vuelve al menú
- **Búsquedas sin resultados:** Informa al usuario claramente

---

## Ejemplo Completo de Ejecución

```
Ingrese el nombre del archivo CSV: paises.csv

Archivo 'paises.csv' cargado correctamente con 195 países.

    MENÚ PRINCIPAL    
1. Buscar país por nombre
2. Filtrar por continente
3. Filtrar por población
4. Filtrar por superficie
5. Ordenar países
6. Mostrar estadísticas
7. Mostrar todos los paises
0. Salir
 
Elija una opcion: 1

Ingrese nombre: Argent
1. Argentina | Población: 45376763 | Superficie: 2780400 km² | Continente: América

    MENÚ PRINCIPAL    
1. Buscar país por nombre
2. Filtrar por continente
3. Filtrar por población
4. Filtrar por superficie
5. Ordenar países
6. Mostrar estadísticas
7. Mostrar todos los paises
0. Salir
 
Elija una opcion: 5

¿De qué forma lo quiere ordenar?
1. Por nombre ascendente
2. Por nombre descendente
3. Por población ascendente
4. Por población descendente
5. Por superficie ascendente
6. Por superficie descendente
Elija una opción: 4

1. China | Población: 1439323776 | Superficie: 9596961 km² | Continente: Asia
2. India | Población: 1380004385 | Superficie: 3287263 km² | Continente: Asia
3. Estados Unidos | Población: 331002651 | Superficie: 9833517 km² | Continente: América
...

    MENÚ PRINCIPAL    
...
Elija una opcion: 0

Programa finalizado.
```

---

## Limitaciones Conocidas

- La búsqueda por nombre realiza coincidencia parcial pero es secuencial (O(n))
- El ordenamiento modifica la lista original de países
- No se persisten cambios en el archivo CSV (solo lectura)
- El algoritmo Bubble Sort tiene complejidad O(n²) - no óptimo para grandes datasets
- No hay opción de agregar, modificar o eliminar países desde el programa

---

## Posibles Mejoras Futuras

- Implementar algoritmos de ordenamiento más eficientes (QuickSort, MergeSort)
- Agregar funcionalidad CRUD (crear, actualizar, eliminar países)
- Persistir cambios en el archivo CSV
- Exportar estadísticas a formato PDF o Excel
- Interfaz gráfica con Tkinter o PyQt
- Agregar gráficos estadísticos con matplotlib
- Implementar búsqueda binaria tras ordenamiento

---

## Tecnologías Utilizadas

- **Lenguaje:** Python 3.10+
- **Módulos estándar:** csv
- **Control de versiones:** Git/GitHub
- **Encoding:** UTF-8 con BOM

---

## Licencia

Este proyecto fue desarrollado con fines educativos para la asignatura de Programación 1 de la Tecnicatura Universitaria en Programación de la UTN.

---

## Contacto

Para consultas o sugerencias sobre este proyecto:

- **Email:** benjalagospato@gmail.com
- **GitHub:** [@benjapatolag](https://github.com/benjapatolag)
- **Universidad:** UTN (Universidad Tecnológica Nacional)
- **Asignatura:** Programación 1

---

**Fecha de entrega:** Noviembre 2025  
**Versión:** 1.0