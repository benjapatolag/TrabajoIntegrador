# Sistema de Gestión de Datos de Países

Trabajo Práctico Integrador - Programación 1  
**Tecnicatura Universitaria en Programación - UTN**

## Descripción del Proyecto

Sistema desarrollado en Python para la gestión y análisis de información sobre países. Permite realizar búsquedas, aplicar filtros, ordenar datos y generar estadísticas a partir de un archivo CSV con información de países de todo el mundo.

El programa implementa conceptos fundamentales de programación como listas, diccionarios, funciones, estructuras de control, algoritmos de ordenamiento y manejo de archivos.

## Integrantes del Equipo

- **[Benjamin Lagos]** - [Estudiante]
- **[Leandro Rea]** - [Estudiante]

## Funcionalidades

### Búsqueda por Nombre
Permite buscar países ingresando su nombre completo. La búsqueda normaliza acentos para facilitar la entrada.

**Ejemplo:**
Ingrese nombre: Argentina

### Filtrar por Continente
Muestra todos los países pertenecientes a un continente específico.

**Continentes disponibles:**
- América
- Europa
- Asia
- África
- Oceanía

**Ejemplo:**

Ingrese continente: America

### Filtrar por Población
Filtra países dentro de un rango de población específico.

**Ejemplo:**

Mínimo: 10000000
Máximo: 50000000


### Filtrar por Superficie
Filtra países dentro de un rango de superficie en km².

**Ejemplo:**

Mínimo: 100000
Máximo: 3000000


### Ordenar Países
Ordena la lista de países según diferentes criterios:
- Por nombre (A-Z / Z-A)
- Por población (menor a mayor / mayor a menor)
- Por superficie (menor a mayor / mayor a menor)

### Estadísticas
Genera un reporte completo con:
- País con mayor y menor población
- País con mayor y menor superficie
- Promedio de población mundial
- Promedio de superficie
- Cantidad de países por continente

### Mostrar Todos los Países
Lista todos los países cargados en el sistema con su información completa.


## Instalación y Uso

### Requisitos Previos
- Python 3.x instalado
- Archivo CSV con datos de países

### Instalación

1. **Clonar el repositorio:**
```bash
git clone https://github.com/[usuario]/gestion-paises.git
cd gestion-paises
```

2. **Verificar que el archivo CSV esté en el directorio:**
```bash
ls paises.csv
```

### Ejecución

```bash
python main.py
```

Al iniciar, el programa solicitará el nombre del archivo CSV:

Ingrese el nombre del archivo CSV: paises.csv




## Formato del Archivo CSV

El archivo debe contener las siguientes columnas:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
Alemania,83149300,357022,Europa
```

### Especificaciones:
- **nombre**: Texto (nombre del país)
- **poblacion**: Número entero (habitantes)
- **superficie**: Número entero (km²)
- **continente**: Texto (continente al que pertenece)


## Ejemplos de Uso

### Ejemplo 1: Búsqueda por Nombre

MENÚ PRINCIPAL
1. Buscar país por nombre
Elija una opcion: 1

Ingrese nombre: Brasil

1. Brasil | Población: 213993437 | Superficie: 8515767 km² | Continente: América


### Ejemplo 2: Filtrar por Continente

MENÚ PRINCIPAL
2. Filtrar por continente
Elija una opcion: 2

Ingrese continente: Asia

1. Japón | Población: 125800000 | Superficie: 377975 km² | Continente: Asia
2. China | Población: 1439323776 | Superficie: 9596961 km² | Continente: Asia


### Ejemplo 3: Estadísticas

MENÚ PRINCIPAL
6. Mostrar estadísticas
Elija una opcion: 6

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


## Estructura del Código

### Funciones Principales

#### Validación
- `convertir_entero(valor)`: Valida y convierte valores a enteros
- `pedir_entero(mensaje)`: Solicita entrada numérica con validación

#### Carga de Datos
- `cargar_paises(ruta)`: Lee el archivo CSV y valida los datos

#### Búsqueda y Filtros
- `buscar_por_nombre(paises, termino)`: Busca países por nombre
- `filtrar_por_continente(paises, continente)`: Filtra por continente
- `filtrar_por_poblacion(paises, min_p, max_p)`: Filtra por rango de población
- `filtrar_por_superficie(paises, min_s, max_s)`: Filtra por rango de superficie

#### Ordenamiento
- `ordenar_paises(paises, clave, descendente)`: Ordena usando Bubble Sort

#### Estadísticas
- `estadistica_mayor_o_menor_poblacion(paises)`: Calcula extremos de población
- `estadistica_mayor_o_menor_superficie(paises)`: Calcula extremos de superficie
- `promedio_poblacion(paises)`: Calcula promedio de población
- `promedio_superficie(paises)`: Calcula promedio de superficie
- `cantidad_paises_cont(paises)`: Cuenta países por continente

#### Visualización
- `mostrar_pais(p)`: Formatea la información de un país
- `listar_paises(paises)`: Muestra lista de países

---

##  Validaciones Implementadas

Validación de formato del archivo CSV  
Verificación de datos numéricos (población y superficie)  
Control de campos vacíos  
Normalización de acentos en búsquedas  
Validación de entrada numérica en menús  
Manejo de búsquedas sin resultados  
Control de rangos inválidos en filtros

---

## Conceptos Aplicados

### Estructuras de Datos
- **Listas**: Almacenamiento de la colección de países
- **Diccionarios**: Representación de cada país con sus atributos

### Algoritmos
- **Bubble Sort**: Implementación manual para ordenamiento
- **Búsqueda lineal**: Para filtros y búsquedas
- **Recorrido de listas**: Para cálculo de estadísticas

### Programación Estructurada
- **Modularización**: Una función por responsabilidad
- **Validación de datos**: Control de errores en entrada y archivos
- **Manejo de archivos**: Lectura de CSV con encoding UTF-8



## Errores Conocidos y Limitaciones

La búsqueda por nombre es exacta (no busca coincidencias parciales)  
El ordenamiento modifica la lista original  
No se persisten los cambios en el archivo CSV


## Contacto

Para consultas o sugerencias sobre este proyecto:
- Email: [benjalagospato@gmail.com]
- GitHub: [@benjapatolag](https://github.com/benjapatolag)

