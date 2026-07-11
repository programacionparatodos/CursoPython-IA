def dar_alta_gato(datos_gato):
    # * Recibe un diccionario completo con los datos del felino
    print(f" [GATOS] Procesando papeleo de alta para: {datos_gato['nombre']}")

    if datos_gato["esta_enfermo"] == False:
        return f"😺 El gato {datos_gato['nombre']} de sexo {datos_gato['sexo']} está sano y puede ir a casa"
    else:
        return f"⚠️ ¡Alerta! El gato {datos_gato['nombre']} necesita vacunas antes de salir"