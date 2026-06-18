# ==============================================================================
# 5_operadores -> operaciones_strings.py
# ==============================================================================

# ==============================================================================
# BLOQUE 1: Creación, Estructura y Medición
# ==============================================================================

# ==============================================================================
# * SECCIÓN 1: COMBINAR Y REPETIR CADENAS
# ==============================================================================

# ------------------------------------------------------------------------------
# * 1.1 Pegado Tradicional (Concatenación con +)
# ------------------------------------------------------------------------------
# ? Definimos las dos frases icónicas de Avengers
frase_1 = "Yo soy inevitable"
frase_2 = "Y yo soy Iron Man"

# ! ALERTA: La concatenación tradicional no añade espacios automáticos
choque_titanes = frase_1 + frase_2
print("Concatenación directa:", choque_titanes)

# ------------------------------------------------------------------------------
# * 1.2 La Solución Moderna: f-strings (Inyección de Variables)
# ------------------------------------------------------------------------------
# * Colocamos una 'f' antes de las comillas y metemos las variables dentro de llaves {}
dialogo_limpio = f"{frase_1}   VS 🫰  {frase_2}"
print("Diálogo optimizado con f-string:", dialogo_limpio)

# ------------------------------------------------------------------------------
# * 1.3 Fotocopiadora de Texto (Replicación con *)
# ------------------------------------------------------------------------------
# ? Usamos el asterisco para clonar la cadena de texto de forma exacta
risa_villano = "Ja"
risa_completa = risa_villano * 7
print("Risa clonada de Ultrón:", risa_completa)

# ! TRAMPA DE EXAMEN: Rompe el programa por usar tipo decimal (float)
# error_risa = "Ja" * 2.5  # Lanzará un TypeError: can't multiply sequence by non-int of type 'float'

# ==============================================================================
# * SECCIÓN 2: MEDICIÓN DE TEXTOS
# ==============================================================================

# ------------------------------------------------------------------------------
# * 2.1 Medir el Tamaño Real con la Función len()
# ------------------------------------------------------------------------------
# ? Medimos una sola palabra limpia
nombre_corto = "Groot"
print(f"El nombre '{nombre_corto}' mide:", len(nombre_corto), "caracteres.")

# ------------------------------------------------------------------------------
# * 2.2 El Impacto Invisible de los Espacios en Blanco
# ------------------------------------------------------------------------------
# ! ALERTA DE EXAMEN: len() cuenta de forma estricta espacios y signos de puntuación
frase_icono = "Yo soy Groot."
print(f"La frase '{frase_icono}' mide en total:", len(frase_icono), "caracteres.")

# ? Caso Extremo: Cadena vacía (No contiene nada, mide cero)
vacio = ""
print("Longitud de un texto vacío:", len(vacio))

# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa
# ------------------------------------------------------------------------------

# * Ejemplo A: Midiendo mensajes multilínea completos
# ? La función len() también cuenta los saltos de línea (enter) como un carácter invisible (\n).
discurso_corto = """Yo soy
Groot"""
# Explicación: 'Yo'(2) + ' '(1) + 'soy'(3) + 'salto de línea'(1) + 'Groot'(5) = 12
print("Longitud de discurso con salto de línea:", len(discurso_corto)) 

# * Ejemplo B: Validar longitud para simular un límite de caracteres
# ? En el mundo real, len() se usa para que las contraseñas o nombres no sean muy cortos.
nombre_usuario = "Tony"
print(f"¿El nombre '{nombre_usuario}' es seguro? Su tamaño es de {len(nombre_usuario)} letras.")

# ==============================================================================
# BLOQUE 2: Acceso y Cirugía de Cadenas
# ==============================================================================

# ==============================================================================
# * SECCIÓN 3: POSICIONES EN EL TEXTO (INDEXACIÓN)
# ==============================================================================

# ------------------------------------------------------------------------------
# * 3.1 Indexación Positiva (De izquierda a derecha)
# ------------------------------------------------------------------------------
# ? Índices:       0    1    2    3    4    5
# villano =       "T    h    a    n    o    s"

villano = "Thanos"

# * Obtenemos el primer carácter usando el índice base 0
primera_letra = villano[0]
print("La primera letra de nuestro villano es:", primera_letra)

# * Obtenemos la letra de la posición 3
letra_tres = villano[3]
print("La letra en el índice 3 es:", letra_tres)

# ------------------------------------------------------------------------------
# * 3.2 Indexación Negativa (De derecha a izquierda)
# ------------------------------------------------------------------------------
# ? Índices:    [-6] [-5] [-4] [-3] [-2] [-1]
# ? Villano:     T    h    a    n    o    s

# * Obtenemos el último carácter de la fila de forma directa usando -1
ultima_letra = villano[-1]
print("La última letra usando índice negativo es:", ultima_letra)

# ------------------------------------------------------------------------------
# * 3.3 Fórmula de Examen: El Último Índice Válido y el IndexError
# ------------------------------------------------------------------------------
# ? El último índice accesible de forma segura es len(villano) - 1 (6 - 1 = 5)
ultimo_asiento_real = len(villano) - 1
print("El último índice utilizable de forma segura es:", ultimo_asiento_real) 

# ! TRAMPA DE EXAMEN: Acceder a un índice fuera de rango romperá el programa inmediatamente
# error_guantelete = villano[10]  # Lanzará un IndexError: string index out of range

# ==============================================================================
# * SECCIÓN 4: REBANADO DE CADENAS (SLICING)
# ==============================================================================

# ------------------------------------------------------------------------------
# * 4.1 El Cuchillo de Python: Sintaxis [inicio:fin]
# ------------------------------------------------------------------------------
# ? Índices:     012345678910
nombre_heroe =  "Peter Parker"

# * Queremos extraer solo el nombre "Peter" (va del índice 0 al 4)
# ! TRAMPA: Debemos poner como fin el índice 5 para que Python corte exactamente hasta el 4.
nombre = nombre_heroe[0:5]
print("Nombre extraído con [0:5]:", nombre)

# ------------------------------------------------------------------------------
# * 4.2 Atajos Rápidos (Omitir Inicio o Fin)
# ------------------------------------------------------------------------------
# * Si dejas el lado izquierdo vacío, Python empieza automáticamente desde el índice 0
inicio_vacio = nombre_heroe[:5]
print("Corte desde el inicio con [:5]:", inicio_vacio)

# * Si dejas el lado derecho vacío, Python camina hasta el último carácter existente
apellido = nombre_heroe[6:]
print("Apellido extraído con [6:]:", apellido)

# * Si dejas AMBOS lados vacíos, saca una copia exacta y completa del texto original
copia_completa = nombre_heroe[:]
print("Copia completa usando [:]:", copia_completa)

# ------------------------------------------------------------------------------
# * 4.3 Truco de Entrevista de Trabajo: Invertir Texto
# ------------------------------------------------------------------------------
# * Invertimos por completo el sentido de la cadena usando un paso de retroceso
nombre_al_reves = nombre_heroe[::-1]
print("Nombre invertido con [::-1]:", nombre_al_reves)

# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa
# ------------------------------------------------------------------------------

# * Ejemplo A: Combinando len() con Indexación Negativa
# ? Si quieres rastrear el tercer carácter contando desde el final de una palabra.
objeto_magico = "Mjolnir"
antepenultima_letra = objeto_magico[-3]
print(f"Refuerzo: La antepenúltima letra de {objeto_magico} es '{antepenultima_letra}'") 

# * Ejemplo B: Slicing con omisiones extremas en frases largas
# ? Si dejas el fin vacío en un texto largo, Python extrae todo sin importar la longitud.
grito_guerra = "¡Vengadores... Unidos!"
frase_recortada = grito_guerra[14:]
print("Refuerzo (Slicing [14:]):", frase_recortada)

# * Ejemplo C: Inversión de palabras individuales en una f-string
# ? Puedes usar el truco de inversión directamente dentro de un formato de texto ordenado.
heroe_secreto = "Spider-Man"
print(f"Refuerzo: El nombre encriptado de {heroe_secreto} es {heroe_secreto[::-1]}")

# ==============================================================================
# BLOQUE 3: Limpieza, Transformación y Reemplazo
# ==============================================================================

# ==============================================================================
# * SECCIÓN 5: HIGIENE DE DATOS (LIMPIEZA EXTERIOR)
# ==============================================================================

# ------------------------------------------------------------------------------
# * 5.1 El Efecto Formulario y el Uso de .strip()
# ------------------------------------------------------------------------------
# ? Un usuario se registra en la base de datos de S.H.I.E.L.D. e introduce espacios extra:
agente = "   Marcos99   "

# ! SI NO LIMPIAMOS EL TEXTO: Los espacios fantasmas alteran el tamaño real en la memoria
print("Tamaño con errores de espacio:", len(agente))

# * Usamos .strip() para purificar ambos extremos automáticamente
agente_limpio = agente.strip()
print("Texto corregido por Python:", agente_limpio)
print("Tamaño real purificado:     ", len(agente_limpio))

# ------------------------------------------------------------------------------
# ! 5.2 Alerta de Examen: Los Espacios Centrales no se Tocan
# ------------------------------------------------------------------------------
# ? Si aplicamos .strip() a una frase con espacios intermedios, el centro no se altera
frase_con_espacio_interno = "   Tony   Stark   "
print("Resultado de limpieza interna:", frase_con_espacio_interno.strip())

# ==============================================================================
# * SECCIÓN 6: MODIFICACIÓN ESTÉTICA (CONCEPTO DE ORO)
# ==============================================================================

# ------------------------------------------------------------------------------
# * 6.1 Demostración Práctica de la Inmutabilidad
# ------------------------------------------------------------------------------
# ? Escribimos la frase mezclando mayúsculas y minúsculas adrede
frase_cap = "pOdRíA hAcEr EsTo ToDo El DíA"

# ------------------------------------------------------------------------------
# * 6.2 El Trío de Transformación Indispensable
# ------------------------------------------------------------------------------
# * .upper() convierte absolutamente todo a mayúsculas
print("Con .upper(): ", frase_cap.upper()) 

# * .lower() convierte absolutamente todo a minúsculas
print("Con .lower(): ", frase_cap.lower())

# * .title() pone en mayúscula solo la primera letra de cada palabra
print("Con .title(): ", frase_cap.title())

# ! RECORDATORIO DE EXAMEN: La variable original nunca cambió debido a la inmutabilidad
print("Variable original intacta:", frase_cap)

# ==============================================================================
# * SECCIÓN 7: CIRUGÍA DE PALABRAS (MODIFICACIÓN INTERIOR)
# ==============================================================================

# ------------------------------------------------------------------------------
# * 7.1 Reemplazar Fragmentos de Texto con .replace()
# ------------------------------------------------------------------------------
# ? Guardamos una frase con el villano equivocado
orden_batalla = "Ataquen a Thanos de inmediato"
print("Orden original: ", orden_batalla)

# * Reemplazamos "Thanos" por "Ultrón". ¡Recuerden que esto genera una nueva cadena!
nueva_orden = orden_batalla.replace("Thanos", "Ultrón")
print("Orden actualizada:", nueva_orden)

# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa
# ------------------------------------------------------------------------------

# * Ejemplo A: Reasignación de variables para guardar transformaciones (Inmutabilidad)
# ? Como el texto es inmutable, DEBES sobreescribir la variable para salvar los cambios.
nombre_bando = "vengadores"
print("Antes de guardar:", nombre_bando)

nombre_bando = nombre_bando.upper()
print("Después de guardar:", nombre_bando) 

# * Ejemplo B: Encadenamiento de métodos en una sola línea
# ? En Python puedes aplicar un método detrás de otro. Aquí limpiamos bordes y pasamos a Mayúsculas.
entrada_sucia = "    ojo de halcón    "
entrada_perfecta = entrada_sucia.strip().title()
print(f"Refuerzo (Encadenado .strip().title()): '{entrada_perfecta}'")

# * Ejemplo C: Reemplazar caracteres individuales repetidos con .replace()
# ? .replace() no solo cambia palabras completas, cambia CADA coincidencia que encuentre.
coordenadas_error = "S-H-I-E-L-D"
coordenadas_limpias = coordenadas_error.replace("-", "")
print("Refuerzo (.replace de guiones):", coordenadas_limpias)

# ==============================================================================
# BLOQUE 4: Búsqueda, Validación y Fragmentación
# ==============================================================================

# ==============================================================================
# * SECCIÓN 8: DETECTIVES DE FRONTERAS Y FILTROS NATIVOS
# ==============================================================================

# ------------------------------------------------------------------------------
# * 8.1 Inspección de Extremos con .startswith() y .endswith()
# ------------------------------------------------------------------------------
# ? Almacenamos el bloque de discurso de Tony Stark usando triples comillas
discurso_stark = "Todo el mundo quiere un final feliz, te amo tres millones."

# * Comprobamos el inicio exacto del texto
print("¿Empieza con 'Todo'?:", discurso_stark.startswith("Todo"))    

# ! TRAMPA: La sensibilidad a mayúsculas altera el resultado lógico
print("¿Empieza con 'todo'?:", discurso_stark.startswith("todo"))    

# * Comprobamos el final exacto del texto
print("¿Termina con 'millones.'?:", discurso_stark.endswith("millones.")) 

# ------------------------------------------------------------------------------
# * 8.2 El Filtro Más Intuitivo: Operadores 'in' y 'not in'
# ------------------------------------------------------------------------------
# ? Definimos el grito de guerra de Thor para buscar elementos
grito_thor = "¡Tráiganme a Thanos!"

# * 'in' verifica si una subcadena exacta vive dentro del texto (coincidencia pura)
print("¿'Thanos' está en el grito?:", "Thanos" in grito_thor)
print("¿Las letras 'han' están?:", "han" in grito_thor)

# * 'not in' valida la ausencia absoluta de una subcadena
print("¿'IronMan' NO está?:", "IronMan" not in grito_thor)

# ==============================================================================
# * SECCIÓN 9: CONTEO TOTAL
# ==============================================================================

# ------------------------------------------------------------------------------
# * 9.1 Contar Apariciones Exactas con .count()
# ------------------------------------------------------------------------------
# ? El texto contiene la subcadena "te amo" exactamente 2 veces
frase_strange = "Yo te amo, te amo en todos los universos"

# * Contamos todas las ocurrencias exactas en el string
total_confesiones = frase_strange.count("te amo")
print("Conteo total de 'te amo':", total_confesiones)

# ==============================================================================
# * SECCIÓN 10: INTERROGACIÓN Y FRAGMENTACIÓN
# ==============================================================================

# ------------------------------------------------------------------------------
# * 10.1 Validación Estricta de Seguridad (.isalpha / .isdigit)
# ------------------------------------------------------------------------------
# ? Definimos códigos de validación para las armaduras de Iron Man
armadura = "Mark"
codigo = "85"

# * .isalpha() valida que no existan números ni símbolos espaciales
print("¿'Mark' es solo alfabeto?:", armadura.isalpha())

# * .isdigit() valida que contenga únicamente caracteres numéricos enteros
print("¿'85' contiene solo dígitos?:", codigo.isdigit())

# ------------------------------------------------------------------------------
# * 10.2 Romper un Texto en Palabras con .split()
# ------------------------------------------------------------------------------
# ? Guardamos el lema de los Vengadores
lema = "Vengadores Unidos"

# * Rompemos el string en partes individuales usando sus espacios como guillotina
lista_palabras = lema.split()
print("Texto fragmentado con .split():", lista_palabras) 

# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa
# ------------------------------------------------------------------------------

# * Ejemplo A: El peligro del operador 'in' con minúsculas mezcladas
# ? Recuerda que la búsqueda es Case Sensitive. Si buscas un villano, hazlo con la caja correcta.
alerta_radar = "Se detectó la nave de Thanos acercándose."
print("¿thanos (minúscula) está?:", "thanos" in alerta_radar)
print("Solución Inteligente usando .lower():", "thanos" in alerta_radar.lower()) 

# * Ejemplo B: El impacto de .count() en textos que no contienen la palabra
# ? Si buscas un elemento que está ausente, .count() nunca lanzará un error; simplemente devolverá 0.
registro_bajas = "Iron Man, Black Widow"
print("Conteo de 'Capitán' en el registro:", registro_bajas.count("Capitán"))

# * Ejemplo C: El uso de .split() para contar palabras exactas en una frase
# ? Combinando .split() con len(), puedes contar cuántas palabras componen un texto de manera exacta.
discurso_wakanda = "Wakanda por siempre"
palabras_separadas = discurso_wakanda.split()
print(f"El lema tiene exactamente {len(palabras_separadas)} palabras individuales.")