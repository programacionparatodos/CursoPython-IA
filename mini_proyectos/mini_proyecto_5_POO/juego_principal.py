# mini_proyecto_5_POO/juego_principal.py

# ==============================================================================
# * [TEMA 10]: MOTOR PRINCIPAL DE INTERACCIÓN Y CONTROL MODULAR (MARVEL ARENA)
# ==============================================================================

import json
import random

# * [TEMA 10]: IMPORTACIÓN COMPLETA DESDE NUESTRO PAQUETE DE POO PERSONALIZADO
from simulador_combate.guerreros import GuerreroFisico
from simulador_combate.hechiceros import HechiceroMistico
from simulador_combate.cientificos import CientificoTecnologico

# * Nombre del archivo físico que guardará el progreso de los héroes en el disco
ARCHIVO_DATOS = "partida_guardada.json"

# ==============================================================================
# * [TEMA 7]: BASE DE DATOS INICIAL (LISTA QUE ANIDA DICCIONARIOS ESTÁNDAR)
# ==============================================================================
# ? Si el archivo JSON no existe en la PC, el sistema usará este catálogo de respaldo
BASE_DATOS_PREDETERMINADA = [
    {"tipo": "Guerrero", "alias": "Hulk", "salud": 100, "extra": "Puños", "victorias": 0},
    {"tipo": "Guerrero", "alias": "Capitán América", "salud": 100, "extra": "Escudo", "victorias": 0},
    {"tipo": "Hechicero", "alias": "Doctor Strange", "salud": 100, "extra": 80, "victorias": 0},
    {"tipo": "Hechicero", "alias": "Scarlet Witch", "salud": 100, "extra": 100, "victorias": 0},
    {"tipo": "Cientifico", "alias": "Iron Man", "salud": 100, "extra": 100, "victorias": 0},
    {"tipo": "Cientifico", "alias": "Doc Ock", "salud": 100, "extra": 100, "victorias": 0}
]

# ==============================================================================
# * FASE 1: FUNCIONES DE PERSISTENCIA Y CONVERSIÓN DE FORMATOS (JSON <-> POO)
# ==============================================================================

# ==========================================================================
# ? ¿Qué hace?: Lee el archivo JSON del disco y restaura la lista de diccionarios.
# ! Parámetros: Ninguno.
# * Retorna: Una lista (list) llena de diccionarios con los datos de los héroes.
# ==========================================================================
def cargar_base_datos_json():
    # * [TEMA 9]: BLINDAJE DEFENSIVO ANTE ARCHIVOS INEXISTENTES CON TRY-EXCEPT
    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            # * [TEMA 9]: Resucitamos la lista de diccionarios desde el archivo físico
            datos_cargados = json.load(archivo)
            print("💾 [SISTEMA]: Registros históricos recuperados con éxito del disco duro.")
            return datos_cargados
    except FileNotFoundError:
        print("🚀 [SISTEMA]: Primera ejecución detectada. Cargando catálogo predeterminado en RAM.")
        return BASE_DATOS_PREDETERMINADA

# ==========================================================================
# ? ¿Qué hace?: Toma los objetos modificados de la RAM y los guarda en el JSON.
# ! Parámetros: lista_objetos_instanciados (list) -> Objetos POO actuales.
# * Retorna: Nada (Escribe de forma permanente en el disco duro).
# ==========================================================================
def guardar_base_datos_json(lista_objetos_instanciados):
    lista_diccionarios_guardado = []

    # * [TEMA 8]: Recorremos cada objeto de la RAM para empaquetarlo de vuelta a diccionario
    for heroe in lista_objetos_instanciados:
        # * Estructura de diccionario base común para cualquier héroe
        dict_heroe = {
            "alias": heroe.alias,
            "salud": 100, # Todos los héroes guardan su progreso curados para la próxima partida
            "victorias": heroe.victorias
        }

        # * [TEMA 6 / TEMA 11]: Identificamos el tipo de objeto para mapear su atributo exclusivo
        if isinstance(heroe, GuerreroFisico):
            dict_heroe["tipo"] = "Guerrero"
            dict_heroe["extra"] = heroe.arma
        elif isinstance(heroe, HechiceroMistico):
            dict_heroe["tipo"] = "Hechicero"
            dict_heroe["extra"] = heroe.mana
        elif isinstance(heroe, CientificoTecnologico):
            dict_heroe["tipo"] = "Cientifico"
            dict_heroe["extra"] = heroe.bateria

        # * [TEMA 7]: Agregamos el diccionario recién construido a la lista de guardado
        lista_diccionarios_guardado.append(dict_heroe)

    # * [TEMA 9]: Volcado físico de la lista de diccionarios al archivo permanente JSON
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(lista_diccionarios_guardado, archivo, indent=4, ensure_ascii=False)
    print("💾 [SISTEMA]: Historial y victorias guardadas de forma segura. ¡Progreso respaldado!")

# ==========================================================================
# ? ¿Qué hace?: Convierte la lista de diccionarios JSON en instancias reales POO.
# ! Parámetros: lista_dicts (list) -> Datos en bruto en formato de diccionario.
# * Retorna: Una lista (list) llena de objetos listos para combatir en la RAM.
# ==========================================================================
def instanciar_personajes(lista_dicts):
    lista_objetos = []
    
    for item in lista_dicts:
        # * [TEMA 6 / TEMA 11]: Traducimos los diccionarios a sus respectivas clases hijas
        if item["tipo"] == "Guerrero":
            nuevo_objeto = GuerreroFisico(item["alias"], item["salud"], item["extra"], item["victorias"])
        elif item["tipo"] == "Hechicero":
            nuevo_objeto = HechiceroMistico(item["alias"], item["salud"], item["extra"], item["victorias"])
        elif item["tipo"] == "Cientifico":
            nuevo_objeto = CientificoTecnologico(item["alias"], item["salud"], item["extra"], item["victorias"])
        
        lista_objetos.append(nuevo_objeto)
    
    return lista_objetos

# ==============================================================================
# * FASE 2: MOTOR DE COMBATE POR TURNOS Y LÓGICA DE JUEGO (MODULARIDAD)
# ==============================================================================

# ==========================================================================
# ? ¿Qué hace?: Simula un combate automático por turnos entre dos objetos héroes.
# ! Parámetros: heroe1 (Objeto POO), heroe2 (Objeto POO).
# * Retorna: El objeto héroe que resultó ganador del encuentro de simulación.
# ==========================================================================
def simular_arena_combate(heroe1, heroe2):
    print(f"\n🏟️  [ARENA]: ¡Inicia el encuentro definitivo entre {heroe1.alias} y {heroe2.alias}!")
    
    # * [TEMA 8]: Bucle de combate que corre mientras ambos contendientes sigan vivos
    while heroe1.esta_vivo and heroe2.esta_vivo:
        # * [TEMA 10]: Determinamos al azar quién ataca primero en este turno
        atacante = random.choice([heroe1, heroe2])
        defensor = heroe2 if atacante == heroe1 else heroe1

        print(f"\n⚡ [TURNO]: Turno de ataque para {atacante.alias}...")
        
        # * [TEMA 10]: Si es un guerrero, tiene un 40% de probabilidad de activar su escudo
        if isinstance(atacante, GuerreroFisico) and random.random() < 0.40:
            atacante.activar_defensa()
            
        # * [TEMA 10]: Si es un hechicero con poca energía, se ve forzado a meditar primero
        if isinstance(atacante, HechiceroMistico) and atacante.mana < 25:
            atacante.meditar()
            continue # Salta el ataque en este turno para recuperar el recurso místico

        # * [TEMA 10]: Si es un científico con batería baja, recarga de forma automática
        if isinstance(atacante, CientificoTecnologico) and atacante.bateria < 20:
            atacante.recargar_nucleo()
            continue

        # * [TEMA 11]: Invocación polimórfica del método atacar()
        daño_generado = atacante.atacar()
        
        # * [TEMA 11]: El defensor procesa el impacto de forma interna y lógica
        defensor.recibir_impacto(daño_generado)

    # * Determinar y coronar al ganador de la ronda de simulación
    ganador = heroe1 if heroe1.esta_vivo else heroe2
    ganador.victorias = ganador.victorias + 1 # [TEMA 5]: Operador incremental
    print(f"\n🏆 [VICTORIA]: ¡{ganador.alias} ha ganado la batalla! Registro total: {ganador.victorias} victorias.")
    return ganador


# ==============================================================================
# * FASE 3: SISTEMA DE INTERACCIÓN PRINCIPAL (EL MENÚ INTERACTIVO)
# ==============================================================================

# * Inicialización del flujo: cargamos los diccionarios JSON y los instanciamos a objetos RAM
datos_en_bruto = cargar_base_datos_json()
lista_heroes_ram = instanciar_personajes(datos_en_bruto)

# * [TEMA 8]: Bucle indefinido para mantener el software operativo continuamente
while True:
    print("\n==========================================")
    print("      ⚔️   MARVEL ARENA SIMULATOR  ⚔️      ")
    print("==========================================")
    print("1. Mostrar salón de héroes y victorias")
    print("2. Desatar batalla aleatoria en la Arena")
    print("3. Curar y restablecer recursos de todos")
    print("4. Salir y respaldar estadísticas (JSON)")
    print("==========================================")
    
    entrada_usuario = input("Seleccione una opción de control (1-4): ")

    # * [TEMA 8]: 🛡️ CLÁUSULA DE GUARDA CONTRA ENTRADAS VACÍAS O TEXTO ERÓNEMO
    if not entrada_usuario.isdigit():
        print("❌ [ALERTA]: Opción inválida. Teclee únicamente números enteros de las opciones.")
        continue

    opcion_elegida = int(entrada_usuario)

    # * [TEMA 8]: ESTRUCTURA MODERNA MATCH-CASE PARA REDUCCIÓN DE IF-ELSE
    match opcion_elegida:

        # ----------------------------------------------------------------------
        # * CASE 1: VISUALIZAR ESTADÍSTICAS Y CLASES ACTUALES
        # ----------------------------------------------------------------------
        case 1:
            print("\n--- 🎖️  SALÓN OFICIAL DE SUPERHÉROES ---")
            for indice, heroe in enumerate(lista_heroes_ram, 1):
                # * Identificamos la clase para mostrar una etiqueta amigable en consola
                clase_str = heroe.__class__.__name__
                salud_actual = heroe.consultar_salud()
                print(f"{indice}. [{clase_str}] {heroe.alias} | Salud: {salud_actual}% | Victorias: {heroe.victorias}")

        # ----------------------------------------------------------------------
        # * CASE 2: FILTRADO Y EJECUCIÓN DEL COMBATE POR TURNOS
        # ----------------------------------------------------------------------
        case 2:
            print("\n--- 🏟️  PREPARANDO LA ARENA DE COMBATE ---")
            
            # * [TEMA 7]: Filtramos la lista mediante comprensión para aislar héroes aptos (vivos)
            heroes_disponibles = [h for h in lista_heroes_ram if h.esta_vivo]
            
            # * 🛡️ CLÁUSULA DE GUARDA: Descartamos el combate si no hay suficientes héroes sanos
            if len(heroes_disponibles) < 2:
                print("⚠️ [AVISO]: No hay suficientes héroes vivos para pelear. Elija la opción 3 primero.")
                continue

            # * [TEMA 10]: Seleccionamos al azar dos peleadores diferentes de la lista filtrada
            peleadores = random.sample(heroes_disponibles, 2)
            
            # * Desatamos el motor modular pasándole ambos objetos instanciados
            simular_arena_combate(peleadores[0], peleadores[1])

        # ----------------------------------------------------------------------
        # * CASE 3: MUTACIÓN MASIVA DE ESTADOS DE LA LISTA
        # ----------------------------------------------------------------------
        case 3:
            print("\n--- 🧪 RESTABLECIENDO SIGNOS VITALES ---")
            for heroe in lista_heroes_ram:
                # * Accedemos de forma directa y lógica a los atributos para resucitarlos
                heroe.esta_vivo = True
                heroe._salud = 100 # Curación controlada
                
                # * Restablecemos los recursos exclusivos de las subclases de forma segura
                if isinstance(heroe, HechiceroMistico):
                    heroe.mana = 80
                elif isinstance(heroe, CientificoTecnologico):
                    heroe.bateria = 100
                    
            print("✅ [SISTEMA]: Todos los personajes han sido sanados y sus recursos recargados.")

        # ----------------------------------------------------------------------
        # * CASE 4: VOLCADO PERMANENTE Y CIERRE DE PROCESOS (PERSISTENCIA)
        # ----------------------------------------------------------------------
        case 4:
            print("\n--- 💾 CERRANDO SESIÓN DE JUEGO ---")
            # * Guardamos las estadísticas reales de la RAM de vuelta a formato de disco JSON
            guardar_base_datos_json(lista_heroes_ram)
            print("👋 [SISTEMA]: Programa finalizado con éxito. ¡Hasta la próxima batalla!")
            break # Rompe de forma definitiva el bucle 'while True' cerrando el software

        # ----------------------------------------------------------------------
        # * CASE DEFAULT: FILTRADO DE VALORES FUERA DE RANGO
        # ----------------------------------------------------------------------
        case _:
            print("❌ [ALERTA]: El número ingresado no está en el menú. Elija del 1 al 4.")






# ==============================================================================
# 🎮 ¡TU TURNO DE PROGRAMAR! - RETO DE AMPLIACIÓN AUTÓNOMO
# ==============================================================================
# ? OBJETIVO: Evaluar tus conocimientos del curso modificando el sistema modular.
# ? Deberás abrir tus archivos independientes y agregar una nueva mecánica
# ? sin romper las reglas de persistencia JSON ni la estructura de paquetes.

# * 🛠️ TU TAREA: "EL SISTEMA DE TIENDA Y POTENCIADORES"
# ? Actualmente, los héroes ganan victorias en el archivo 'juego_principal.py',
# ? pero esas victorias no sirven para nada. ¡Vamos a darles un uso real!

# * PASO 1: Modificar el paquete POO (simulador_combate/base.py)
# ? Agrega un nuevo método dentro de la clase Padre 'PersonajeBase' llamado:
# ?     def equipar_potenciador(self):
# ? Este método debe verificar si el héroe tiene al menos 1 victoria acumulada.
# ? Si la tiene, le restará 1 victoria y le subirá la salud máxima a 120 puntos.
# ? ! Recuerda usar las etiquetas Better Comments para documentar parámetros y retornos.

# * PASO 2: Expandir el menú interactivo (juego_principal.py)
# ? En el bucle principal 'while True', añade una nueva opción en el menú:
# ?     "5. Comprar Potenciador de Salud (Costo: 1 Victoria)"
# ? Modifica el 'match-case' para recibir esta opción. El programa deberá:
# ?   A. Pedirle al usuario que teclee el número del héroe que desea potenciar.
# ?   B. Filtrar la entrada con una cláusula de guarda (.isdigit()) contra letras.
# ?   C. Invocar el nuevo método que creaste en el PASO 1 sobre ese objeto en la RAM.

# * PASO 3: Probar la Persistencia Total
# ? Juega una partida, haz que un héroe gane batallas, entra al menú 5, gasta su 
# ? victoria para potenciarlo, y finalmente sal usando la opción 4. 
# ? ¡Verifica que el archivo 'partida_guardada.json' guarde correctamente los cambios!