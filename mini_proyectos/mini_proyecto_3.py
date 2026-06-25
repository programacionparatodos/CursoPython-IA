# ==============================================================================
# # mini_proyectos -> mini_proyecto_3.py
# ==============================================================================

# ==============================================================================
# * MINI PROYECTO 3: ASIGNADOR GALÁCTICO DE SUPER MARIO GALAXY 
# ==============================================================================

print("==================================================")
print("   🌌 BIENVENIDO AL COMPUTADOR ESTELAR DE ROSALINA 🌌   ")
print("==================================================")

# ------------------------------------------------------------------------------
# * RECOLECCIÓN DE DATOS CON UN TOQUE DE HUMOR (Inputs y Cadenas)
# ------------------------------------------------------------------------------
nombre = input("Introduce tu nombre de terrícola: ").strip()

edad_input = input("¿Cuántos años terrestres has acumulado?: ").strip()

# * VALIDACIÓN ESTRICTA: Evitamos que el usuario rompa el juego metiendo texto
if not edad_input.isdigit():
    print("\n❌ ¡ERROR ESPACIAL! Bowser hackeó el sistema porque no pusiste un número entero. Fin.")
else:
    edad = int(edad_input)
    
    # ? Recolectamos más datos interactivos
    bebida_favorita = input("¿Qué tomas para programar/jugar? (Café, Agua, Energizante, Destellos): ").strip()
    tiene_hambre = input("¿Tienes hambre ahora mismo? (si/no): ").strip().lower() == "si"
    
    # * OPERADOR TERNARIO: Evaluamos el peligro del estudiante en la galaxia
    estado_peligro = "BOWSER EN POTENCIA" if tiene_hambre else "CIUDADANO DE CONFIANZA"
    
    print("\n==================================================")
    print(f"🌟 ESCANEANDO ADNs DE: {nombre.upper()}")
    print(f"⚠️ CLASIFICACIÓN DE AMENAZA: [{estado_peligro}]")
    print("==================================================\n")
    
    print("--- 🔮 COMPONENTES DE TU DESTINO COSMOLÓGICO ---")
    print("1. Revelar mi Personaje de Mario Galaxy (Uso de if-elif-else)")
    print("2. Registrar mi Signo y Elemento (Uso de .split())")
    print("3. Consultar Destino según tu Bebida (Uso de match-case)")
    
    opcion = input("\nSelecciona un comando estelar (1-3): ").strip()
    
    # --------------------------------------------------------------------------
    # * PROCESAMIENTO DE LAS DECISIONES (Estructuras de Control)
    # --------------------------------------------------------------------------
    match opcion:
        
        case "1":
            print("\nPROCESANDO: Evaluando tu edad y nivel de hambre acumulado...")
            
            # * BUENAS PRÁCTICAS: Cláusula de guarda humorística por si mienten con la edad
            if edad <= 0 or edad > 120:
                print("👽 ALERTA: Eres un alienígena ancestral o un clon. No juegues con el radar.")
            
            # * CAMINO FELIZ: Condicional Anidada para asignar el personaje de Mario Galaxy
            if 0 < edad <= 120:
                if edad >= 30 and not tiene_hambre:
                    print("👑 RESULTADO: ¡Eres PEACH! Controlas el planetario, eres elegante y mantienes el orden en el cosmos.")
                elif edad >= 30 and tiene_hambre:
                    print("🐢 RESULTADO: ¡Eres BOWSER! Quieres robarte todas las estrellas de la galaxia solo porque tienes mal genio y el estómago vacío.")
                elif 18 <= edad < 30:
                    print("🔴 RESULTADO: ¡Eres MARIO! Valiente, listo para saltar de planeta en planeta y rescatar el semestre con código de última hora.")
                else:
                    # * Si son menores de 18 o caen en el descarte por combinaciones
                    if tiene_hambre:
                        print("🦖 RESULTADO: ¡Eres YOSHI! Te da exactamente igual la gravedad del espacio, tú solo quieres comerte a los enemigos y ganar puntos.")
                    else:
                        print("🟢 RESULTADO: ¡Eres LUIGI! Tienes un poquito de miedo de los fantasmas de la galaxia, pero al final del día salvas el día con estilo.")

        case "2":
            print("\nPROCESANDO: El oráculo estelar necesita tu información astral.")
            print("Introduce tu Signo Zodiacal y tu Elemento (Fuego, Agua, Tierra, Aire)")
            entrada_astros = input("Ejemplo (Leo Fuego): ").strip()
            
            # * REPASO: Rompemos la cadena en dos partes usando .split()
            datos_astrales = entrada_astros.split()
            
            # * OPERADOR DE COMPARACIÓN: Validamos que escribiera exactamente dos palabras
            if len(datos_astrales) == 2:
                signo = datos_astrales[0]
                elemento = datos_astrales[1]
                print(f"\n✨ ¡Mapa Astral Sincronizado!")
                print(f"-> Tu Constelación: {signo.capitalize()}")
                print(f"-> Tu Poder Elemental: {elemento.capitalize()}")
                print(f"🚀 Rosalina dice que las estrellas de {elemento.capitalize()} guiarán tus líneas de código.")
            else:
                print("❌ ERROR: El sensor se confundió. Debes poner solo dos palabras (Signo espacio Elemento).")

        case "3":
            print("\nPROCESANDO: Analizando el combustible líquido de tu cuerpo...")
            
            # * CONDICIONAL MÚLTIPLE: Mapeo de la bebida favorita con humor
            match bebida_favorita.lower():
                case "café" | "cafe":
                    print("☕ DESTINO: Eres un Destello (Luma) sobrecargado de energía. Vas a explotar y transformar tu código en una nueva galaxia.")
                case "agua":
                    print("💧 DESTINO: Eres un pingüino del Planeta Glaciación. Mantienes la mente fría y resuelves bugs sin alterarte.")
                case "energizante":
                    print("⚡ DESTINO: Eres Toad corriendo en pánico por el ataque de la flotilla de Bowser. ¡Cálmate un poco!")
                case _:
                    print("🍹 DESTINO: Bebida exótica no identificada. Kamek derramó una poción mágica en tu vaso. ¡Cuidado al compilar!")

        case _:
            print("❌ Comando inválido. Te caíste del planeta y reaparecerás en el Reino Champiñón.")

print("\n==================================================")
print("  🛰️ CONEXIÓN ESTELAR FINALIZADA. ¡SÍGUE PROGRAMANDO! ")
print("==================================================")
