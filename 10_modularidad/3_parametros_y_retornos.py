# ==============================================================================
# # 10_modularidad -> 3_parametros_y_retorno.py
# ==============================================================================

# ==============================================================================
# * FUNCIONES II: PARÁMETROS DE ENTRADA Y EL RETORNO DE DATOS (`RETURN`)
# ==============================================================================

# * Función que simula la ficha técnica de una película (Usa str, int y float)
def mostrar_ficha_pelicula(titulo, año_estreno, calificacion):
    print(f"🎬 [NETFLIX] Película: {titulo}")
    print(f"🗓️ [INFO] Año de lanzamiento: {año_estreno} | Comunidad: {calificacion}/10")

print("--- 3.1 Enviando Datos Dinámicos a la Función ---")
# * Invocamos la misma función pasándole diferentes datos reales en el orden correcto
mostrar_ficha_pelicula("Ironman", 2012, 8)
mostrar_ficha_pelicula("Face Off", 1997, 8.5)

# ------------------------------------------------------------------------------
# * 3.2 El Retorno de Datos (`return`) y su Almacenamiento
# ------------------------------------------------------------------------------

# * Función que calcula el costo total de entradas y su descuento de cine (Usa int y float)
def calcular_costo_boletos(cantidad_personas, precio_boleto):
    total = cantidad_personas * precio_boleto
    descuento = total - (total * 0.10)
    return total, descuento

print("\n--- 3.2 Capturando el resultado de return ---")
# * Llamamos a la función y atrapamos su 'return' dentro de dos variables nuevas
gasto_salida, gasto_salida_descuento = calcular_costo_boletos(2)
print(f"🎫 El costo total para 2 personas en taquilla es de: {gasto_salida} Bs.")
print(f"🎫 El costo total para 2 personas en taquilla con descuento es de: {gasto_salida_descuento} Bs.")

# ! NOTA: No confundas 'print' con 'return'. El 'print' solo dibuja texto en la 
# ! consola. El 'return' entrega un valor real que tu programa puede seguir operando.

# ------------------------------------------------------------------------------
# * 3.3 Parámetros por Defecto (Valores de respaldo o protección)
# ------------------------------------------------------------------------------
# ? Concepto corto: Podemos asignar un valor predeterminado a un parámetro usando `=`. 
# ? Si al llamar la función el usuario olvida enviar ese dato, Python usará el de respaldo.

# * Función para configurar la calidad de video del perfil de streaming
def configurar_reproduccion(perfil_usuario, calidad="Full HD (1080p)"):
    print(f"👤 [PERFIL] Usuario: {perfil_usuario} -> Transmitiendo en: {calidad}")

print("\n--- 3.3 Uso de Parámetros Predeterminados ---")
configurar_reproduccion("Admin") # Toma el valor por defecto automáticamente
configurar_reproduccion("Invitado", "720p") # Sobreescribe el valor por defecto

# ------------------------------------------------------------------------------
# * 3.4 Procesamiento de Estructuras Complejas (Listas y Diccionarios)
# ------------------------------------------------------------------------------

# * Función que analiza las preferencias del usuario (Recibe una lista y un diccionario)
def recomendar_por_genero(historial_vistas, datos_perfil):
    print(f"🤖 Analizando algoritmo para {datos_perfil['nombre']} (País: {datos_perfil['pais']})...")
    print(f"🔍 Evaluando últimas {len(historial_vistas)} categorías vistas...")
    
    if "Ciencia Ficción" in historial_vistas:
        return "✨ Recomendación de hoy: 'Interstellar' o 'Dune'."
    return "🍿 Recomendación de hoy: 'Glass Onion' (Comedia/Misterio)."

print("\n--- 3.4 Pasando Listas y Diccionarios como Parámetros ---")
# * Creamos los datos reales fuera de la función
generos_favoritos = ["Acción", "Drama", "Ciencia Ficción"] # list
usuario_actual = {"nombre": "Carlos", "pais": "México", "suscripcion": "Premium"} # dict

# * Le inyectamos las estructuras completas a la función y guardamos la respuesta
sugerencia_ia = recomendar_por_genero(generos_favoritos, usuario_actual)
print(sugerencia_ia)


# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa
# ------------------------------------------------------------------------------

# * Ejemplo A: Múltiples declaraciones 'return' condicionales (If/Else)
# ? Una función puede tener varios 'return'. El primero que Python encuentre en su 
# ? camino detendrá la ejecución por completo, actuando como un freno de mano.
def verificar_restriccion_edad(edad_usuario):
    if edad_usuario >= 18:
        return "🔓 [ACCESO CONCEDIDO] Catálogo de terror y acción desbloqueado."
    else:
        return "🔒 [ACCESO RESTRINGIDO] Solo contenido apto para todo público."

print("\n--- Refuerzo A: Bifurcaciones con Return ---")
control_parental = verificar_restriccion_edad(15)
print(control_parental)


# * Ejemplo B: Empaquetar y devolver múltiples valores (Uso de Tuplas)
# ? Si separas varios datos con comas en el 'return', Python los agrupará de forma 
# ? automática en una tupla, permitiéndote exportar varios resultados a la vez.
def obtener_estadisticas_maraton(lista_duraciones_minutos):
    total_minutos = sum(lista_duraciones_minutos)
    cantidad_capitulos = len(lista_duraciones_minutos)
    return total_minutos, cantidad_capitulos # Devuelve una tupla inmutable (int, int)

print("\n--- Refuerzo B: Retorno Múltiple de Datos ---")
tiempos_maraton = [45, 52, 48, 50] # list
minutos, capitulos = obtener_estadisticas_maraton(tiempos_maraton)
print(f"📺 Viste {capitulos} capítulos. Tiempo total frente a la pantalla: {minutos} min.")


# * Ejemplo C: Control de duplicados en listas de reproducción (Uso de Sets)
# ? Podemos enviarle una lista con elementos repetidos a una función y usar un set 
# ? interno para limpiar la base de datos de manera inmediata.
def limpiar_historial_busqueda(lista_busquedas):
    # * Convertimos la lista a set para eliminar duplicados de películas
    busquedas_unicas = set(lista_busquedas)
    return busquedas_unicas

print("\n--- Refuerzo C: Limpieza de Estructuras con Sets ---")
historial_sucio = ["Batman", " Shrek", "Batman", "Avatar", "Shrek"]
historial_limpio = limpiar_historial_busqueda(historial_sucio)
print(f"Historial original: {len(historial_sucio)} elementos. Historial limpio: {historial_limpio}")


# * Ejemplo D: Alerta de Código Inalcanzable (Código Muerto)
# ? ¡Cuidado! Cualquier línea de código colocada debajo de un 'return' dentro de 
# ? la misma función se convertirá en código fantasma: Python jamás la leerá.
def calcular_descuento_suscripción(precio_base, porcentaje_desc):
    ahorro = precio_base * (porcentaje_desc / 100)
    return precio_base - ahorro
    print("🚨 [ALERTA ESPÍA] Esta línea jamás se ejecutará porque está abajo del return.")

print("\n--- Refuerzo D: Demostración de Código Muerto ---")
total_pago = calcular_descuento_suscripción(12.00, 15)
print(f"Monto final de la mensualidad con descuento aplicado: ${total_pago}")