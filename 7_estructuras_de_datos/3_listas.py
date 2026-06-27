# ==============================================================================
# # 7_estructuras_de_datos -> 3_listas.py
# ==============================================================================

# ==============================================================================
# * INTRODUCCIÓN A LAS LISTAS (LISTS)
# ==============================================================================

# ------------------------------------------------------------------------------
# * 3.1 ¿Qué es una Lista y cuál es su sintaxis básica?
# ------------------------------------------------------------------------------

# * Creamos nuestra primera lista vacía (un contenedor listo para usar)
lista_pendientes = []

# * Creamos una lista con datos precargados: componentes de un sistema operativo
componentes_sistema = ["Explorador", "Administrador de Tareas", "Panel de Control"]

print("--- Inicialización de Listas ---")
print(f"Estado inicial de la lista vacía: {lista_pendientes}")
print(f"Componentes precargados en el sistema: {componentes_sistema}")

# ------------------------------------------------------------------------------
# * 3.2 El concepto de Índice Lineal (La numeración en programación)
# ------------------------------------------------------------------------------

print("\n--- Acceso por Índices ---")
# * Accedemos al primer elemento de la lista (Índice 0)
primer_componente = componentes_sistema[0]
print(f"Primer elemento del sistema (Índice 0): {primer_componente}")

# * Accedemos al tercer elemento de la lista (Índice 2)
tercer_componente = componentes_sistema[2]
print(f"Tercer elemento del sistema (Índice 2): {tercer_componente}")

# TODO: Error común de novato -> Intentar acceder a componentes_sistema[3]. 
# TODO: Como solo hay 3 elementos (índices 0, 1 y 2), provocará un error 'IndexError'.


# ------------------------------------------------------------------------------
# * 3.3 Métodos Esenciales para manipular Listas (Modificación Dinámica)
# ------------------------------------------------------------------------------

print("\n--- Manipulación de la Lista ---")

# * Agregamos elementos nuevos a la lista de pendientes (Uso de .append)
lista_pendientes.append("Revisar correos del trabajo")
lista_pendientes.append("Actualizar controladores de video")
# print(f"Lista tras añadir actividades pendientes: {lista_pendientes}")
# del lista_pendientes[1]  #elimina un elemento de acuerdo a su índice
# print(f"Lista tras añadir actividades pendientes ELIMINADO: {lista_pendientes}")

# * Limpiamos la lista por completo simulando el cierre del día (Uso de .clear)
lista_pendientes.clear()
# print(f"Lista tras cumplir las tareas pendientes: {lista_pendientes}")


# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa
# ------------------------------------------------------------------------------

# * Ejemplo A: Averiguar el tamaño de la lista de forma automática (Función len)
# ? La función len() nos dice cuántos elementos tiene una lista en total. 
# ? En sistemas reales sirve para validar si una cola de peticiones superó su límite.
historial_notificaciones = ["Alerta de red", "Actualización lista", "Error crítico", "Copia exitosa"]
total_alertas = len(historial_notificaciones)

print("\n--- Refuerzo Práctico (Métodos y Funciones Extra) ---")
print(f"Cantidad total de alertas en el historial: {total_alertas}")


# * Ejemplo B: Modificar un elemento directamente usando su índice
# ? Si un dato almacenado cambia, podemos apuntar directamente a su posición (índice) 
# ? y asignarle un nuevo valor para sobrescribirlo en la memoria RAM.
navegadores_instalados = ["Firefox", "Edge", "Navegador Viejo"]
print(f"Lista de navegadores original: {navegadores_instalados}")

# * Reemplazamos el navegador viejo por uno moderno y optimizado
navegadores_instalados[2] = "Chrome"
print(f"Lista de navegadores actualizada en tiempo real: {navegadores_instalados}")


# * Ejemplo C: Eliminar un elemento específico por su nombre (.remove)
# ? Si conoces exactamente el texto o valor que quieres sacar de la lista, puedes 
# ? usar el método .remove(). Buscará el elemento y lo borrará de la memoria.
programas_inicio = ["Antivirus", "Spotify", "Steam"]
print(f"Programas al encender la PC (Antes): {programas_inicio}")

# * Desactivamos Spotify del inicio para que la computadora encienda más rápido
programas_inicio.remove("Spotify")
print(f"Programas al encender la PC (Después): {programas_inicio}")


# * Ejemplo D: Insertar un elemento en una posición intermedia (.insert)
# ? El método .append siempre manda todo al final. Si necesitas obligatoriamente 
# ? meter un dato en medio o al principio de la lista, usas .insert(índice, elemento).
cola_impresion = ["Documento_1.pdf", "Documento_3.pdf"]
print(f"Fila de impresión original: {cola_impresion}")

# * Insertamos el Documento_2 justo en la posición intermedia (Índice 1)
cola_impresion.insert(1, "Documento_2.pdf")
print(f"Fila de impresión con documento intercalado: {cola_impresion}")


# * Ejemplo E: Extraer y recuperar el último elemento de la lista (.pop)
# ? El método .pop() hace dos cosas a la vez: elimina el último vagón de la lista, 
# ? pero te entrega su contenido para que puedas guardarlo en otra variable o usarlo.
historial_ventanas = ["Pestaña 1", "Pestaña 2", "Pestaña Cerrada"]

# * Extraemos la última pestaña eliminándola de la lista, pero guardando su nombre
ultima_pestaña = historial_ventanas.pop()

print(f"Lista de pestañas restante: {historial_ventanas}")
print(f"Ventana recuperada mediante .pop(): {ultima_pestaña}")
